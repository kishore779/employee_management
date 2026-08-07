# Copyright (c) 2026, Kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Attendence(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date | None
		employee: DF.Link | None
		remarks: DF.SmallText | None
		status: DF.Literal["Present", "Leave", "HalfDay"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Attendence"

	def validate(self):
		if frappe.db.exists(
			"Attendence",
			{
				"employee" : self.employee,
				"date" : self.date,
				"name" : ["!=", self.name]
			}
		):
			frappe.throw("Already Marked Attendence")