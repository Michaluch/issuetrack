from controllers.controller import Controller
from models.backlogs import Backlogs


class Backlog(Controller):
    _backlogs = None

    def __init__(self):
        super(Backlog, self).__init__()
        self._backlogs = Backlogs()

    def get(self, id):
        self._permissions.signed()
        return self._backlogs.get(id)

    def add(self, data):
        self._permissions.signed()
        return self._backlogs.add(data)

    def edit(self, id, data):
        self._permissions.signed()
        return self._backlogs.edit(id, data)

    def delete(self, id):
        self._permissions.signed()
        return self._backlogs.delete(id)

    def all(self, filter):
        self._permissions.signed()
        return self._backlogs.all(filter)
