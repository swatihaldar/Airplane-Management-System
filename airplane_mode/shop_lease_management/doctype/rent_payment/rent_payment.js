// Copyright (c) 2024, Swati and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
    refresh(frm) {

    },
    after_save: function(frm) {
        if (frm.doc.payment_status === "Paid") {
            frappe.call({
                method: "frappe.client.set_value",
                args: {
                    doctype: "Lease Contract",
                    name: frm.doc.contract,
                    fieldname: {
                        "payment_status": "Paid"
                    }
                },
                callback: function(response) {
                    if (response && !response.exc) {
                        frappe.msgprint({
                            title: "Payment Successful",
                            message: `Your payment for Contract <b>${frm.doc.contract}</b> has been successfully received.Thank you!`,
                            indicator: "green"
                        });
                    }
                }
            });
        }
    },
});

