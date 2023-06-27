# Copyright (c) 2023, saidi.amine.p@gmail.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RaqibAPIsettings(Document):
	def on_update(self):
		if self.computer_vision_api_link.endswith("/"):
			self.computer_vision_api_link = self.computer_vision_api_link[:-1]
			self.save()
