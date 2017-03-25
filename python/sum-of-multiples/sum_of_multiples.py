def sum_of_multiples(up_to, nums):
  multiples = set()
  for num in nums:
    for x in xrange(1, (up_to - 1)/num+1):
      multiples.add(x*num)
  return sum(multiples)
