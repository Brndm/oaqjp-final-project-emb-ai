"""This module allows to run an app using emotion detection"""
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """This function sends a request and apply the emotion detection algorithm """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = str(response['anger']) if response['anger'] is not None else '0.0'
    disgust = str(response['disgust']) if response['disgust'] is not None else '0.0'
    fear = str(response['fear']) if response['fear'] is not None else '0.0'
    joy = str(response['joy']) if response['joy'] is not None else '0.0'
    sadness = str(response['sadness']) if response['sadness'] is not None else '0.0'

    if response['dominant_emotion'] is not None:
        label = "For the given statement, the system response is 'anger': " + anger +\
        ", 'disgust': " + disgust + ", 'fear': " + fear + ", 'joy': " + joy +\
        " and 'sadness': " + sadness + ". The dominant emotion is "\
        + str(response['dominant_emotion']) + "."
    else:
        label = 'Invalid text! Please try again!'
    return label

@app.route("/")
def render_index_page():
    """This function allows to use the web application structure"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
