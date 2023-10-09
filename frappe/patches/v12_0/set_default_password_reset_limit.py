# Copyright (c) 2015, NETMANTHAN and Contributors
# License: MIT. See LICENSE

import frappe


def execute():
	frappe.reload_doc("core", "doctype", "system_settings", force=1)
	frappe.db.set_single_value("System Settings", "password_reset_limit", 3)
