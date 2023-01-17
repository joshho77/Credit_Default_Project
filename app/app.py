import numpy as np
from numpy import asarray
from flask import Flask, request, jsonify, render_template
import pickle as pkl

app = Flask(__name__)
pipe = pkl.load(open('pipe.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [float(x) for x in request.form.values()]
    final_features = asarray([features])
    prediction = pipe.predict(final_features)

    output = prediction[0]

    if output == 1:
        result = 'Based on the information provided, this individual will likely default on their loans.'
    else:
        result = 'Based on the information provided, this individual will likely not default on their loans!'

    return render_template('index.html', prediction_text='{}'.format(result))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)