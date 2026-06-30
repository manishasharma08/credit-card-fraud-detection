from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

model = pickle.load(open('fraud_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    data = np.array(data).reshape(1, -1)

    # scale Amount (last column assumed)
    data[0][-1] = scaler.transform([[data[0][-1]]])[0][0]

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    return jsonify({
        'fraud': int(prediction),
        'probability': float(prob)
    })

if __name__ == '__main__':
    app.run(debug=True)