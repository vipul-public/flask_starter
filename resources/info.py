import datetime
import os
from flask import Response, request
from flask_jwt_extended import create_access_token
from flask_restplus import Namespace, Resource, fields
from resources.errors import InternalServerError

info_ns = Namespace('Info', description='Informational Endpoints')

@info_ns .errorhandler(InternalServerError)
def handle_non_unique_exception(error):
    return {'message': 'Something went wront ..'}, 500


@info_ns .route('/health')
class HealthApi(Resource):
    def get(self):
        try:
            # Check health of components here
            return {'status': 'healthy'}, 200
        except Exception as e:
            raise InternalServerError

@info_ns .route('/version')
class VersionApi(Resource):
    def get(self):
        try:
            return {'version': os.environ.get('VERSION')}, 200
        except Exception as e:
            raise InternalServerError
