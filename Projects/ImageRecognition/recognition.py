from flask import Flask, request, jsonify
from requests_html import HTMLSession
from flask_cors import CORS
import torch
from torchvision import models, transforms
from PIL import Image



appRecognition = Flask(__name__)
CORS(appRecognition)
@appRecognition.route('/image_recognition', methods=['GET','POST'])
def image_recognition ():

    alexnet = models.alexnet(pretrained=True)    

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    img = request.files['image']
    img = Image.open(img)

    input_image = preprocess(img)
    alexnet.eval()
    output = alexnet(input_image.unsqueeze(0))

    with open('/home/austinmarquis30/a-marquis30.github.io/Projects/ImageRecognition/imagenet_classes.txt') as f:
        labels = [line.strip() for line in f.readlines()]

    _, predicted_idx = torch.max(output, 1)
    predicted_label = labels[predicted_idx.item()]

    return jsonify({'predicted_label': predicted_label})

if __name__ == '__main__':
    appRecognition.run(debug=True)
