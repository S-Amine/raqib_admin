// Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Access Request", {
	refresh(frm) {
    frappe.after_ajax(() => {
        // Select the div with data-fieldname="car_number" and set max-width to "100% !important"
        const carNumberDiv = document.querySelector('div[data-fieldname="car_number"]');
        if (carNumberDiv) {
            carNumberDiv.style.maxWidth = '100%';
            carNumberDiv.style.width = '100%';
        }
        const car_number_image = document.querySelector('div[data-fieldname="car_number_image"]');
        if (car_number_image) {
            car_number_image.style.maxWidth = '100%';
            car_number_image.style.width = '100%';
        }
    });

    frm.set_df_property('car_number_image', 'description', `<img src="${frm.doc.car_number_image}" style="width: 100%" alt="Image">`);
    frm.refresh_field('car_number_image');
	},
});
