import re

def calculate(phrase):
  calc = phrase
  pattern = r".*?([-0-9]+[A-z ]+[-0-9]+).*?"
  m_any = re.match(pattern, calc)
  while (m_any is not None):
    mult_div = re.match(r".*?([-0-9 ]+[multiplied by|divided by][-0-9 ]+).*?", calc)
    if (mult_div is not None):
      repl = simplify(mult_div.group(1))
      calc = calc.replace(mult_div.group(1), repl)
    else:
      repl = simplify(m_any.group(1))
      calc = calc.replace(m_any.group(1), repl)
    m_any = re.match(pattern, calc)
  
  final = re.match(r"[^-0-9]*([-0-9]+)[^-0-9]*", calc)
  return int(final.group(1))

def simplify(sub_phrase):
  m = re.match(r"([-0-9 ]+)(plus|minus|multiplied by|divided by)([-0-9 ]+)", sub_phrase)
  if (m is None):
    raise ValueError("Unknown operation")
  elif (m.group(2) == "multiplied by"):
    result = int(m.group(1))*int(m.group(3))
  elif (m.group(2) == "divided by"):
    result = int(m.group(1))/int(m.group(3))
  elif (m.group(2) == "plus"):
    result = int(m.group(1))+int(m.group(3))
  elif (m.group(2) == "minus"):
    result = int(m.group(1))-int(m.group(3))
  return str(result)
