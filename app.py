from gradio_client import Client
import requests
# from PIL import Image
from io import BytesIO
import base64
from flask import Flask, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# base_url = os.getenv('URL_IMAGE_GENERATE')
base_url = os.environ.get('URL_IMAGE_GENERATE')

def generate_image(query):
    # Gradio client configuration
    client = Client(base_url)

    # Generate an image using Gradio
    result = client.predict(query, api_name="/predict")

    b64_string = ''

    with open(result, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())

    return b64_string

@app.route('/, methods=['get'])
def upload_image():
    return "server is working fine"


@app.route('/generate_image, methods=['get'])
def upload_image():
    query = request.args.get('query')

    if not query:
        return jsonify({"error": "Missing 'query' parameter."}), 400

    b64_string = generate_image(query)
    return b64_string

if __name__ == '__main__':
    app.run()
