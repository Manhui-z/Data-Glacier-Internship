import os
os.chdir('/Users/zhumanhui/Desktop/Data Glacier/Week 4 Flask/')
print("Current Working Directory:", os.getcwd())

import pandas as pd
import numpy as np
from flask import Flask, request, render_template, url_for
import pickle

app = Flask(__name__)  # app name

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

# set a post method to yield predictions on page
@app.route('/predict', methods = ['POST'])
def predict():

    # obtain value of all predcitors and place them in array
    int_features = [float(x) for x in request.form.values()]
    # conbine them all into a final numpy array
    final_features = [np.array(int_features)]
    # predict the optin values by given input predictors
    prediction = model.predict(final_features)[0]

    # if the ouput is negative, the predcitor values entered are unreasonable
    if prediction < 0:
        return render_template('index.html', predcition_text = 'Predicted option value is negative, values entered is unreasonable.')
    # if  the output is greater than 0, return prediction
    else:
        return render_template('index.html', prediction_text = 'Predicted option value is: $ {}'.format(prediction))
    
# run app
if __name__ == '__main__':
    app.run(port = 5000, debug = True)