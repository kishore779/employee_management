# Copyright (c) 2026, Kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaveRequest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		employee: DF.Link | None
		from_date: DF.Date | None
		leave_type: DF.Literal["Paid", "Not-Paid"]
		reason: DF.SmallText | None
		status: DF.Literal["Pending", "Approved", "Rejected"]
		to_date: DF.Date | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Leave Request"

	def validate(self):
		if self.to_date > self.from_date:
			frappe.throw("Leave must be Atleast 1 day")
