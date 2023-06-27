# Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from .utils import send_image_request, insert_access_image_plat

class AccessImage(Document):
	def after_insert(self):
		frappe.enqueue('raqib_admin.raqib_admin.doctype.access_image.utils.insert_access_image_plat',
						queue='long',
						enqueue_after_commit=True,
						at_front=True,
						access_image=self.name)
