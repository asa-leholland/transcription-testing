# main.py
# Author: Asa LeHolland


import speech_recognition  as sr

def getSRVersion():
    return sr.__version__


def getHarvardAudioText(pathToAudioFile):
    r = sr.Recognizer()


    validAudio = sr.AudioFile(pathToAudioFile)

    with validAudio as source:
        audioFile = r.record(source)

    return r.recognize_google(audioFile)





if __name__ == "__main__":
    print(getHarvardAudioText())