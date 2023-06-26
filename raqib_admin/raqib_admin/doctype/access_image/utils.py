import requests
from frappe.utils.file_manager import get_file_path

def send_image_request(image_file_path, image_id):
	url = 'http://api.sistemna.site:8002/api/portal/access/car/'

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
