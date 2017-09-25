from itertools import groupby

def getFrequencyOfElements(array):
    return [len(list(group)) for key, group in groupby(array)]