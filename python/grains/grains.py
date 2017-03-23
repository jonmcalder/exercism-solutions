def on_square(x):
    return 2**(x-1)


def total_after(x):
    return sum(on_square(y) for y in xrange(1,x+1))
