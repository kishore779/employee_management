import frappe

def daily_maintenance():
    frappe.log_error(
        title="Daily Maintence",
        message="Daily Maintence executed successfully"
    )