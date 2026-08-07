# Copyright (c) 2026, Kishore and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate, today
from frappe.model.document import Document


class Employee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_of_birth: DF.Date | None
		department: DF.Link | None
		email: DF.Data | None
		employee_id: DF.Data | None
		first_name: DF.Data | None
		joining_date: DF.Date | None
		last_name: DF.Data | None
		phone: DF.Phone | None
		photo: DF.Attach | None
		salary: DF.Currency
		status: DF.Literal["Active", "Inactive", "Resigned"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Employee"

	@property
	def full_name(self):
		first = self.first_name or ""
		second = self.last_name or ""
		return f'{first}{second}'

	def validate(self):
		if getdate(self.joining_date) > getdate(today()):
			frappe.throw("Joining date cannot be in future")

		if self.salary <= 0:
			frappe.throw("Salary must be in positive")

		if frappe.db.exists(
			"Employee",
			{
				"email" : self.email,
				"name" : ["!=", self.name]
			}
		): frappe.throw("Email already exists")