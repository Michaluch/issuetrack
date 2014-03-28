define([],

    function() {
        return Backbone.Model.extend({
            idAttribute : "_id",
            url: function () {
                return "/api/user/" + this.id + "/";
            },

            signin: function (email, password) {
                this.fetch({type: "POST", data:{
                    "email": email,
                    "password": password
                }});
            },

            signout: function () {
                this.clear({silent: true});
                this.fetch({type: "DELETE"});
            }
        });
    }
)
