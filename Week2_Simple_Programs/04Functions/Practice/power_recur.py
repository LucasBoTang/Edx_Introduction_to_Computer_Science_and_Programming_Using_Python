def recurPower(base, exp):
    '''
    :type base: int or float
    :type exp: int >= 0
    :rtype: int or float
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
