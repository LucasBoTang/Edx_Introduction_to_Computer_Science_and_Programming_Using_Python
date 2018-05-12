def polysum(n, s):
    '''
    :type n: int, number of sides
    :type s: float or int, length of each sides
    :rtype: float
    '''
    import math
    # Calculate the area of regular polygon
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    # Calculate the length of the boundary of the polygon
    p = s * n
    # Sum and round to 4 decimal places
    result = round(area + p ** 2, 4)
    return result 
