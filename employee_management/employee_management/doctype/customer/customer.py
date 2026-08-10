# Copyright (c) 2026, Kishore and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from employee_management.employee_management.doctype.product.product import Product
		from frappe.types import DF

		email: DF.Data | None
		mobile_number: DF.Phone | None
		name1: DF.Data | None
		purchased_products: DF.Table[Product]
		total_payable_amount: DF.Currency
	# end: auto-generated types

	_DOCTYPE_NAME = "Customer"
