# Copyright (c) 2021, NETMANTHAN and Contributors
# License: MIT. See LICENSE

from click import secho

import frappe


def execute():
	if frappe.get_hooks("jenv"):
		print()
		secho(
			'WARNING: The hook "jenv" is deprecated. Follow the migration guide to use the new "jinja" hook.',
			fg="yellow",
		)
		secho("https://github.com/netmanthan/shoperframeworks/wiki/Migrating-to-Version-13", fg="yellow")
		print()
