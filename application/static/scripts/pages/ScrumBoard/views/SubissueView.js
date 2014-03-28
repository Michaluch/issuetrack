define(["text!pages/ScrumBoard/html/SubissueView.html",
        "css!pages/ScrumBoard/css/SubissueView.css"],

    function(subissueHTML, subissueCSS) {
        return Backbone.View.extend({
            className: "subissue-wrapper",

            template: _.template(subissueHTML),

            events: {
                
            },
            
            dragSettings: {
                revert: "invalid",
                opacity: 0.75,
                zIndex: 100,
                containment: "#wrapper",
                cursor: "move"
            },

            initialize: function (options) {
                this.item = options.item;
            },

            render: function () {
                this.$el.html(this.template(/*{
                    _id: this.item.id,
                    name: this.item.get("name"),
                    description: this.item.get("description")
                }*/
                this.item.toJSON()));
                
                this.$el.draggable(this.dragSettings);

                return this;
            }
        });
    }
);
