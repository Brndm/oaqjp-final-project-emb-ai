import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    myobj = { "raw_document": { "text": text_to_analyze } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    record = {}
    prev = 0.0
    dom_emo = ''
    if response.status_code == 200:
        formated_response = json.loads(response.text)
        emotion = formated_response['emotionPredictions'][0]['emotion']
        record['anger'] = emotion['anger']
        record['disgust'] = emotion['disgust']
        record['fear'] = emotion['fear']
        record['joy'] = emotion['joy']
        record['sadness'] = emotion['sadness']
        for item in record.items():
            if float(item[1]) > prev:
                prev = float(item[1])
                dom_emo = item[0]
        record['dominant_emotion'] = dom_emo

    else:
        record = {'anger': '', 'disgust': '', 'fear': '', 'joy': '', 'sadness': '', 'dominant_emotion': ''}


    return record