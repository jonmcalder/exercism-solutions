def encode(text):
  
  last = ''
  counter = 1
  code = ''
  
  for c in text:
    if c == last:
      counter += 1
    else:
      if counter > 1:
        code += str(counter)
        counter = 1
      code += last
      last = c
  
  if counter > 1:
    code += str(counter)
  code += last
  
  return code
  
def decode(code):
  
  counter = 1
  last = ''
  text = ''
  
  for c in code:
    if c.isdigit():
      if last.isdigit():
        counter = int(last+c)
      else:
        counter = int(c)
    else:
      text += c * counter
      counter = 1
    last = c
      
  return text
