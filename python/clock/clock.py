class Clock:
  
  def __init__(self, hours, minutes):
    """
    Create clock which keeps track of minutes
    Disregard time component over 24 hours
    """
    self.minutes = (hours * 60 + minutes) % (60 * 24)
    
  def add(self, minutes):
    """
    Add minutes, and disregard time component over 24 hours 
    """
    self.minutes = (self.minutes + minutes) % (60 * 24)
    return self

  def __str__(self):
    """
    Print method, shows hours and minutes
    """
    minutes = self.minutes % 60
    hours = int(self.minutes / 60)
    return str(hours).zfill(2)+":"+str(minutes).zfill(2)
    
  def __eq__(self, other):
    """
    Return True if other is also a Clock and has the same minutes as
    this one.
    """
    return isinstance(other, Clock) and self.minutes == other.minutes
