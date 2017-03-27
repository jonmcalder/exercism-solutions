import re

class Phone(object):
    def __init__(self, number):
        num = re.sub(r'\D', "", number)
        if len(num) == 10:
            self.number = num
        elif len(num) == 11:
            if num[0] == "1":
                self.number = num[1:11]
            else:
                self.number = "0000000000"
        else:
            self.number = "0000000000"
      
    def area_code(self):
        return self.number[0:3]
        
    def pretty(self):
        return "(" + self.number[0:3] + ") " + self.number[3:6] + "-" + self.number[6:10]
