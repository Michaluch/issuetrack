from flask import session

from controllers.controller import Controller
from models.users import Users


class User(Controller):
    _users = None

    def __init__(self):
        super(User, self).__init__()
        self._users = Users()

    def get(self, id):
        self._permissions.signed()
        data = self._users.get(id)
        if "password" in data:
            del data["password"]
        return data

    def add(self, data):
        self._permissions.signed()
        return self._users.add(data)

    def edit(self, id, data):
        self._permissions.signed()
        return self._users.edit(id, data)

    def delete(self, id):
        self._permissions.signed()
        return self._users.delete(id)

    def all(self, filter):
        self._permissions.signed()
        data = self._users.all(filter)
        for item in data:
            if "password" in item:
                del item["password"]
        return data

    def current(self):
        return self._users.check(session.get("email"), session.get("password"))

    def signin(self, data):
        user = self._users.check(data.get("email"), data.get("password"))
        if "email" in user and "password" in user:
            session["email"] = user["email"]
            session["password"] = user["password"]
        return self.current()

    def signout(self):
        session.pop('email', None)
        session.pop('password', None)
        return self.current()
