from .. import db

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lead_id = db.Column(db.Integer, db.ForeignKey('elo_lead.id'))

	def __init__(self, lead):
		self.lead = lead

	def __repr__(self):
		return '<Customer lead_id: %r>' % self.lead_id
