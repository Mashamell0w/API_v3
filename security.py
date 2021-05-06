from users import User


def authenticate(user_name, password):
    user = User.find_by_username(user_name)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
