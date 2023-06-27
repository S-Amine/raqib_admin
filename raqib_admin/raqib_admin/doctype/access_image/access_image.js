// Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Access Image", {
	refresh(frm) {
    frm.set_df_property('image', 'label', 'Image');
    frm.set_df_property('image', 'description', `<img src="${frm.doc.image}" style="width: 100%" alt="Image">`);
    frm.refresh_field('image');
	},
});
