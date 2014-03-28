define(["text!pages/ScrumBoard/html/FooterView.html",
        "css!pages/ScrumBoard/css/FooterView.css"],

    function(footerHTML, footerCSS) {
        return Backbone.View.extend({
            id: "footer",

            template: _.template(footerHTML),

            render: function() {
                this.$el.html(this.template());
 
                return this;
            }
        });    
    }
);
