define(["pages/ScrumBoard/Environment",
        "text!pages/ScrumBoard/html/SprintView.html",
        "css!pages/ScrumBoard/css/SprintView.css",
        "pages/ScrumBoard/collections/Issues",
        "pages/ScrumBoard/views/IssueView",
        "pages/ScrumBoard/views/FilterView"],

    function(environment, sprintHTML, sprintCSS, Issues, IssueView, FilterView) {
        return Backbone.View.extend({
            id: "sprint",

            template: _.template(sprintHTML),

            events: {
                
            },

            initialize: function(options) {
                environment.issues = new Issues();
            },

            render: function () {
                this.$el.html(this.template());
                this.makeColumnsDroppable();

                var filter = new FilterView();
                filter.render();
                this.$("#filter-container").append(filter.el);

                environment.issues.on("reset", this.draw, this);
                environment.issues.fetch({"reset": true});

                return this;
            },
            
            draw: function (collection, options) {
                collection.each(this.issue, this);
            },

            makeColumnsDroppable: function() {
                var onColumnDrop = function (event, ui) {
                    if ( ui.draggable.hasClass("issue-wrapper") ) {
                        ui.draggable
                            .appendTo($(this))
                            .css({"top" : 0, "left" : 0});
                    } else if ( ui.draggable.hasClass("subissue-wrapper") ) {
                        var parentId = ui.draggable.find(".subissue").data("parent");
                        var issueWrapper = $(this).find(".subissue-container")
                            .filter(function() {
                                return $(this).data("issue-id") == parentId;
                        });
                        if ( !issueWrapper.size() ) {
                            issueWrapper = $("<div>");
                            issueWrapper.append("<div class='container'>container</p>");
                            issueWrapper.attr('data-issue-id');
                            issueWrapper.addClass("subissue-container").data("issue-id", parentId).appendTo($(this));
                        }
                        ui.draggable.appendTo($(issueWrapper)).css({"top" : 0, "left" : 0});
                    }
                } 
                this.$(".column").droppable({
                    drop: onColumnDrop
                });
            },
            
            issue: function (issue) {
                var view = new IssueView({item: issue});
                view.render();
                
                var selector = ".todo";
                if (issue.get("status") == "doing") {
                    selector = ".doing";
                } else if (issue.get("status") == "done") {
                    selector = ".done";
                }
                
                this.$(selector).append(view.el);
            },

            equalColumns: function (selector) {
                var tallestColumn = 0;
                $(selector).height('100%');
                _.each($(selector), function(column) {
                    var $currentHeight = $(column).height();
                    if ($currentHeight > tallestColumn) {
                        tallestColumn = $currentHeight;
                    }
                });
                $(selector).height(tallestColumn + 50);
            }
        });    
    }
);
