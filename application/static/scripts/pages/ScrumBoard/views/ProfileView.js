define(["pages/ScrumBoard/Environment",
        "text!pages/ScrumBoard/html/ProfileView.html",
        "css!pages/ScrumBoard/css/ProfileView.css"],

    function(environment, profileHTML, profileCSS) {
        return Backbone.View.extend({
            id: "profile",

            template: _.template(profileHTML),

            events: {
                "submit #profile-form": "change"
            },

            render: function() {
                this.$el.html(this.template());

                this.$("#profile-form input[name=email]").val(environment.user.get("email"));
                this.$("#profile-form input[name=first_name]").val(environment.user.get("first_name"));
                this.$("#profile-form input[name=last_name]").val(environment.user.get("last_name"));
 
                return this;
            },

            change: function (event) {
                event = event || window.event;
                event.preventDefault ? event.preventDefault() : (event.returnValue = false);

                environment.user.save({
                    "email": this.$("#profile-form input[name=email]").val(),
                    "first_name": this.$("#profile-form input[name=first_name]").val(),
                    "last_name": this.$("#profile-form input[name=last_name]").val(),
                    "wait": true
                });
            }
        });    
    }
);
