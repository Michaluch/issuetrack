from models.model import Model
from models.db import DB
from models.counter import Counter


class Backlogs(Model):
    _db = None
    
    _fields = {"_id": 1, 
               "name": 1,
               "sprint": 1}

    def __init__(self):
        super(Backlogs, self).__init__()
        self._db = DB()

    def _collection(self):
        self._db.collection("backlogs")
        
    def get(self, id):
        self._collection()
        cursor = self._db.select_one({"_id": id}, self._fields)
        return cursor[0] if cursor.count() > 0 else dict()

    def add(self, data):
        id = Counter().issue()
        self._collection()
        self._db.insert({"_id": id,
                         "name": data["name"],
                         "sprint": data["sprint"]})
        return self.get(id)

    def edit(self, id, data):
        self._collection()
        where = {"_id": id}

        value = dict()
        if data["name"] is not None:
            value["name"] = data["name"]
        if data["sprint"] is not None:
            value["sprint"] = data["sprint"]

        self._db.update(where, {"$set": value})
        return self.get(id)

    def delete(self, id):
        self._collection()
        self._db.delete({"_id": id})
        return self.get(id)

    def all(self, filter):
        self._collection()
        where = dict()
     
        cursor = self._db.select(where, self._fields)
        return [item for item in cursor]

