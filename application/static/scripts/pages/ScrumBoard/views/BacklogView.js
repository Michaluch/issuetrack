define(["text!pages/ScrumBoard/html/BacklogView.html",
        "css!pages/ScrumBoard/css/BacklogView.css",
        "pages/ScrumBoard/collections/Issues",
        "pages/ScrumBoard/views/FilterView"],

    function(backlogHTML, backlogCSS, Issues, FilterView) {
        return Backbone.View.extend({
            id: "backlog",

            template: _.template(backlogHTML),

            initialize: function(options) {
                this.issues = new Issues();
            },

            render: function () {
                this.$el.html(this.template());

                var filter = new FilterView();
                filter.render();
                this.$("#filter-container").append(filter.el);

                this.issues.fetch({"reset": true});

                return this;
            }
        });    
    }
);
