$(function () {
    function ThingiverseDownloader(parameters) {
        var self = this;

        self.settings = parameters[0];

        self.thingUrl = ko.observable();

        self.loading = ko.observable();

        self.result = ko.observable();

        self.thingUrl.subscribe(function (newValue) {
            if (newValue === "") {
                self.loading(false);
                self.result(null);
            }
        });

        self.onBeforeBinding = function () {
            self.thingUrl("");
            self.loading(false);
            self.result(null);
        };

        self.getResultState = function () {
            let resultStatus = "Download Status: ";
            if (self.result() === true) {
                resultStatus += "<b>Completed</b> &#9989;";
            } else if (self.result() === false) {
                resultStatus += "<b>Failed</b> &#10060;";
            } else if (self.loading() === true) {
                resultStatus += "<b>Downloading...</b>";
            } else if (self.loading() === false) {
                resultStatus += "<b>Not started</b>";
            }

            return resultStatus;
        };

        self.downloadUrlFiles = function () {
            self.loading(true);
            self.result(null);
            $.ajax({
                url: API_BASEURL + "plugin/thingiverse_downloader",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    command: "download",
                    url: self.thingUrl(),
                }),
                contentType: "application/json; charset=UTF-8",
            })
                .then(function ({ result }) {
                    self.loading(false);
                    self.result(result);
                })
                .catch(function () {
                    self.loading(false);
                    self.result(false);
                });
        };
    }

    OCTOPRINT_VIEWMODELS.push([
        ThingiverseDownloader,
        ["settingsViewModel"],
        ["#tab_plugin_thingiverse_downloader"],
    ]);
});
