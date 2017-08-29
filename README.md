# Overthere Smb Converter plugin #

This document describes the functionality provided by the XLD Overthere Smb Converter plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# CI status #

[![Build Status][xld-overthere-smb-converter-plugin-travis-image]][xld-overthere-smb-converter-plugin-travis-url]
[![Codacy Badge][xld-overthere-smb-converter-plugin-codacy-image] ][xld-overthere-smb-converter-plugin-codacy-url]
[![Code Climate][xld-overthere-smb-converter-plugin-code-climate-image] ][xld-overthere-smb-converter-plugin-code-climate-url]
[![License: MIT][xld-overthere-smb-converter-plugin-license-image] ][xld-overthere-smb-converter-plugin-license-url]
[![Github All Releases][xld-overthere-smb-converter-plugin-downloads-image] ]()


[xld-overthere-smb-converter-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-overthere-smb-converter-plugin.svg?branch=master
[xld-overthere-smb-converter-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-overthere-smb-converter-plugin
[xld-overthere-smb-converter-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/da40fbbd28b349d4866556b2a7833184
[xld-overthere-smb-converter-plugin-codacy-url]: https://www.codacy.com/app/joris-dewinne/xld-overthere-smb-converter-plugin
[xld-overthere-smb-converter-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xld-overthere-smb-converter-plugin/badges/gpa.svg
[xld-overthere-smb-converter-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xld-overthere-smb-converter-plugin
[xld-overthere-smb-converter-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-overthere-smb-converter-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-overthere-smb-converter-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-overthere-smb-converter-plugin/total.svg


# Overview #

## Features ##

* Convert **overthere.AliasCifsHost** to **overthere.AliasSmbHost**
* Convert **overthere.CifsHost** to **overthere.SmbHost**
* Convert **overthere.AliasSmbHost** to **overthere.AliasCifsHost**
* Convert **overthere.SmbHost** to **overthere.SmbHost**

# Requirements #

* **XL Deploy requirements**
	* **XL Deploy**: version 5.x+
	* **XL Deploy** patch to support SMB (not released yet)
	* [xld-credential-on-host-plugin](https://github.com/xebialabs-community/xld-credential-on-host-plugin) branch: "smb"

# Installation

Place the plugin jar or xldp into your `XL_DEPLOY_SERVER_HOME/plugins` directory.

# Usage #

Right click on a host you want to convert and select 'Convert to Smb' or 'Convert to Cifs', then click Execute. Based on the current type, the new type is calculated. Also the property of the port will be copied.

# Known limitations #

* None
