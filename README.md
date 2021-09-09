# Thingiverse-Downloader

Download and extract a thing from Thingiverse to your Octoprint instance, given a URL to the thing

[![CodeFactor](https://www.codefactor.io/repository/github/appdevelopmentandsuch/thingiverse-downloader/badge)](https://www.codefactor.io/repository/github/appdevelopmentandsuch/thingiverse-downloader)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/appdevelopmentandsuch/Thingiverse-Downloader.svg)](https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/release/appdevelopmentandsuch/Thingiverse-Downloader.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/releases/)
[![GitHub tag](https://img.shields.io/github/tag/appdevelopmentandsuch/Thingiverse-Downloader.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/tags/)
[![Github all releases](https://img.shields.io/github/downloads/appdevelopmentandsuch/Thingiverse-Downloader/total.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/releases/)
[![GitHub stars](https://img.shields.io/github/stars/appdevelopmentandsuch/Thingiverse-Downloader.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/stargazers/)
[![GitHub issues](https://img.shields.io/github/issues/appdevelopmentandsuch/Thingiverse-Downloader.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/appdevelopmentandsuch/Thingiverse-Downloader.svg)](https://GitHub.com/appdevelopmentandsuch/Thingiverse-Downloader/issues?q=is%3Aissue+is%3Aclosed)

![Thingiverse-Downloader-Demo-URL](https://user-images.githubusercontent.com/22528729/132139046-1b1b4dc5-dfb8-4084-bb2d-1d3c27e53bb4.gif)
![Thingiverse-Downloader-Demo-ID](https://user-images.githubusercontent.com/22528729/132139044-446589ee-4ab9-4962-ac1d-04c991062782.gif)

## Setup

### Quick Install

![Thingiverse-Downloader-Install](https://user-images.githubusercontent.com/22528729/131595461-adb80ed1-4f57-4f24-ade5-fa84749ae93a.gif)

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/archive/main.zip

1. Install the [Octoprint-Slic3r](https://plugins.octoprint.org/plugins/slic3r/) plugin in order to view / upload STL files to your Octoprint instance.
2. Install the Thingiverse-Downloader plugin either from the Plugin manager, or manually.
3. Acquire an API key from the Thingiverse Developer Console (tutorial to come).

## Configuration

| Settings           | Description                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| _API Key_          | An API key / App Key acquired from the Thingiverse Developer Console found [here](https://www.thingiverse.com/developers). |
| _Output Directory_ | The desired directory you wish to have the Thingiverse thing downloaded to. Recommend using `models`                       |
