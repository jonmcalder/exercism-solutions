lyrics <- function(first, last) {
  
  paste(
    lapply(first:last, verse),
    collapse = "\n"
  )
  
}

verse <- function(number) {
  
  num = number
  next_num = number - 1
  bot = "bottles"
  next_bot = "bottles"
  next_step = "Take one down and pass it around,"
  
  if (number == 2) {
    next_bot = "bottle"
  }
  if (number == 1) {
    bot = "bottle"
    next_step = "Take it down and pass it around,"
    next_num = "no more"
  }
  if (number == 0) {
    num = "No more"
    next_step = "Go to the store and buy some more,"
    next_num = 99
  }
  
  paste0(
    num, " ", bot, " of beer on the wall, ", tolower(num), " ", bot, " of beer.\n",
    next_step, " ", next_num, " ", next_bot, " of beer on the wall.\n"
  )
  
}
