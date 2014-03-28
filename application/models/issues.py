from models.model import Model
from models.db import DB
from models.counter import Counter


class Issues(Model):
    _db = None

    _fields = {"_id": 1, 
               "name": 1,
               "description": 1,
               "kind": 1}

    def __init__(self):
        super(Issues, self).__init__()
        self._db = DB()

    def _collection(self):
        self._db.collection("issues")

    def get(self, id):
        self._collection()
        cursor = self._db.select_one({"_id": id}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()

    def add(self, data):
        id = Counter().issue()
        self._collection()
        self._db.insert({"_id": id,
                         "name": data["name"],
                         "description": data["description"],
                         "kind": data["kind"]})
        return self.get(id)

    def edit(self, id, data):
        self._collection()
        where = {"_id": id}

        value = dict()
        if data["name"] is not None:
            value["name"] = data["name"]
        if data["description"] is not None:
            value["description"] = data["description"]
        if data["kind"] is not None:
            value["kind"] = data["kind"]

        self._db.update(where, {"$set": value})
        return self.get(id)

    def delete(self, id):
        self._collection()
        self._db.delete({"_id": id})
        return self.get(id)

    def all(self, filter):
        self._collection()
        where = dict()
        
        if "sprint" in filter:
            where["sprint"] = int(filter["sprint"])
       
        cursor = self._db.select(where, self._fields)
        return [item for item in cursor]
