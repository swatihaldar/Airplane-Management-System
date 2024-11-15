# # Copyright (c) 2024, Swati and contributors
# # For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):

    columns = [
        {"fieldname": "airport", "label": _("Airport"), "fieldtype": "Data", "width": 150},
        {"fieldname": "available_shops", "label": _("Available Shops"), "fieldtype": "Int", "width": 150},
        {"fieldname": "occupied_shops", "label": _("Occupied Shops"), "fieldtype": "Int", "width": 150},
        {"fieldname": "total_shops", "label": _("Total Shops"), "fieldtype": "Int", "width": 150},
    ]
    
    data = []
    airports = frappe.get_all("Airport Shop", fields=["airport"], distinct=True)
    
    for airport in airports:
        total_count = frappe.db.count("Airport Shop", {
            "airport": airport["airport"]
        })
        
        available_count = frappe.db.count("Airport Shop", {
            "airport": airport["airport"],
            "status": "Available"
        })
        
        occupied_count = frappe.db.count("Airport Shop", {
            "airport": airport["airport"],
            "status": "Occupied"
        })
        
        data.append({
            "airport": airport["airport"],
            "total_shops": total_count,
            "available_shops": available_count,
            "occupied_shops": occupied_count
        })
    
    chart = {
        "data": {
            "labels": [d["airport"] for d in data],
            "datasets": [
                {"name": _("Available Shops"), "values": [d["available_shops"] for d in data]},
                {"name": _("Occupied Shops"), "values": [d["occupied_shops"] for d in data]}
            ]
        },
        "type": "bar", 
        "colors": ["#34c38f", "#f46a6a"], 
        "fieldtype": "Int"
    }
    
    return columns, data, None, chart
