from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
import pickle

#  on startup, check to see if we have already iniitalized an NLP model of the audio data
model = Model("./dependencies/vosk-model-en-us-0.22")


def transcribeVosk(infile):
    wf = wave.open(infile, "rb")

    transcription = []

    rec = KaldiRecognizer(model, wf.getframerate())

    while True:
        chunk_data = wf.readframes(4000)
        if len(chunk_data) == 0:
            break
        if rec.AcceptWaveform(chunk_data):
            result_dict = json.loads(rec.Result())
            transcription.append(result_dict.get("text", ""))
    

    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    transcription_text = ' '.join(transcription)
    return transcription_text