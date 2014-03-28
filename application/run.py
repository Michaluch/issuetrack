from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from helper import result
from models.permissions import PermissionsError
from controllers.user import User
from controllers.backlog import Backlog
from controllers.issue import Issue
from controllers.subissue import Subissue


app = Flask("Issuetrack")
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# template

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<path:path>/")
def index_redirect(path=None):
    return redirect("/")
    
    
# error

@app.errorhandler(PermissionsError)
def error_permissions(error):
    return result(dict({"error": "Permissions error"})), 401


# user

@app.route("/api/user/<int:id>/", methods=["GET"])
def user_get(id):
    return result(User().get(id))


@app.route("/api/user/", methods=["POST"])
def user_add():
    return result(User().add(request.json))


@app.route("/api/user/<int:id>/", methods=["PUT"])
def user_edit(id):
    return result(User().edit(id, request.json))


@app.route("/api/user/<int:id>/", methods=["DELETE"])
def user_delete(id):
    return result(User().delete(id))


@app.route("/api/user/all/", methods=["GET"])
def user_all():
    return result(User().all(request.args))


@app.route("/api/user/current/", methods=["GET"])
def user_current():
    return result(User().current())


@app.route("/api/user/current/", methods=["POST"])
def user_signin():
    return result(User().signin(request.form))


@app.route("/api/user/current/", methods=["DELETE"])
def user_signout():
    print "LOGOUT"
    return result(User().signout())


# backlog

@app.route("/api/backlog/<int:id>/", methods=["GET"])
def backlog_get(id):
    return result(Backlog().get(id))

@app.route("/api/backlog/", methods=["POST"])
def backlog_add():
    return result(Backlog().add(request.json))

@app.route("/api/backlog/<int:id>/", methods=["PUT"])
def backlog_edit(id):
    return result(Backlog().edit(id, request.json))

@app.route("/api/backlog/<int:id>/", methods=["DELETE"])
def backlog_delete(id):
    return result(Backlog().get(id))

@app.route("/api/backlog/all/", methods=["GET"])
def backlog_all():
    return result(Backlog().all(request.args))


# issue

@app.route("/api/issue/<int:id>/", methods=["GET"])
def issue_get(id):
    return result(Issue().get(id))


@app.route("/api/issue/", methods=["POST"])
def issue_add():
    return result(Issue().add(request.json))


@app.route("/api/issue/<int:id>/", methods=["PUT"])
def issue_edit(id):
    return result(Issue().edit(id, request.json))


@app.route("/api/issue/<int:id>/", methods=["DELETE"])
def issue_delete(id):
    return result(Issue().delete(id))


@app.route("/api/issue/all/", methods=["GET"])
def issue_all():
    return result(Issue().all(request.args))


# subissue

@app.route("/api/subissue/<int:id>/", methods=["GET"])
def subissue_get(id):
    return result(Subissue().get(id))


@app.route("/api/subissue/", methods=["POST"])
def subissue_add():
    return result(Subissue().add(request.json))


@app.route("/api/subissue/<int:id>/", methods=["PUT"])
def subissue_edit(id):
    return result(Subissue().edit(id, request.json))


@app.route("/api/subissue/<int:id>/", methods=["DELETE"])
def subissue_delete(id):
    return result(Subissue().delete(id))


@app.route("/api/subissue/all/", methods=["GET"])
def subissue_all():
    return result(Subissue().all(request.args))


# main

if __name__ == "__main__":
    app.run(port=8080, debug=True)
