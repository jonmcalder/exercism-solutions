import string

def word_count(text):
  
  words = {}
  
  cleaned_text = text.replace("_", " ").replace(",", " ").translate(None, string.punctuation).lower()
  
  for word in cleaned_text.split():
    if word in words:
      words[word] += 1
    else:
      words[word] = 1
      
  return words
