# coding=utf-8
from __future__ import absolute_import
import requests
import flask
import os
import octoprint.plugin


class ThingiverseDownloaderPlugin(octoprint.plugin.TemplatePlugin,
                                  octoprint.plugin.AssetPlugin,
                                  octoprint.plugin.SimpleApiPlugin,
                                  octoprint.plugin.SettingsPlugin):
    def get_settings_defaults(self):
        return {"api_key": None, "output_directory": "/home/pi/.octoprint/uploads/models"}

    def get_assets(self):
        return dict(
            js=["js/thingiverse_downloader.js"],
            css=["css/thingiverse_downloader.css"]
        )

    def get_template_configs(self):
        return [
            dict(type="tab", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_api_commands(self):
        return dict(
            download=["url"]
        )

    def return_response(self, result, error=None):
        return flask.jsonify({"result": result, "error": error}) if error else flask.jsonify({"result": result})

    def on_api_command(self, command, data):
        result = False
        if command == "download":
            SEPERATOR = "https://www.thingiverse.com/thing:"
            BASE_URL = "https://api.thingiverse.com/things"

            ACCESS_TOKEN = self._settings.get(["api_key"])

            if ACCESS_TOKEN is None:
                return self.return_response(result, "API Key not set.")

            PARAM_ACCESS_TOKEN = "?access_token={0}".format(ACCESS_TOKEN)

            THING_URL = data.get("url", None)

            if THING_URL is None:
                return self.return_response(result, "A Thingiverse URL was not supplied.")

            THING_ID = THING_URL.partition(SEPERATOR)[2]

            OUTPUT_DIRECTORY = "{0}".format(self._settings.get(
                ["output_directory"]).rstrip('/'))

            URL = "{0}/{1}/{2}".format(BASE_URL, THING_ID,
                                       PARAM_ACCESS_TOKEN)

            r = requests.get(url=URL)

            name = r.json().get('name', None)

            if name is None:
                return self.return_response(result, "A name could not be parsed from the Thingiverse item.")

            FILES_URL = "{0}/{1}/files/{2}".format(BASE_URL, THING_ID,
                                                   PARAM_ACCESS_TOKEN)

            r = requests.get(url=FILES_URL)

            data = r.json()

            for item in data:
                DOWNLOAD_URL = "{0}{1}".format(
                    item["download_url"], PARAM_ACCESS_TOKEN)

                r = requests.get(DOWNLOAD_URL)

                path = "{0}/{1}".format(OUTPUT_DIRECTORY, name)
                filename = "{0}/{1}".format(path, item["name"])

                try:
                    os.makedirs(path)
                except OSError:
                    if not os.path.isdir(path):
                        return self.return_response(result, "An error occurred while creating the model directory.")

                open(filename, 'wb').write(r.content)

            result = True
            return self.return_response(result)


__plugin_name__ = "Thingiverse Downloader"
__plugin_version__ = "0.0.0"
__plugin_description__ = "Download and extract a thing from Thingiverse to your Octoprint instance, given a URL to the thing"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = ThingiverseDownloaderPlugin()
