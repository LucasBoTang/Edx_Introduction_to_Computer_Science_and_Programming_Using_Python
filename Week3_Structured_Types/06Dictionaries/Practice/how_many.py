def how_many(aDict):
    '''
    :type aDict: dict, where all the values are lists.
    :rtype: int, how many values are in the dictionary.
    '''
    count = 0
    for value in aDict.values():
        count += len(value)
    return count
