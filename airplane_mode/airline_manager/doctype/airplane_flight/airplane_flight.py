# Copyright (c) 2024, Swati and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def before_submit(self):
        if self.status == "Scheduled":
            self.status = "Completed"
        else:
            frappe.throw("Cannot change status after submission")