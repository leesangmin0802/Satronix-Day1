from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['file']
    image.save(os.path.join(UPLOAD_FOLDER, 'latest.png'))
    return 'Upload successful.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)