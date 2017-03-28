class School(object):
    def __init__(self, school_name):
        self.name = school_name
        self.grades = {}
        
    def add(self, name, grade):
        if grade not in self.grades:
            self.grades[grade] = set()
        self.grades[grade].add(name)
        
    def grade(self, grade):
        return self.grades[grade] if grade in self.grades else set()
        
    def sort(self):
        return [(key, tuple(value)) for (key, value) in self.grades.items()]
