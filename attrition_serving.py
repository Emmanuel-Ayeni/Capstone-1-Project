import pickle
import numpy as np

from flask import Flask, request, jsonify

def predict_single(employee, dv, model):
    X = dv.transform([employee])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]




with open('hrAttrition_Log_model_v3.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('attrition')


@app.route('/predict', methods=['POST'])
def predict():
    employee = request.get_json()

    prediction = predict_single(employee, dv, model)
    attrition = prediction >= 0.5
    
    result = {
        'attrition_probability': float(prediction),
        'attrition': bool(attrition),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)