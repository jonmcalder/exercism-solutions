anagram <- function(subject, candidates) {
  
  subject_letters <- tolower(strsplit(subject, "")[[1]])
  word_letters <- subject_letters
  target <- table(word_letters)
  
  is_anagram <- function(word) {
    word_letters <- tolower(strsplit(word, "")[[1]])
    if (identical(table(word_letters), target) & !identical(word_letters, subject_letters)) {
      TRUE
    }
    else {
      FALSE
    }
  }
  
  matches <- sapply(candidates, FUN = is_anagram)
  
  if(!any(matches)) {
    c()
  }
  else {
    candidates[matches]
  }
}
