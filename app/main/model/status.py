from .. import db

class Status(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(255))
	leads = db.relationship('Lead', backref='status', lazy='dynamic')

	def __init__(self, id, description):
		self.id = id
		self.description = description

	def __repr__(self):
		return '<Status id: %r>' % self.id
