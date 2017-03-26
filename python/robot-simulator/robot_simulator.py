NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

class Robot(object):
    def __init__(self, direction = NORTH, x_coord = 0, y_coord = 0):
        self.bearing = direction
        self.coordinates = (x_coord, y_coord)
      
    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4
        
    def turn_left(self):
        for i in xrange(3):
            self.turn_right()
        
    def advance(self):
        x, y = self.coordinates
        if self.bearing == NORTH:
          self.coordinates = (x, y+1)
        elif self.bearing == SOUTH:
          self.coordinates = (x, y-1)
        elif self.bearing == EAST:
          self.coordinates = (x+1, y)
        else:
          self.coordinates = (x-1, y)
          
    def simulate(self, commands):
        for command in commands:
            if command == "L":
                self.turn_left()
            elif command == "R":
                self.turn_right()
            elif command == "A":
                self.advance()
            else:
                raise ValueError("Unknown command")
