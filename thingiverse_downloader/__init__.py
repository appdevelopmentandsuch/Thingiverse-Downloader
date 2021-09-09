# coding=utf-8
from __future__ import absolute_import
import requests
import flask
import os
import errno
import octoprint.plugin
import octoprint.settings


class ThingiverseDownloaderPlugin(octoprint.plugin.TemplatePlugin,
                                  octoprint.plugin.AssetPlugin,
                                  octoprint.plugin.SimpleApiPlugin,
                                  octoprint.plugin.SettingsPlugin):
    BASE_URL = "https://api.thingiverse.com/things"

    def get_settings_defaults(self):
        return {"api_key": None, "output_directory": "models"}

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
            download=["url", "override_name"], preview=["url"]
        )

    def return_response(self, result, error=None):
        return flask.jsonify({"result": result, "error": error}) if error else flask.jsonify({"result": result})

    def get_access_token_parameter(self, ACCESS_TOKEN):
        return "?access_token={0}".format(ACCESS_TOKEN)

    def get_thing_id_url(self, THING_ID, ACCESS_TOKEN):
        param_access_token = self.get_access_token_parameter(ACCESS_TOKEN)
        return "{0}/{1}/{2}".format(self.BASE_URL, THING_ID,
                                    param_access_token)

    def get_thing_id(self, thing_url):
        thing_id = ''

        for char in thing_url:
            if char.isdigit():
                thing_id += char
            elif char.isdigit() is False and len(thing_id) > 0:
                break

        return thing_id

    def get_thing_from_thingiverse(self, thing_id, access_token):
        thing_id_url = self.get_thing_id_url(thing_id, access_token)
        r = requests.get(url=thing_id_url)
        return r.json()

    def get_thing_download_files(self, thing_id, access_token):
        param_access_token = self.get_access_token_parameter(access_token)
        files_url = "{0}/{1}/files/{2}".format(self.BASE_URL, thing_id,
                                               param_access_token)

        r = requests.get(url=files_url)

        return r.json()

    def on_api_command(self, command, data):
        response = False
        try:
            ACCESS_TOKEN = self._settings.get(["api_key"])

            if ACCESS_TOKEN is None:
                raise Exception("API Key not set.")

            PARAM_ACCESS_TOKEN = self.get_access_token_parameter(ACCESS_TOKEN)

            thing_url = data.get("url", None)

            if thing_url is None or thing_url == "":
                raise Exception(
                    "A Thingiverse URL / Thing ID was not supplied.")

            thing_id = self.get_thing_id(thing_url)

            if not thing_id.isnumeric():
                raise Exception("A Thing ID could not be parsed.")

            thing = self.get_thing_from_thingiverse(thing_id, ACCESS_TOKEN)

            if command == "download":
                override_name = data.get("override_name", "")

                name = override_name if override_name != "" else thing.get(
                    'name', '')
                name = name.encode(
                    'ascii', 'ignore').decode("utf-8")  # Remove filename unsafe characters

                if name == '':
                    raise Exception(
                        "A name could not be parsed from the Thingiverse item.")

                thing_files = self.get_thing_download_files(
                    thing_id, ACCESS_TOKEN)

                uploads_dir = octoprint.settings.Settings().getBaseFolder("uploads")

                OUTPUT_DIRECTORY = "{0}/{1}".format(uploads_dir, self._settings.get(
                    ["output_directory"]).rstrip('/'))

                for thing_file in thing_files:
                    thing_file_download_url = thing_file.get(
                        "download_url", None)

                    if thing_file_download_url is None:
                        raise Exception(
                            "Could not find download url for thing {0}".format(name))

                    download_url = "{0}{1}".format(
                        thing_file_download_url, PARAM_ACCESS_TOKEN)

                    r = requests.get(url=download_url)

                    path = "{0}/{1}".format(OUTPUT_DIRECTORY, name)
                    thing_file_name = thing_file.get("name", None)

                    if thing_file_name is None:
                        raise Exception(
                            "Could not determine file part name while downloading {0}".format(name))

                    filename = "{0}/{1}".format(path, thing_file_name)

                    try:
                        os.makedirs(path)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise Exception(
                                "An error occurred while creating the model directory.")

                    open(filename, 'wb').write(r.content)

                response = True
            elif command == "preview":
                response = {'url': thing.get(
                    "thumbnail", ""), 'name': thing.get("name")}
            else:
                raise Exception("Invalid command provided")
        except Exception as e:
            return self.return_response(False, str(e))

        return self.return_response(response)


__plugin_name__ = "Thingiverse Downloader"
__plugin_version__ = "0.3.0"
__plugin_description__ = "Download and extract a thing from Thingiverse to your Octoprint instance, given a URL to the thing"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_implementation__ = ThingiverseDownloaderPlugin()
