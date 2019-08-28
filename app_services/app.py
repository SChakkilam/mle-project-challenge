# Dependencies
from flask import Flask, request, jsonify
import pickle
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)
RFC = pickle.load(open('latePaymentsModel.pkl', 'rb')) # Load "model.pkl"
print ('Model loaded')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if RFC:
        try:
            json_ = request.get_json(force=True)
            print(json_)
            data = pd.DataFrame.from_dict(json_) 
            print(data)          
            prediction = list(RFC.predict_proba(data))
            return jsonify({'prediction': str(prediction)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000, debug=True)
