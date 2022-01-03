import os

from google.cloud import speech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'client_service_key.json'

speech_client = speech.SpeechClient()

def processAudioinfileGCSTT(infile):
    with open(infile, 'rb') as file:
        byte_data_infile = file.read()

    audio = speech.RecognitionAudio(content=byte_data_infile)

    config = speech.RecognitionConfig(
        language_code = 'en-us', 
    )

    response = speech_client.recognize(config=config, audio=audio)

    return response.results[0].alternatives[0].transcript
