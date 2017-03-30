def score(word):
    
    letter_score = {}
    scores = {
      1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
      2: ['D', 'G'],
      3: ['B', 'C', 'M', 'P'],
      4: ['F', 'H', 'V', 'W', 'Y'],
      5: ['K'],
      8: ['J', 'X'],
      10: ['Q', 'Z']
    }
    
    for (x,y) in scores.items():
        for z in y:
            letter_score[z] = x

    score = 0
    for letter in word.upper():
        if letter in letter_score:
            score += letter_score[letter]
        else:
            return 0

    return score
