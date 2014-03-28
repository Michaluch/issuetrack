from models.permissions import Permissions


class Controller(object):
    _permissions = None

    def __init__(self):
        super(Controller, self).__init__()
        self._permissions = Permissions()
