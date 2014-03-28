define(["pages/ScrumBoard/views/HeaderView",
        "pages/ScrumBoard/views/FooterView",],

    function(HeaderView, FooterView) {
        return Backbone.View.extend({       
            el: "body",

            initialize: function(options) {
                this.ContentView = options.content;
            },

            render: function() {               
                var $wrapper = this.$("#wrapper");

                var headerView = new HeaderView();
                headerView.render();

                var contentView = new this.ContentView();
                contentView.render();

                var footerView = new FooterView();
                footerView.render();

                $wrapper
                    .html(headerView.el)
                    .append(contentView.el)
                    .append(footerView.el);
 
                return this;
            }
        });
    }
);
