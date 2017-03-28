def sieve(n):
    if n < 2:
      return []
    primes = {key: True for key in xrange(2, n+1)}
    for x in xrange(2, n+1):
        if primes[x]:
            for y in xrange(2*x, n+1, x):
                primes[y] = False
    return [key for (key, value) in primes.items() if value]
        
