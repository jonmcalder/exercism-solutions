def distance(a, b):
  
  if len(a) == len(b):
    return sum([x!=y for x,y in zip(a,b)])
  else:
    raise ValueError("DNA strands are of different lengths")
