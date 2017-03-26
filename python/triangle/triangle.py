class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, a, b, c):
        lengths = sorted((a, b, c))
        if lengths[0] == 0:
            raise TriangleError("Triangle side(s) have zero length")
        elif lengths[0] + lengths[1] <= lengths[2]:
            raise TriangleError("Triangle side lengths violate the triangle inequality")
        self.lengths = lengths
        
    def kind(self):
        if len(set(self.lengths)) == 1:
            return "equilateral"
        elif len(set(self.lengths)) == 2:
            return "isosceles"
        else:
            return "scalene"
