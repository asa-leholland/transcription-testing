from transcribeSR import transcribeSRGoogleCloudSpeech, transcribeSRSphinx

from transcribeGCSTT import processAudioinfileGCSTT

from runJiwer import determineAccuracy

from processSampleText import processHarvardSentenceList

from timeit import default_timer

from pathlib import Path

import pandas as pd

from transcribeVosk import transcribeVosk

# set this to True to test one audio file (rather than all 20)
IS_TESTING_ONE = False
IS_TESTING_APIS = False

transcriptFilePaths = Path('transcriptions').glob('*.txt')
audioFilePaths = Path('audiofiles').glob('*.wav')

transcriptionFunctions = {
    "Speech Recognition (CMU Sphinx)": transcribeSRSphinx,
    "VOSK (trained with Generic Eng. Model)": transcribeVosk
    }

if IS_TESTING_APIS:
    additional_services = [
        ("Speech Recognition (GoogleSpeech to Text)", transcribeSRGoogleCloudSpeech),
        ("google-cloud-speech", processAudioinfileGCSTT)
        ]
    for (serviceTitle, serviceFunction) in additional_services:
        transcriptionFunctions[serviceTitle] = serviceFunction

# create testing list of lists using audio files and transcriptions
sample_data = []

for audioFilePath in audioFilePaths:
    sample_data.append([str(audioFilePath)])

i = 0
for transcriptFilePath in transcriptFilePaths:
    sample_data[i].append(str(transcriptFilePath))
    i += 1
        

if IS_TESTING_ONE:
    sample_data = [sample_data[0]]



evaluation_results = []

# iterate over each transcription service function
for title, transcriptionFunction in transcriptionFunctions.items():

    # for each sample case
    for audioPath, rawTranscriptPath in sample_data:

        # obtain the expected final transcript result
        expectedTranscription = processHarvardSentenceList(rawTranscriptPath)

        # record the time taken to make the service call
        start = default_timer()
        actualTranscription = transcriptionFunction(audioPath)
        end = default_timer()
        duration = end - start

        # calcualte accuracy of result against expected results
        accuracy = determineAccuracy(expectedTranscription, actualTranscription)

        if IS_TESTING_ONE: 
            print(actualTranscription)

    evaluation_results.append((title, audioPath, duration, accuracy))


# create a dataframe to store results
results_df = pd.DataFrame(evaluation_results, columns=['Service', 'Source', 'Duration', 'Accuracy'])
results_df.to_csv('results.csv', sep=',', index=False)

summary_df = results_df.groupby('Service').mean().round(2)
print('\n', summary_df)
summary_df.to_csv('resultsSummary.csv', sep=',')