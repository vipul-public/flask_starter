import datetime
from flask import Response, request
from flask_jwt_extended import create_access_token
from flask_restplus import Namespace, Resource, fields
from database.models import User
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

auth_ns = Namespace('Auth', description='Authentication Endpoints')

userModel = auth_ns.model('User', {
    'email': fields.String(required=True, description='email address'),
    'password': fields.String(required=True, description='password'),
})


@auth_ns.errorhandler(SchemaValidationError)
def handle_file_does_not_exists_exception(error):
    return {'message': 'Invalid input'}, 400

@auth_ns.errorhandler(EmailAlreadyExistsError)
def handle_non_unique_exception(error):
    return {'message': 'Email already exists'}, 400

@auth_ns.errorhandler(UnauthorizedError)
def handle_unauthorised_exception(error):
    return {'message': 'Invalid username or password'}, 401

@auth_ns.errorhandler(InternalServerError)
def handle_non_unique_exception(error):
    return {'message': 'Something went wront ..'}, 500


@auth_ns.route('/signup')
class SignupApi(Resource):
    @auth_ns.expect(userModel)
    def post(self):
        try:
            body = request.get_json()
            user =  User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

@auth_ns.route('/login')
class LoginApi(Resource):
    @auth_ns.expect(userModel)
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
