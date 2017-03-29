def slices(string, n):
    if n == 0 or n > len(string):
        raise ValueError()
    else:
        return [[int(string[x+y]) for y in xrange(n)] for x in xrange(len(string)+1-n)]
