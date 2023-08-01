import requests
from frappe.utils.file_manager import get_file_path
import frappe
import json
from frappe.utils.file_manager import save_file
import os


def create_access_request(access_image):
    plat_image_doc = frappe.get_doc('Access Image Plat', access_image)
    access_request = frappe.new_doc("Access Request")
    access_request.image_plat_id = plat_image_doc
    access_request.access_type = "in"
    access_request.insert()
