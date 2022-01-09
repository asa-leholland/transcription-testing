import os

static_path = "./dependencies/vosk-model-en-us-0.22"

def listContents(path):
    print(os.listdir(static_path))

def is_file_empty(filepath):
    return os.path.exists(filepath) and os.stat(filepath).st_size == 0