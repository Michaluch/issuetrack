from flask import session

from models.singleton import Singleton
from models.db import DB


class PermissionsError(Exception):
    pass
   

class Permissions(Singleton):
    _db = None
    
    _fields = {"_id": 1, 
               "email": 1,
               "password": 1,
               "status": 1}

    def __init__(self):
        super(Permissions, self).__init__()
        self._db = DB()

    def _collection(self):
        self._db.collection("users")
        
    def user(self):
        self._collection()
        cursor = self._db.select_one({"email": session.get("email"), "password": session.get("password")}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()

    def signed(self):
        if self.user().get("email") is None:
            raise PermissionsError
    
    def admin(self):
        if self.user().get("email") is None:
            raise PermissionsError

    def developer(self):
        if self.user().get("email") is None:
            raise PermissionsError

    def watcher(self):
        if self.user().get("email") is None:
            raise PermissionsError
