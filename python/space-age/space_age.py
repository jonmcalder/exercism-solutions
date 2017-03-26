class SpaceAge(object):
    def __init__(self, secs):
        self.seconds = secs
    
    def planet_age(self, factor):
        return round(self.seconds / (24 * 3600 * 365.25 * factor), 2)
        
    def on_earth(self):
        return self.planet_age(1)
    
    def on_mercury(self):
        return self.planet_age(0.2408467)
        
    def on_venus(self):
        return self.planet_age(0.61519726)
        
    def on_mars(self):
        return self.planet_age(1.8808158)
        
    def on_jupiter(self):
        return self.planet_age(11.862615)
        
    def on_saturn(self):
        return self.planet_age(29.447498)
        
    def on_uranus(self):
        return self.planet_age(84.016846)
        
    def on_neptune(self):
        return self.planet_age(164.79132)
