def isIn(char, aStr):
    '''
    :type char: str, a single character
    :type aStr: str, an alphabetized string
    :rtype: bool, True if char is in aStr; False otherwise
    '''
    mid = len(aStr) // 2
    if not mid:
        return char == aStr
    elif char == aStr[mid]:
        return True
    elif char > aStr[mid]:
        return isIn(char, aStr[mid:])
    else:
        return isIn(char, aStr[:mid])
