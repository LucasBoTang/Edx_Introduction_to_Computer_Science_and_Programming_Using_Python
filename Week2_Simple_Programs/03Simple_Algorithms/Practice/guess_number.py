print('Please think of a number between 0 and 100!')
low, high = 0, 100
check = None
while check != 'c':
    mid = (low + high) // 2
    print('Is your secret number ' + str(mid) + '?')
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if check == 'c':
        break
    elif check == 'h':
        high = mid
    elif check == 'l':
        low = mid
    else:
        print('Sorry, I did not understand your input.')
        continue
print('Game over. Your secret number was: ' + str(mid))
