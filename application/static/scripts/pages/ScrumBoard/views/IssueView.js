define(["text!pages/ScrumBoard/html/IssueView.html",
        "css!pages/ScrumBoard/css/IssueView.css",
        "pages/ScrumBoard/views/SubissueView"],

    function(issueHTML, issueCSS, SubissueView) {
        return Backbone.View.extend({
            className: "issue-wrapper",

            template: _.template(issueHTML),

            events: {
                
            },

            initialize: function (options) {
                this.item = options.item;
            },

            render: function () {
                var dragSettings = {
                    revert: "invalid",
                    opacity: 0.75,
                    zIndex: 100,
                    containment: "#wrapper",
                    cursor: "move"
                };
                
                this.$el.html(this.template({"issue": this.item.toJSON()}));

                if ( this.item.get("kind") !== "story" ) {
                    this.$el.draggable(dragSettings);
                }
                this.item.subissues.on("reset", this.draw, this);
                this.item.subissues.fetch({"reset": true, "data": {"issue": this.item.id}});

                return this;
            },

            draw: function (collection, options) {
                collection.each(this.subissue, this);
            },

            subissue: function (subissue) {
                var view = new SubissueView({item: subissue});
                view.render().$el.data('issue', this.$el);

                this.$(".subissue-container").append(view.el);
            }
        });
    }
);
