import re

def is_isogram(word):
    letter_count = {}
    for x in re.sub(r'[^a-z]', '', word.lower()):
      if x in letter_count:
        return False
      else:
        letter_count[x] = 1
    return True
