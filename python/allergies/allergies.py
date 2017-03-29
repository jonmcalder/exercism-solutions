class Allergies(object):
  
    def __init__(self, score):
        allergyDict = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}
        self.lst = []
        score_remaining = score % 256
        for key in reversed(sorted(allergyDict.keys())):
            if score_remaining / key > 0:
                self.lst.append(allergyDict[key])
                score_remaining = score_remaining % key
        
    def is_allergic_to(self, allergy):
        return allergy in self.lst
