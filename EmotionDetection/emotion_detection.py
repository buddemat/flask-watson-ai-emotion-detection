import json
import requests

def run_watson_emotion_detection(text_to_analyze):
    ''' Send text_to_analyze to embedded Watson NLP library service and process response. '''
    url = 'https://sn-watson-emotion.labs.skills.network/' \
          'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { 'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock' }
    input_json = { 'raw_document': { 'text': text_to_analyze } }

    response = requests.post(url, 
                             json=input_json, 
                             headers=headers)
    if response.status_code == 400:
        return { 'anger': None,
                 'disgust': None,
                 'fear': None,
                 'joy': None,
                 'sadness': None,
                 'dominant_emotion': None
               }
    elif response.status_code == 200:
        response_json = json.loads(response.text)
        response_emotions = response_json.get('emotionPredictions')[0].get('emotion')
        response_dominant = max(response_emotions, key=response_emotions.get)
        response_emotions.update({ 'dominant_emotion': response_dominant })
    
        return response_emotions
    else:
        return { 'message': response.text}, response.status_code