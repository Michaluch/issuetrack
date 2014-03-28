from models.model import Model
from models.db import DB
from models.counter import Counter


class Subissues(Model):
    _db = None

    _fields = {"_id": 1,
               "issue": 1, 
               "name": 1,
               "description": 1,
               "status": 1,
               "kind": 1,
               "estimate": 1,
               "assign": 1}

    def __init__(self):
        super(Subissues, self).__init__()
        self._db = DB()

    def _collection(self):
        self._db.collection("subissues")

    def get(self, id):
        self._collection()
        cursor = self._db.select_one({"_id": id}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()

    def add(self, data):
        id = Counter().subissue()
        self._collection()
        self._db.insert({"_id": id,
                         "issue": data["issue"],
                         "name": data["name"],
                         "description": data["description"],
                         "status": data["status"],
                         "kind": data["kind"],
                         "estimate": data["estimate"],
                         "assign": data["assign"]})
        return self.get(id)

    def edit(self, id, data):
        self._collection()
        where = {"_id": id}

        value = dict()
        if data["issue"] is not None:
            value["issue"] = data["issue"]
        if data["name"] is not None:
            value["name"] = data["name"]
        if data["description"] is not None:
            value["description"] = data["description"]
        if data["status"] is not None:
            value["status"] = data["status"]
        if data["kind"] is not None:
            value["kind"] = data["kind"]
        if data["estimate"] is not None:
            value["estimate"] = data["estimate"]
        if data["assign"] is not None:
            value["assign"] = data["assign"]

        self._db.update(where, {"$set": value})
        return self.get(id)

    def delete(self, id):
        self._collection()
        self._db.delete({"_id": id})
        return self.get(id)

    def all(self, filter):
        self._collection()
        where = dict()

        if "issue" in filter:
            where["issue"] = int(filter["issue"])
        if "status" in filter:
            where["status"] = filter["status"]
        
        cursor = self._db.select(where, self._fields)
        return [item for item in cursor]
