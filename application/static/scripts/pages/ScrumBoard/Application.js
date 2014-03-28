define(["pages/ScrumBoard/Environment",
        "pages/ScrumBoard/routers/PageRouter",
        "pages/ScrumBoard/models/User"],

    function(environment, PageRouter, User) {
        var _public = {};
        var _private = {};

        _private.init = function () {
            environment.user = new User();
            environment.router = new PageRouter();

            environment.user.url = function () {
                return environment.user.id ? '/api/user/' + environment.user.id + '/' : '/api/user/current/';
            };
            environment.user.fetch({async: false});
        };

        _public.start = function () {
            _private.init();
            Backbone.history.start();
        };

        return _public;
    }
);
