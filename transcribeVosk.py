from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
import pickle

from timeit import default_timer

from utilities.utilityTesting import is_file_empty 

print('Starting Vosk...')
#  on startup, check to see if we have a base pickle we can use to load the vosk model

vosk_start = default_timer()
# This commented code would work to Pickle the vosk filename, but vosk createas _cffi_backend._CDataBase using C, which are unpickable.
# Therefore, currently Vosk must recreate the model each time

# VOSK_PICKLE_FILENAME = 'voskModel.pickle'
# if not is_file_empty(VOSK_PICKLE_FILENAME):
#     # Note that this is where I installed my copy of the Vosk training data, YMMV
#     model = Model("./dependencies/vosk-model-en-us-0.22")
#     with open(VOSK_PICKLE_FILENAME, 'wb') as f:
#         pickle.dump(model, f)

# # Once we have a working pickle, initialize the NLP model of the audio data
# with open(VOSK_PICKLE_FILENAME, 'rb') as f:
#     try:
#         model = pickle.load(f)
#     except EOFError:
#         print(f'Error: {VOSK_PICKLE_FILENAME} was empty')
#         model = Model("./dependencies/vosk-model-en-us-0.22")
model = Model("./dependencies/vosk-model-en-us-0.22")
vosk_end = default_timer()
vosk_setup_duration = round(vosk_end - vosk_start, 2)
print(f'Vosk is loaded. This took {vosk_setup_duration} seconds.')

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