from models.model import Model
from models.db import DB


class Counter(Model):
    _db = None

    def __init__(self):
        super(Counter, self).__init__()
        self._db = DB()
        self._create()

    def _collection(self):
        self._db.collection("counter")

    def _create(self):
        self._collection()
        if not(self._db.check({"_id": "user"})):
            self._db.insert({"_id": "user", "next": 0})
        if not(self._db.check({"_id": "issue"})):
            self._db.insert({"_id": "issue", "next": 0})
        if not(self._db.check({"_id": "subissue"})):
            self._db.insert({"_id": "subissue", "next": 0})
        if not(self._db.check({"_id": "backlog"})):
            self._db.insert({"_id": "backlog", "next": 0})

    def _next(self, name):
        self._collection()
        document = self._db.update_and_select({"_id": name},
                                              {"$inc": {"next": 1}})
        return document["next"]

    def user(self):
        return self._next("user")

    def issue(self):
        return self._next("issue")

    def subissue(self):
        return self._next("subissue")
        
    def subissue(self):
        return self._next("backlog")
