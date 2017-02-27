import re

def hey(what):
  
  if re.search(r"[A-Z]+", what) and what == what.upper():
    response = 'Whoa, chill out!'
  elif re.search(r"\?\s*$", what):
    response = 'Sure.'
  elif not re.search(r"[A-Za-z0-9]", what):
    response = 'Fine. Be that way!'
  else:
    response = 'Whatever.'

  return response
