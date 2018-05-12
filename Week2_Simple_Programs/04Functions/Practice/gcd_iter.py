def gcdIter(a, b):
    '''
    :type a: positive int
    :type b: positive int
    :rtype: positive int, the greatest common divisor of a & b
    '''
    gcd = min(a, b)
    while gcd > 1:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd -= 1
    return gcd
