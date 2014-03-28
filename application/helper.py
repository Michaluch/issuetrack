from flask import json
from hashlib import sha512


def result(data):
    return json.dumps(data)


def sha512(text):
    return sha512(text).hexdigest()
