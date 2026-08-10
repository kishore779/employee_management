# Copyright (c) 2026, Kishore and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Singlee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attach_uxcr: DF.Attach | None
		present: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Singlee"
