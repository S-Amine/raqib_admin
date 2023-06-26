# Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json
from .utils import send_image_request

class AccessImage(Document):
	def after_insert(self):
		response = json.loads(send_image_request(self.image, self.name))
		access_doc = frappe.new_doc("Access Image Plat")
		access_doc.name = response[0]["id"]
		access_doc.access_image = self.name
		access_doc.car_number = response[0]["car_number"]
		access_doc.car_number_image = "http://api.sistemna.site:8002{}".format(response[0]["car_number_image"])
		access_doc.image = self.name
		access_doc.insert()
		access_doc.notify_update()
