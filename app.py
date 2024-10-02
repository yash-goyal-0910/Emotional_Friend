import os
import json
import random
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)

# Load the pre-trained model
model = load_model('cnn_emotion_detection.h5')

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load comments from the JSON file
def load_comments():
    with open('comments.json', 'r') as file:
        return json.load(file)

# Get a random comment based on the emotion
def get_random_comment(emotion):
    comments = load_comments()
    if emotion in comments:
        return random.choice(comments[emotion])
    else:
        return "No comment available."

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        img = Image.open(file.stream).convert("L")  # Convert image to grayscale
        img = img.resize((48, 48))  # Resize to match the model's input size
        img_array = np.array(img).reshape(1, 48, 48, 1) / 255.0  # Preprocess image

        # Predict emotion using the model
        prediction = model.predict(img_array)
        emotion_index = np.argmax(prediction[0])
        emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        emotion = emotions[emotion_index]

        # Get a random comment for the detected emotion
        comment = get_random_comment(emotion)

        # Redirect to the result page with the detected emotion and random comment
        return redirect(url_for('show_result', emotion=emotion, comment=comment))

# Route to handle webcam prediction
@app.route('/predict_webcam', methods=['POST'])
def predict_webcam():
    image_data = request.form['capturedImageData']
    image_data = image_data.split(',')[1]  # Remove data URL prefix
    img = Image.open(BytesIO(base64.b64decode(image_data))).convert('L')  # Convert to grayscale
    img = img.resize((48, 48))  # Resize to match the model's input size
    img_array = np.array(img).reshape(1, 48, 48, 1) / 255.0  # Preprocess image

    # Predict emotion using the model
    prediction = model.predict(img_array)
    emotion_index = np.argmax(prediction[0])
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    emotion = emotions[emotion_index]

    # Get a random comment for the detected emotion
    comment = get_random_comment(emotion)

    # Redirect to the result page with the detected emotion and random comment
    return redirect(url_for('show_result', emotion=emotion, comment=comment))

# Route to display the result
@app.route('/result')
def show_result():
    emotion = request.args.get('emotion')
    comment = request.args.get('comment')
    return render_template('result.html', emotion=emotion, comment=comment)


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
