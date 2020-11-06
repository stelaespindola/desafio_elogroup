from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from app.main.model.status import Status
from app.main import db
from ..util.dto import StatusDto
from ..service.status_service import delete_all_status

api = StatusDto.api
_status = StatusDto.status

@api.route('/')
class StatusList(Resource):
    @api.doc('delete_all_status')
    def delete(self):
        delete_all_status()
        return 'ok'

    @api.doc('create_all_status')
    def post(self):
        self.delete()
        a = Status(1,"Cliente em Potencial")
        b = Status(2,"Dados Confirmados")
        c = Status(3,"Reunião Agendada")
        db.session.add(a)
        db.session.add(b)
        db.session.add(c)
        db.session.commit()
        return 'ok'
