define(["pages/ScrumBoard/Environment",
        "pages/ScrumBoard/views/PageView",
        "pages/ScrumBoard/views/LoginView",
        "pages/ScrumBoard/views/ProfileView",
        "pages/ScrumBoard/views/SprintView",
        "pages/ScrumBoard/views/BacklogView"],

    function(environment, PageView, LoginView, ProfileView, SprintView, BacklogView) {
        return Backbone.Router.extend({
            routes: {
                "sprint": "sprint",
                "backlog": "backlog",
                "signin": "signin",
                "profile": "profile",
                "*other": "other"
            },
            
            initialize: function () {
                environment.user.on("sync", this.userChange, this);
            },

            other: function () {
                this.navigate("sprint", {trigger: true});
            },

            sprint: function () {
                if (environment.signed()) {
                    var pageView = new PageView({content: SprintView});
                    pageView.render();
                } else {
                    this.navigate("signin", {trigger: true});
                }
            },

            backlog: function () {
                if (environment.signed()) {
                    var pageView = new PageView({content: BacklogView});
                    pageView.render();                
                } else {
                    this.navigate("signin", {trigger: true});
                }
            },

            signin: function () {
                if (environment.signed()) {
                    this.navigate("sprint", {trigger: true});
                } else {
                    var pageView = new PageView({content: LoginView});
                    pageView.render();
                }
            },

            profile: function () {
                if (environment.signed()) {
                    var pageView = new PageView({content: ProfileView});
                    pageView.render();
                } else {
                    this.navigate("signin", {trigger: true});
                }
            },
            
            userChange: function (model, resp, options) {
                if (environment.signed()) {
                    environment.router.navigate("sprint", {trigger: true});
                } else {
                    environment.router.navigate("signin", {trigger: true});
                }
            }
        })
    }
);
