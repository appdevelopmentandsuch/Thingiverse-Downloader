$(function () {
    function ThingiverseDownloader(parameters) {
        var self = this;

        const ENDPOINT_THINGIVERSE_DOWNLOADER_PLUGIN =
            "plugin/thingiverse_downloader";

        const EMPTY_PREVIEW = { name: null, url: null };

        self.callPlugin = function (data) {
            return {
                url: `${API_BASEURL}${ENDPOINT_THINGIVERSE_DOWNLOADER_PLUGIN}`,
                type: "POST",
                dataType: "json",
                data,
                contentType: "application/json; charset=UTF-8",
            };
        };

        self.settings = parameters[0];

        self.thingUrl = ko.observable("");

        self.loading = ko.observable(false);

        self.result = ko.observable(null);

        self.previewData = ko.observable(EMPTY_PREVIEW);

        self.thingUrl.subscribe(function () {
            self.fetchPreviewImage();
            self.result(null);
        });

        self.clearThingUrl = function () {
            self.thingUrl("");
        };

        self.fetchPreviewImage = function () {
            $.ajax(
                self.callPlugin(
                    JSON.stringify({
                        command: "preview",
                        url: self.thingUrl(),
                    })
                )
            )
                .then(function ({ result, error }) {
                    if (error == undefined) {
                        self.previewData(result);
                    } else {
                        self.previewData(EMPTY_PREVIEW);
                    }
                })
                .catch(function () {
                    self.previewData(EMPTY_PREVIEW);
                });
        };

        self.downloadUrlFiles = function () {
            self.loading(true);
            self.result(null);
            $.ajax(
                self.callPlugin(
                    JSON.stringify({
                        command: "download",
                        url: self.thingUrl(),
                    })
                )
            )
                .then(function ({ result }) {
                    self.loading(false);
                    self.result(result);
                })
                .catch(function () {
                    self.loading(false);
                    self.result(false);
                });
        };

        self.downloadButtonClass = function () {
            let className = "btn-primary";
            if (self.result() === true) {
                className = "btn-success";
            } else if (self.result() === false) {
                className = "btn-danger";
            }
            return className;
        };

        self.downloadStateIcon = function () {
            let icon = "";
            if (self.result() === true) {
                icon =
                    "fas fa-check-square thingiverse-downloader-result-success";
            } else if (self.result() === false) {
                icon =
                    "fas fa-exclamation-triangle thingiverse-downloader-result-failed";
            } else if (self.loading() === true) {
                icon = "fas fa-spinner fa-spin";
            } else if (self.loading() === false) {
                icon = "fas fa-download";
            }
            return icon;
        };
    }

    OCTOPRINT_VIEWMODELS.push([
        ThingiverseDownloader,
        ["settingsViewModel"],
        ["#tab_plugin_thingiverse_downloader"],
    ]);
});
