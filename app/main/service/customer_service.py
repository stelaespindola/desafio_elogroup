from app.main import db
from app.main.model.customer import Customer


def get_all_customers():
	return Customer.query.all()

def get_customers_by_lead(data):
	return Customer.query.filter_by(lead_id=data["lead_id"])


def save_new_customer(lead):
	new_customer = Customer(lead)
	save_changes(new_customer)

	response_object = {
		'method': 'save_new_customer',
		'status': 'success',
		'message': 'New customer successfully registered.'
	}
	return response_object, 201

def delete_all_customers():
	all = Customers.query.all()
	for customer in all:
		db.session.delete(customer)

	db.session.commit()

def save_changes(data):
	db.session.add(data)
	db.session.commit()
