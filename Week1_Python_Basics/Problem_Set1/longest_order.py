result = cur = s[0]
for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        cur += s[i]
        if len(cur) > len(result):
            result = cur
    else:
        cur = s[i]
print('Longest substring in alphabetical order is: ' + result)
