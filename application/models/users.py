from models.model import Model
from models.db import DB
from models.counter import Counter


class Users(Model):
    _db = None

    _fields = {"_id": 1, 
               "email": 1,
               "password": 1,
               "first_name": 1,
               "last_name": 1,
               "status": 1}

    def __init__(self):
        super(Users, self).__init__()
        self._db = DB()

    def _collection(self):
        self._db.collection("users")

    def get(self, id):
        self._collection()
        cursor = self._db.select_one({"_id": id}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()
        
    def check(self, email, password):
        self._collection()
        cursor = self._db.select_one({"email": email, "password": password}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()

    def add(self, data):
        id = Counter().user()
        self._collection()
        self._db.insert({"_id": id,
                         "email": data["email"],
                         "password": data["password"],
                         "first_name": data["first_name"],
                         "last_name": data["last_name"],
                         "status": data["status"]})
        return self.get(id)

    def edit(self, id, data):
        self._collection()
        where = {"_id": id}

        value = dict()
        if data["email"] is not None:
            value["email"] = data["email"]
        if data["password"] is not None:
            value["password"] = data["password"]
        if data["first_name"] is not None:
            value["first_name"] = data["first_name"]
        if data["last_name"] is not None:
            value["last_name"] = data["last_name"]
        if data["status"] is not None:
            value["status"] = data["status"]

        self._db.update(where, {"$set": value})
        return self.get(id)

    def delete(self, id):
        self._collection()
        self._db.delete({"_id": id})
        return self.get(id)

    def all(self, filter):
        self._collection()
        where = dict()

        if "status" in filter:
            where["status"] = filter["status"]
        
        cursor = self._db.select(where, self._fields)
        return [item for item in cursor]
