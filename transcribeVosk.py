from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
import pickle
from os.path import exists

print('starting Vosk...')
#  on startup, check to see if we have a base pickle we can use to load the vosk model
if not exists('voskModel.pickle'):
    # Note that this is where I installed my copy of the Vosk training data, YMMV
    model = Model("./dependencies/vosk-model-en-us-0.22")
    with open('voskModel.pickle', 'wb') as f:
        pickle.dump(model, f)

# Once we have a working pickle, initialize the NLP model of the audio data
with open('voskModel.pickle', 'rb') as f:
    try:
        model = pickle.load(f)
    except EOFError:
        print('Error: voskModel.pickle was empty')
        model = Model("./dependencies/vosk-model-en-us-0.22")
        
print('loaded Vosk.')

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


if __name__ == "__main__":
    print(transcribeVosk('audio_files_harvard.wav'))