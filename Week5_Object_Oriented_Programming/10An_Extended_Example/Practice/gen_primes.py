def genPrimes():
    num = 2
    primes = []
    while True:
        primes.append(num)
        yield num
        while not all([num % prime != 0 for prime in primes]):
             num += 1
