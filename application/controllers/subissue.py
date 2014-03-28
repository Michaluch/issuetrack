from controllers.controller import Controller
from models.subissues import Subissues


class Subissue(Controller):
    _subissues = None

    def __init__(self):
        super(Subissue, self).__init__()
        self._subissues = Subissues()

    def get(self, id):
        self._permissions.signed()
        return self._subissues.get(id)

    def add(self, data):
        self._permissions.signed()
        return self._subissues.add(data)

    def edit(self, id, data):
        self._permissions.signed()
        return self._subissues.edit(id, data)

    def delete(self, id):
        self._permissions.signed()
        return self._subissues.delete(id)

    def all(self, filter):
        self._permissions.signed()
        return self._subissues.all(filter)
