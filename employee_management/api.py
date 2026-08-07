
import frappe
from frappe.query_builder import DocType

def greet(doc,method):
    frappe.msgprint("Employee Created Successfully!")

def notify(doc, method):
    frappe.msgprint("Leave Applied Successfully")

@frappe.whitelist()
def hr_leave_summary():
    Employee = DocType("Employee")
    LeaveRequest = DocType("Leave Request")


    records = (
        frappe.qb.from_(Employee)
        .right_join(LeaveRequest)
        .on(Employee.name == LeaveRequest.employee)
        .select(
            Employee.name.as_("employee"),
            Employee.first_name,
            Employee.last_name,
            LeaveRequest.name.as_("leave_request"),
            LeaveRequest.status
        )
        .limit(5)
        ).run(as_dict = True)
    if not records:
        return []

    # Document API
    leave_doc = frappe.get_doc(
        "Leave Request",
        records[0]["leave_request"]
    )

    leave_doc.status = "Approved"
    leave_doc.save()

    # Database API
    for row in records:
        frappe.db.set_value(
            "Employee",
            row["employee"],
            "status",
            "Active",
            update_modified=False
        )

    return records
