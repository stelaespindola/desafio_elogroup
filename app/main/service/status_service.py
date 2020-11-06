from app.main import db
from app.main.model.status import Status

def get_all_status():
	return Status.query.all()

def delete_all_status():
    all = Status.query.all()
    for status in all:
        db.session.delete(status)

    db.session.commit()

def save_new_status(data):
    status = Status.query.get(data['description'])
    if status is None:
        status=Status(data['description'])
        save_changes(status)

        response_object = {
        	'method': 'save_new_status',
        	'status': 'success',
        	'message': 'Status successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
        	'method': 'save_new_status',
        	'status': 'fail',
        	'message': 'Status already exists.'
        }
        return response_object, 400


def save_changes(data):
	db.session.add(data)
	db.session.commit()
