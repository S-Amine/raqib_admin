// Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Access Image Plat", {
    refresh: function(frm) {
        // Check if the image field is set
        if (frm.doc.access_image) {
            // Set the image source when the form is refreshed
            frappe.model.with_doc("Access Image", frm.doc.access_image, function() {
                var access_image = frappe.model.get_doc("Access Image", frm.doc.access_image);
                var image_url = access_image.image;

                frm.set_df_property('car_number_image', 'label', 'Car Number Image');
                frm.set_df_property('car_number_image', 'description', `<img src="${frm.doc.car_number_image}" style="width: 100%" alt="Image">`);
                frm.refresh_field('car_number_image');

                frm.set_df_property('access_image', 'label', 'Acess image');
                frm.set_df_property('access_image', 'description', `<img src="${image_url}" style="width: 100%" alt="Image">`);
                frm.refresh_field('access_image');
            });
        }
    }
});
