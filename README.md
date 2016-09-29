# Overthere Smb Converter plugin #

This document describes the functionality provided by the XLD Overthere Smb Converter plugin.

See the **XL Deploy Reference Manual** for background information on XL Deploy and deployment concepts.

# Overview #

##Features##

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
