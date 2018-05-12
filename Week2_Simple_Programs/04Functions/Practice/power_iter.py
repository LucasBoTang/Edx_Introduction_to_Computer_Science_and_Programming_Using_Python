def iterPower(base, exp):
    '''
    :type base: int or float
    :type exp: int >= 0
    :rtype: int or float
    '''
    result = 1
    while exp:
        result *= base
        exp -= 1
    return result
