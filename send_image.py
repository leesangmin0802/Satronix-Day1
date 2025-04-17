# send_image.py
import requests

def send_image(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        r = requests.post('http://your-server.com/upload', files=files)
        print(r.text)

send_image("sat_1680000000.png")
