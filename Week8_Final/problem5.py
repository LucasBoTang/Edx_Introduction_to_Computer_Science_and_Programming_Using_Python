def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    result = []
    counts = {}
    for value in aDict.values():
        counts[value] = counts.get(value, 0) + 1
    for key, value in aDict.items():
        if counts[value] == 1:
            result.append(key)
    result.sort()
    return result