// Copyright (c) 2024, Swati and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport Shop", {
	refresh(frm) {
        display_shop_image(frm)
	},

    tenant(frm){
        if(frm.doc.tenant){
            frm.set_value('status','Occupied');
        } else {
            frm.set_value('status','Available');
        }
    },

    onload(frm) {
        display_shop_image(frm);
    }
});


function display_shop_image(frm) {
    if (frm.doc.shop_image) {
        frm.get_field("image").$wrapper.html(
            `<div style="text-align: center; margin-top: 10px;">
                <img src="${frm.doc.shop_image}" alt="${frm.doc.shop_name}"
                    style="width: 300px; height: 200px; border: 1px solid #ddd; padding: 5px;" />
            </div>`
        );
    }
}