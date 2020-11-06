from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import CustomerDto
from ..service.customer_service import get_all_customers, delete_all_customers

api = CustomerDto.api
_customer = CustomerDto.customer

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_all_customers')
    @token_required
    @api.marshal_list_with(_customer, envelope='data')
    @api.doc(security='apikey')
    def get(self):
        """Lists all registered customers"""
        return get_all_customers()

        '''
    @api.doc('delete_all_leads')
    @token_required
    @api.doc(security='apikey')
    @api.doc('delete all leads')
    def delete(self):
        """ Deletes all leads """
        delete_all_leads()
        return "all leads deleted"
        '''
