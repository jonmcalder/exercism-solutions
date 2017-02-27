from datetime import timedelta

def add_gigasecond(date_time):
  
  d = timedelta(seconds = 10**9)
  
  return date_time + d
