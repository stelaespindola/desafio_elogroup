from app.main.model.user import User

class Auth:

	@staticmethod
	def login_user(data):
		try:
			user = User.query.filter_by(username=data.get('username')).first()
			if user and user.check_password(data.get('password')):
				auth_token = user.get_token()
				response_object = {
					'method': 'login_user',
					'status': 'success',
					'message': 'Successfully logged in.',
					'Authorization': auth_token
				}
				return response_object, 200
			else:
				response_object = {
					'method': 'login_user',
					'status': 'fail',
					'message': 'username or password does not match.'
				}
				return response_object, 401
		except Exception as e:
			print(e)
			response_object = {
				'method': 'login_user',
				'status': 'fail',
				'message': 'Try again'
			}
			return response_object, 500

	@staticmethod
	def logout_user(token):
		user = User.get_user_by_token(token)
		if user:
			user.revoke_token()
			response_object = {
				'method': 'logout_user',
				'status': 'success',
				'message': 'Successfully logged out.'
			}
			return response_object, 200
		else:
			response_object = {
				'method': 'logout_user',
				'status': 'fail',
				'message': 'Provide a valid auth token.'
			}
			return response_object, 403

	@staticmethod
	def get_logged_in_user(new_request):
		# get the auth token
		auth_token = new_request.headers.get('Authorization')
		print(new_request.headers)

		if auth_token:
			user = User.get_user_by_token(auth_token)
			if user:
				response_object = {
					'method': 'get_logged_in_user',
					'status': 'success',
					'data': {
						'user_id': user.id,
						'username': user.username
					}
				}
				return response_object, 200
			else:
				response_object = {
					'method': 'get_logged_in_user',
					'status': 'fail',
					'message': 'Provide a valid auth token.'
				}
				return response_object, 401
		else:
			response_object = {
				'method': 'get_logged_in_user',
				'status': 'fail',
				'message': 'Provide a valid auth token.'
			}
			return response_object, 401
