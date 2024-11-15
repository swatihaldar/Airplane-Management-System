# Copyright (c) 2024, Swati and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPayment(Document):
    def on_submit(self):
        if not self.amount_paid or self.amount_paid == 0:
            self.payment_status = "Unpaid"
        else:
            self.payment_status = "Paid"
        self.save()


