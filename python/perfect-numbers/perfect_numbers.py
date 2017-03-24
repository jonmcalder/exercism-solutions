def is_perfect(n):
    total = 1
    for x in xrange(2, int(n**0.5) + 1):
      if n % x == 0:
        total += x
        total += n/x
    return total == n
