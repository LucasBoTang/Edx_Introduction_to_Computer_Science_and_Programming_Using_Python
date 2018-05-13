def biggest(aDict):
    '''
    :type aDict: dict, where all the values are lists.
    :rtype: str, the key with the largest number of values associated with it
    '''
    biggest, count = None, 0
    for key, value in aDict.items():
        if len(value) > count:
            biggest, count = key, len(value)
    return biggest
