// Copyright (c) 2026, Kishore and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
   refresh(frm) {
      calculate_total(frm)
	},
});

frappe.ui.form.on("Product", {
    price : function(frm, cdt, cdn){
        calculate_total(frm)
    },
    Custmer_remove : function(frm, cdt, cdn){
        calculate_total(frm)
    }
});

function calculate_total(frm){
    let total = 0;

    (frm.doc.purchased_products || []).forEach(row => {
        total += flt(row.item_price)
    });
    frm.set_value('total_payable_amount', total)
}

