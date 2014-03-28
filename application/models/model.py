from models.singleton import Singleton
from models.permissions import Permissions


class Model(Singleton):
    def __init__(self):
        super(Model, self).__init__()
