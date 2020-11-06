# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.lead_controller import api as lead_ns
from .main.controller.status_controller import api as status_ns
from .main.controller.customer_controller import api as customer_ns
from .main.controller.opportunity_controller import api as opp_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='Desafio EloGroup',
          version='1.0',
          description='Desafio proposto pela Elogroup para processo seletivo',
          authorizations= authorizations
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(lead_ns, path='/lead')
api.add_namespace(customer_ns, path='/customer')
api.add_namespace(opp_ns, path='/opportunity')
#api.add_namespace(status_ns, path='/status') # Not safe - use for populating the status db
api.add_namespace(auth_ns)
#cw6VNhUfoZjsuIofue6og5uRT4kRiOk/
