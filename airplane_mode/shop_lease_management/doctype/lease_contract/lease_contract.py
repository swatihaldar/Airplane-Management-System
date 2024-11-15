# Copyright (c) 2024, Swati and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaseContract(Document):
	def validate(self):
		if not self.rent_amount:
			self.rent_amount = frappe.db.get_single_value('Shop Lease Settings', 'default_rent_amount')

