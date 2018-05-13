def oddTuples(aTup):
    '''
    :type aTup: a tuple
    :rtype: tuple, every other element of aTup.
    '''
    result = ()
    for i in range(0, len(aTup), 2):
        result += (aTup[i],)
    return result
