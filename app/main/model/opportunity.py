from .. import db

class Opportunity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	lead_id = db.Column(db.Integer, db.ForeignKey('elo_lead.id'))
	description = db.Column(db.String(255))

	def __init__(self, lead, description):
		self.lead = lead
		self.description = description

	def __repr__(self):
		return '<Oportunity id: %r>' % self.id
