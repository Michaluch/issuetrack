define(["pages/ScrumBoard/Environment",
        "text!pages/ScrumBoard/html/FilterView.html",
        "css!pages/ScrumBoard/css/FilterView.css"],

    function(environment, filterHTML, filterCSS) {
        return Backbone.View.extend({
            id: "filter",

            template: _.template(filterHTML),

            events: {
                "click .goto-sprint": "sprint",
                "click .goto-backlog": "backlog"
            },

            initialize: function (options) {
                
            },

            render: function () {
                this.$el.html(this.template());

                return this;
            },

            sprint: function (event) {
                environment.router.navigate("sprint", {trigger: true});
            },

            backlog: function (event) {
                environment.router.navigate("backlog", {trigger: true});
            }
        });
    }
);
