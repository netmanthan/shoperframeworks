# Copyright (c) 2018, NETMANTHAN and Contributors
# License: MIT. See LICENSE

import frappe


def execute():
	frappe.db.set_value("Currency", "USD", "smallest_currency_fraction_value", "0.01")
