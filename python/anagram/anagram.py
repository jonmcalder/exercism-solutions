def detect_anagrams(word, candidates):
  
  def matches_word(candidate):
    if candidate.lower() == word.lower():
      return False
    if len(candidate) != len(word):
      return False
    letters = word.lower()
    for char in candidate.lower():
      if char not in letters:
        return False
      else:
        letters = letters.replace(char, '', 1)
    return True
  
  return filter(matches_word, candidates)
