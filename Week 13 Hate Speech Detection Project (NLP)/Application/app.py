import os
os.chdir('/Users/zhumanhui/Desktop/Data Glacier/Week 7-13 Project/Application/')

from flask import Flask, request, render_template, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and vectorizer
with open('rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        tweet = request.form['tweet']
        tweet_vectorized = vectorizer.transform([tweet])
        prediction = model.predict(tweet_vectorized)
        result = 'This is a hate tweet. 😡' if prediction[0] == 1 else 'This is a non-hate tweet. 😊'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)