from controllers.controller import Controller
from models.issues import Issues


class Issue(Controller):
    _issues = None

    def __init__(self):
        super(Issue, self).__init__()
        self._issues = Issues()

    def get(self, id):
        self._permissions.signed()
        return self._issues.get(id)

    def add(self, data):
        self._permissions.signed()
        return self._issues.add(data)

    def edit(self, id, data):
        self._permissions.signed()
        return self._issues.edit(id, data)

    def delete(self, id):
        self._permissions.signed()
        return self._issues.delete(id)

    def all(self, filter):
        self._permissions.signed()
        return self._issues.all(filter)
