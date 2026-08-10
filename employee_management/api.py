
import frappe
from frappe.query_builder import DocType
from frappe.utils import now

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

@frappe.whitelist()
def get_todo():
    tasks = frappe.get_list("ToDo",
                   fields = ["name", "description", "owner"])

    results = []
    for task in tasks:
        owner = task.get("owner")
        email = frappe.db.get_value("User",
                                    owner,
                                    "email")

        if owner:
            results.append({
                "name" : task.name,
                "description" : task.description,
                "email" : email
            })

    return {
        "timestamp" : frappe.utils.now(),
        "results" : results
    }