from flask import Flask, request
import base64
import os
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If the user submits an empty part without selecting a file, ignore it
    if file.filename == '':
        return 'No selected file'

    # Process the uploaded file
    file_content = file.read()

    # Convert the file content to base64
    base64_content = base64.b64encode(file_content).decode('utf-8')
