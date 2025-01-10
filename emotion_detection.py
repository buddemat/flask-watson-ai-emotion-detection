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
    output_json = json.loads(response.text)
    return output_json