import datetime

from app.main import db
from app.main.model.lead import Lead
from app.main.model.status import Status


from app.main.service.business_rules import is_valid_status_change, need_new_customer, need_to_book_meeting
from app.main.service.customer_service import save_new_customer
from app.main.service.opportunity_service import save_new_opportunity, change_all_opportunities_description

def get_all_leads():
	return Lead.query.all()

def get_lead_by_id(id):
	lead = Lead.query.get(id)
	return lead


def save_new_lead(data):
	status = Status.query.get(1)
	new_lead = Lead(data['customer_name'], data['customer_phone'], data['customer_email'], status)
	status.leads.append(new_lead)
	save_changes(status)
	for oportunity in data['oportunities']:
		save_new_opportunity(new_lead, oportunity)
	response_object = {
		'method': 'save_new_lead',
		'status': 'success',
		'message': 'Successfully registered.'
	}
	return response_object, 201

def delete_all_leads():
	all = Lead.query.all()
	for lead in all:
		db.session.delete(lead)

	db.session.commit()


def change_lead_status(data):

	lead = get_lead_by_id(data['id'])
	if lead is None:
		response_object = {
			'method': 'change_lead_status',
			'status': 'fail',
			'message': 'Lead not found.'
		}
		return response_object, 404

	old_status = lead.status
	new_status = Status.query.filter_by(id=data['status']).first()

	if new_status is None:
		response_object = {
			'method': 'change_lead_status',
			'status': 'fail',
			'message': 'New status not found.'
		}
		return response_object, 404

	if is_valid_status_change(old_status, new_status):
		old_status.leads.remove(lead)
		new_status.leads.append(lead)

		if(need_new_customer(new_status)):
			save_new_customer(lead)
		if(need_to_book_meeting(new_status)):
			date = data["date"].strftime("%m/%d/%Y %H:%M")
			change_all_opportunities_description(" Agendado: "+ date)

		save_changes(old_status)
		save_changes(new_status)

		response_object = {
			'method': 'change_lead_status',
			'status': 'success',
			'message': 'Status successfully changed.'
		}
		return response_object, 201
	else:
		response_object = {
			'method': 'change_lead_status',
			'status': 'fail',
			'message': 'Fail to change status.'
		}
		return response_object, 404

def save_changes(data):
	db.session.add(data)
	db.session.commit()
