def processHarvardSentenceList(infile):
    with open(infile) as f:
        contents = f.read().strip().lower().replace(".", "").replace("\n", " ")
    return contents

if __name__ == "__main__":
    sampleTranscript = r"./transcriptions/list1.txt"

    print(processHarvardSentenceList(sampleTranscript))