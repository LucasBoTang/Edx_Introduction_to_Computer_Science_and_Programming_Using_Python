def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    # for increasing
    incr_max_len = incr_cur_len = 1
    incr_max_sum = incr_cur_sum = L[0]
    incr_index = 0

    for i in range(len(L) - 1):
        if L[i] <= L[i+1]:
            incr_cur_len += 1
            incr_cur_sum += L[i+1]
            if incr_max_len < incr_cur_len:
                incr_max_len, incr_max_sum, incr_index = incr_cur_len, incr_cur_sum, i
        else:
            incr_cur_len = 1
            incr_cur_sum = L[i+1]
        #print(L[i], incr_max_len, incr_max_sum)

    # for decreasing
    decr_max_len = decr_cur_len = 1
    decr_max_sum = decr_cur_sum = L[0]
    decr_index = 0

    for i in range(len(L) - 1):
        if L[i] >= L[i+1]:
            decr_cur_len += 1
            decr_cur_sum += L[i+1]
            if decr_max_len < decr_cur_len:
                decr_max_len, decr_max_sum, decr_index = decr_cur_len, decr_cur_sum, i
        else:
            decr_cur_len = 1
            decr_cur_sum = L[i+1]
        #print(L[i], decr_max_len, decr_max_sum)

    # compare increasing and decreasing
    if incr_max_len > decr_max_len:
        return incr_max_sum
    elif incr_max_len < decr_max_len:
        return decr_max_sum
    else:
        if incr_index < decr_index:
            return incr_max_sum
        else:
            return decr_max_sum
