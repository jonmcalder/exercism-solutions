def rotate(text, shift):
    """
    Encrypt text using rotational cipher
    """
  
    def rotate_char(char, shift):
        """
        Shift character (preserving case) if it is a letter, 
        else return the character as is
        """

        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            if char.isupper():
              shifted_char = shifted_char.upper()
        else:
          shifted_char = char
        return shifted_char
    
    return ''.join([rotate_char(char, shift) for char in text])
