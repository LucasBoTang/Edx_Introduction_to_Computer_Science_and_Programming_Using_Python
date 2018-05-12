vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for letter in s:
    if letter in vowels:
        count += 1
print('Number of vowels: '+str(count))
