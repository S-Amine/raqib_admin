import requests
from frappe.utils.file_manager import get_file_path
import frappe
import json
from frappe.utils.file_manager import save_file
import os


def send_image_request(image_file_path, image_id):
    api_settings = frappe.get_doc('Raqib API settings')
    url = api_settings.computer_vision_api_link + "/api/portal/access/car/"
    try:
        local_file_path = get_file_path(image_file_path)
        with open(local_file_path, 'rb') as image_file:
            files = [
            ('image', (image_file.name, image_file, 'image/jpeg'))
            ]
            data = {
                'image_id': image_id
            }
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            print('Request sent successfully!')
            print(response.text)
            return response.text
    except requests.exceptions.RequestException as e:
        print('Error sending request:', e)

def insert_access_image_plat(access_image):
    image_doc = frappe.get_doc('Access Image', access_image)
    request = send_image_request(image_doc.image, access_image)
    response = json.loads(request)
    api_settings = frappe.get_doc('Raqib API settings')
    api_link = api_settings.computer_vision_api_link
    access_doc = frappe.new_doc("Access Image Plat")
    access_doc.name = response[0]["id"]
    access_doc.access_image = access_image
    access_doc.car_number = response[0]["car_number"]
    access_doc.access_image = access_image

    # Download the car number image and save it as an attachment
    file_name = image_doc.name + "_car_number_image.jpg"
    image_path = response[0]["car_number_image"]
    image_link = f"{api_link}{image_path}"
    file_content = requests.get(image_link).content
    saved_file = save_file(file_name, file_content, "Access Image Plat", access_doc.name, df="car_number_image")

    # Update the car_number_image field with the correct attachment name
    access_doc.car_number_image = saved_file.file_url
    access_doc.car_number_image_attachment = saved_file.name
    access_doc.car_number_image_attachment_extension = os.path.splitext(saved_file.file_name)[1]

    access_doc.insert()
