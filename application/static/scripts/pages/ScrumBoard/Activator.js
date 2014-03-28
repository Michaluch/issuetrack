// config requirejs

require.config({
    urlArgs: "bust=" + (new Date()).getTime(),  // never delete this
    baseUrl: "/static/scripts",
    paths: {
        text: "libs/requirejs/text",
        css: "libs/requirejs/css"
    }
}); 

require(["pages/ScrumBoard/Application"],

    function (application) {
        application.start();
    }
);
