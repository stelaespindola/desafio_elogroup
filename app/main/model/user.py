from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from datetime import datetime, timedelta
import base64
import os

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	token = db.Column(db.String(32), index=True, unique=True)
	token_expiration = db.Column(db.DateTime)

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def get_token(self, expires_in=3600):
		now = datetime.utcnow()
		if self.token and self.token_expiration > now:
			return self.token
		self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
		self.token_expiration = now + timedelta(seconds=expires_in)
		db.session.add(self)
		db.session.commit()
		return self.token

	def revoke_token(self):
		self.token_expiration = datetime.now() - timedelta(seconds=1)
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def get_user_by_token(token):
		user = User.query.filter_by(token=token).first()
		if user is None or user.token_expiration < datetime.now():
			return None
		return user

	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return '<User id: %r>' % self.id
