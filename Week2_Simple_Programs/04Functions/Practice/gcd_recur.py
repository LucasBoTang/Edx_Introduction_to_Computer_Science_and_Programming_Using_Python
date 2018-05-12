def gcdRecur(a, b):
    '''
    :type a: positive int
    :type b: positive int
    :rtype: positive int, the greatest common divisor of a & b
    '''
    if not b:
        return a
    else:
        return gcdRecur(b, a % b)
