word_count <- function(text) {

  # Get rid of punctuation, make lowercase, split
  words <- strsplit(tolower(gsub("[[:punct:]]", "", text)), " ")
  # Get rid of blanks, count, and transform into list
  as.list(table(lapply(words, function(x){x[!x ==""]})))
  
}
