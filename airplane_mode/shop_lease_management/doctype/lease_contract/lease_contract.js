// Copyright (c) 2024, Swati and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lease Contract", {
	refresh(frm) {
        check_contract_status(frm);
	},

    onload(frm){
        check_contract_status(frm);
    },

    contract_end_date(frm){
        check_contract_status(frm);
    },

    onload: function(frm) {
        if (!frm.doc.rent_amount) {
            frappe.db.get_single_value('Shop Lease Settings', 'default_rent_amount')
                .then((default_rent_amount) => {
                    frm.set_value('rent_amount', default_rent_amount);
                    // frappe.msgprint(`Rent amount set to default value: ${default_rent_amount}`);
                });
        }
    }
});


function check_contract_status(frm){
    let today = frappe.datetime.get_today();
    let contract_end_date = frm.doc.contract_end_date;

    if(contract_end_date && contract_end_date < today){
        frm.set_value('status', 'Expired');
    }
    else if(contract_end_date && contract_end_date >= today){
        frm.set_value('status', 'Active')
    }
}




