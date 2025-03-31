from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('model/model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    
    # Make prediction
    prediction = model.predict([features])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)