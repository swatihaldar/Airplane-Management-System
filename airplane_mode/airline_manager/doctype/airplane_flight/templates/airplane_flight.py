import frappe

def get_context(context):
    context.flights_name = frappe.get_all("Airplane", fields = ['name'])
