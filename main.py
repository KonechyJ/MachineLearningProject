import pandas as PD
import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text)))['compound'])


    if (score > 0):
        label = "This is a good thing"
    elif (score == 0):
        label = "This sentence is neutral"
    else:
        label = "This is a bad thing"

    return (render_template('index.html', variable=label))
if __name__ == "__main__":
    app.run(port="8088", threaded=False)