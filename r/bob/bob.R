bob <- function(input) {

  if (input==toupper(input) & grepl("[[:upper:]]+", input)) {
    return ("Whoa, chill out!")
  }
  else if (grepl("[^A-Z]+.*\\?\\s*$", input)) {
    return ("Sure.")
  }
  else if (!grepl("[A-Za-z0-9]", input)) {
    return ("Fine. Be that way!")
  }
  else {
    return ("Whatever.")
  }
  
}
