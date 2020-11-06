from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import LeadDto
from ..service.lead_service import get_all_leads, save_new_lead, change_lead_status, delete_all_leads

api = LeadDto.api
_lead = LeadDto.lead
_lead_status = LeadDto.lead_status
_lead_customer = LeadDto.lead_customer
@api.route('/')
class LeadList(Resource):
    @api.doc('list_of_registered_leads')
    @token_required
    @api.marshal_list_with(_lead_customer, envelope='data')
    @api.doc(security='apikey')
    def get(self):
        """Lists all registered leads"""
        return get_all_leads()

    @api.expect(_lead, validate=True)
    @api.response(201, 'Lead successfully created.')
    @token_required
    @api.doc(security='apikey')
    @api.doc('create a new lead')
    def post(self):
        """Creates a new Lead """
        data = request.json
        return save_new_lead(data=data)

    @api.doc('change_lead_status')
    @api.expect(_lead_status, validate=True)
    @api.response(201, 'Lead status successfully changed.')
    @token_required
    @api.doc(security='apikey')
    @api.doc('change lead status')
    def put(self):
        """ Changes lead status """
        data = request.json
        return change_lead_status(data=data)

    @api.doc('delete_all_leads')
    @token_required
    @api.doc(security='apikey')
    @api.doc('delete all leads')
    def delete(self):
        """ Deletes all leads """
        delete_all_leads()
        return "all leads deleted"
