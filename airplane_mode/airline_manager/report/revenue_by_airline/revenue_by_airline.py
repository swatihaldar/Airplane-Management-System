# Copyright (c) 2024, Swati and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    total_revenue = calculate_total_revenue(data)
    data_list = [list(row) for row in data]
    chart = get_chart(data_list, total_revenue)
    report_summary = get_report_summary(total_revenue)
    
    return columns, data_list, total_revenue, chart, report_summary


def get_data(filters):
    airlines = frappe.get_all('Airline', fields=['name'])
    data = []
    
    for airline in airlines:
        tickets = frappe.get_all(
            'Airplane Ticket',
            filters={"flight": ["like", f"{airline['name']}-%"]},
            fields = ['total_amount']
		)
        
        total_revenue = 0
        for ticket in tickets:
            total_revenue += ticket.total_amount 
        
        data.append((airline['name'] or 'Other', total_revenue))
        
        
    data.sort(key=lambda x:x[1], reverse=True)
    return data
    

def calculate_total_revenue(data):
    total_revenue = 0
    for d in data:
        total_revenue += d[1]
    return total_revenue 

    # return sum(d[1] for d in data)
    
def get_chart(data, total_revenue):
    return {
        'data': {
            'labels': [d[0] for d in data],
            'datasets':[{
                'name':'Revenue',
                'values':[d[1] for d in data]
			}]
		},
        'type':'donut',
	}


def get_report_summary(total_revenue):
    return [{
        'value': total_revenue,
        'indicator': 'Green' if total_revenue > 0 else 'Red',
        'label':'Total Revenue',
        'datatype':'Currency',
        'currency':'INR'
	}]


def get_columns():
    return [
        {'label': 'Airline', 'fieldname':'airline', 'fieldtype':'Link','options':'Airline','width':200},
        {'label':'Revenue', 'fieldname':'revenue', 'fieldtype':'Currency','width':200}
	]


