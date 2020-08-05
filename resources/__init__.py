from flask_restplus import Api

from .info import info_ns
from .auth import auth_ns

api = Api(
    title='Flask Restful',
    version='1.0.0',
    description='Starter Template',
    # All API metadatas
)

api.add_namespace(auth_ns, path='/api/auth')
api.add_namespace(info_ns, path='/api/info')
