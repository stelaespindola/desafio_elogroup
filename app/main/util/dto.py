from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'token': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password '),
    })

class LeadDto:
    api = Namespace('lead', description='lead related operations')
    lead = api.model('lead', {
        'customer_name': fields.String(required=True, description='customer name'),
        'customer_phone': fields.String(required=True, description='customer phone'),
        'customer_email': fields.String(required=True, description='customer email'),
        'oportunities': fields.List(
            fields.String(attribute='description', required=False),
            description='array of oportunities',
            attribute='oportunities',
			required = True
        )
    })

    lead_customer = api.model('lead_status', {
        'id': fields.String(required=True, description='lead id'),
        'customer_name': fields.String(required=True, description='customer name'),
        'status': fields.String(required=True, attribute='status.id', description='new status id')
    })

    lead_status = api.model('lead_status', {
        'id': fields.String(required=True, description='lead id'),
        'status': fields.String(required=True, attribute='status.id', description='new status id'),
        'date': fields.DateTime(description='date of meeting - new status = 3')
    })

class StatusDto:
    api = Namespace('status', description='status related operations')
    status = api.model('status', {
        'description': fields.String(required=True, description='status description')
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'id': fields.String(required=True, description='clients id'),
        'lead_id': fields.String(required=True, attribute='lead.id', description='lead id')
    })

class OpportunityDto:
    api = Namespace('opportunity', description='opportunity related operations')
    customer = api.model('opportunity', {
        'id': fields.String(required=True, description='opportunity id'),
        'description': fields.String(required=True, description='opportunity description'),
        'lead_id': fields.String(required=True, attribute='lead.id', description='lead id')
    })
