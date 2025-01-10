''' The code in this module starts the application of emotion
    detection to be executed as Flask app and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import run_watson_emotion_detection as emo

app = Flask('Emotion Detection')

@app.route('/')
def show_index_page():
    '''Function to display index page.'''
    return render_template('index.html')

@app.route('/emotionDetector')
def run_emotion_detection():
    '''Function to pass input text to emotion detection service and render answer for display.'''
    text_to_analyze = request.args.get('textToAnalyze')
    result_json = emo(text_to_analyze)
    dominant_emotion = result_json.get('dominant_emotion')
    if dominant_emotion is None:
        return '<b>Invalid text! Please try again!</b>'

    result_json.pop('dominant_emotion')
    return f'For the given statement, the system response is {str(result_json).strip("{}")}. ' \
           f'The dominant emotion is <b>{dominant_emotion}</b>.'

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
            