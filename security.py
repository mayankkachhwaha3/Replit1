from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # check if username and password are valid
    if username == 'admin' and password == 'secret':
        return True
    else:
        return False


from flask_principal import Principal, Permission, RoleNeed

principals = Principal()

admin_permission = Permission(RoleNeed('admin'))

@principals.identity_loader
def load_identity_from_request():
    # this function should return an Identity object with the user's identity
    # you can get the user's identity from a database or token
    identity = Identity(1)
    return identity

@principals.identity_saver
def save_identity_to_request(identity):
    # this function should save the identity to the request
    pass

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day"]
)