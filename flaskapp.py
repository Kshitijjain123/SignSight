#redeploy
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "SignSight API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Dummy response for now
    data = request.get_json()
    return jsonify({"prediction": "Hello", "input": data})

if __name__ == '__main__':
    app.run(debug=True)

