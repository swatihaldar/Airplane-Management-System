# Copyright (c) 2024, Swati and contributors
# For license information, please see license.txt
     
import frappe
from frappe.model.document import Document
import random 


class AirplaneTicket(Document):
    def validate(self):
        total_amount = self.flight_price
        seen_addOns = set()

        for add in self.add_ons:
            if add.item in seen_addOns:
                frappe.throw(f"Add-on {add.item} is added more than once. Each add-on must be unique.")

            seen_addOns.add(add.item)
            total_amount += add.amount

        self.total_amount = total_amount

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("You cannot submit the Airplane Ticket unless the status is 'Boarded'.")

    def before_insert(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat = f"{random_number}{random_letter}"

    
    def on_update(self):
        self.airplane_capacity()

    def airplane_capacity(self):
        if self.flight:
            ticket_count = frappe.db.count(
                'Airplane Ticket',
                filters={
                    'fligth': self.flight,
                    'name':('!=',self.name)
                }
            )

            flight = frappe.get_doc('Airplane Flight', self.flight)
            if flight:
                airplane = frappe.get_doc('Airplane', flight.airplane)

                if ticket_count >= airplane.capacity:
                    frappe.throw(f'Number of tickets exceeds airplane capacity of {airplane.capacity}. Cannot create more Airplane Tickets.')