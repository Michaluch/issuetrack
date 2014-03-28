define([],

    function () {
        return {
            name: "Issue Tracker",

            signed: function () {
                return this.user.get("email") ? true : false;
            }
        }
    }
);
