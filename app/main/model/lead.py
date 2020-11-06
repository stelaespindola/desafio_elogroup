from .. import db
from datetime import datetime
from app.main.model.customer import Customer
from app.main.model.opportunity import Opportunity

class Lead(db.Model):
	__tablename__ = "elo_lead"
	id = db.Column(db.Integer, primary_key=True)
	creation_time = db.Column(db.DateTime)
	customer_name = db.Column(db.String(255))
	customer_phone = db.Column(db.String(255))
	customer_email = db.Column(db.String(255))
	status_id = db.Column(db.Integer, db.ForeignKey('status.id'))

	customers = db.relationship('Customer', backref='lead', lazy='dynamic')
	oportunities = db.relationship('Oportunity', backref='lead', lazy='dynamic')

	def __init__(self, customer_name, customer_phone, customer_email, status):
		self.date = datetime.now()
		self.customer_name = customer_name
		self.customer_phone = customer_phone
		self.customer_email = customer_email
		self.status = status

	def __repr__(self):
		return '<Lead customerName: %r>' % self.customer_name
