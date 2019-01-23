# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class myPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Cloud Storage! (more: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="https://www.thingiverse.com/")
	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/cloudstorage.js"],
			css=["css/cloudstorage.css"],
			less=["less/cloudstorage.less"]
		)

__plugin_name__ = "Cloud Storage"
__plugin_implementation__ = myPlugin()
