define(["pages/ScrumBoard/Environment",
        "text!pages/ScrumBoard/html/HeaderView.html",
        "css!pages/ScrumBoard/css/HeaderView.css"],

    function(environment, headerHTML, headerCSS) {
        return Backbone.View.extend({
            id: "header",

            template: _.template(headerHTML),

            events: {
                "click #logout-button": "signout",
                "click #header-logo": "sprint",
                "click #a-team-member": "profile",
                "click #userpick": "profile"
            },

            render: function() {
                var user = null;
                if (environment.signed()) {
                    user = environment.user.toJSON();
                    user.name = (user.first_name + user.last_name).trim();
                }
            
                this.$el.html(this.template({"user": user}));

                return this;
            },

            signout: function (event) {
                environment.user.signout();
            },
            
            sprint: function (event) {
                environment.router.navigate("sprint", {trigger: true});
            },
            
            profile: function (event) {
                environment.router.navigate("profile", {trigger: true});
            }           
        });    
    }
);
