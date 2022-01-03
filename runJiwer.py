from jiwer import wer


# jiwer calculates the word error rate between an expected string and an provided string
# WER is expressed as a decimal where 1.0 is complete error and 0 represents no errors
# accuracy below is used to determine the opposite: where 1.0 is perfectly accurate and 0.0 is perfectly flawed
def determineAccuracy(expected, actual):
    if not isinstance(expected, str):
        print("TypeError: expected value is not a string")
        return False
    elif not isinstance(actual, str):
        print("TypeError: actual value is not a string")
        return False
    else:
        return 1 - wer(expected.lower(), actual.lower())