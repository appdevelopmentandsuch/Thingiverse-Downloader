# Thingiverse-Downloader

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/thingiverse-downloader/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/thingiverse-downloader)

Download and extract a thing from Thingiverse to your Octoprint instance, given a URL to the thing

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/archive/main.zip

1. Install the [Octoprint-Slic3r](https://plugins.octoprint.org/plugins/slic3r/) plugin in order to view / upload STL files to your Octoprint instance.
2. Install the Thingiverse-Downloader plugin either from the Plugin manager, or manually.
3. Acquire an API key from the Thingiverse Developer Console (tutorial to come).
4. Set the desired output directory for the downloads, files you can interact with can be found in `~/.octoprint/uploads`, however there is currently an issue using the `~` character, so the absolute directory path should be used for setting output, I use `/home/pi/.octoprint/uploads/models`, where models is the directory I store all my models in.

## Configuration

| Settings | Description |
| API Key | An API key / App Key acquired from the Thingiverse Developer Console found [here](https://www.thingiverse.com/developers).|
| Output Directory | The desired directory you wish to have the Thingiverse thing downloaded to. Recommend using `/home/pi/.octoprint/uploads/models` |
