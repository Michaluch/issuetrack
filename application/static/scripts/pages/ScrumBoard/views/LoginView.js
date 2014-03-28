define(["pages/ScrumBoard/Environment",
        "text!pages/ScrumBoard/html/LoginView.html",
        "css!pages/ScrumBoard/css/LoginView.css"],

    function(environment, loginHTML, loginCSS) {
        return Backbone.View.extend({
            id: "login",

            template: _.template(loginHTML),

            events: {
                "submit #login-form": "signin"
            },

            render: function () {
                this.$el.html(this.template());
 
                return this;
            },

            signin: function (event) {
                event = event || window.event;
                event.preventDefault ? event.preventDefault() : (event.returnValue = false);

                environment.user.signin(this.$el.find("#login-form input[name=email]").val(), 
                                       this.$el.find("#login-form input[name=password]").val());

                return false;
            }
        });    
    }
);
