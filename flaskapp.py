from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("signSight_model.h5")  # Make sure this file is in your repo

@app.route('/')
def home():
    return "SignSight API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Example: convert input to numpy array
    input_array = np.array(data["input"]).reshape(1, -1)  # Adjust shape as needed
    
    prediction = model.predict(input_array)
    predicted_class = int(np.argmax(prediction, axis=1)[0])  # For classification models
    
    return jsonify({"prediction": predicted_class})
