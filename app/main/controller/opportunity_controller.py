from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import OpportunityDto
from ..service.opportunity_service import get_all_opportunities

api = OpportunityDto.api
_opp = OpportunityDto.customer

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_all_opportunities')
    @token_required
    @api.marshal_list_with(_opp, envelope='data')
    @api.doc(security='apikey')
    def get(self):
        """Lists all registered opportunities"""
        return get_all_opportunities()

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
