def encode(string):
  """
  Encrypt text using atbash cipher
  """
  encoded = transform(string)
  encoded_blocks = ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))
  return encoded_blocks

def decode(string):
  """
  Encrypt text using atbash cipher
  """
  return transform(string)
  
def transform(raw_string):
  clean_string = ''.join(char.lower() for char in raw_string if char.isalnum())
  return ''.join(chr(25 - (ord(char)-97) + 97) if char.isalpha() else char for char in clean_string)
