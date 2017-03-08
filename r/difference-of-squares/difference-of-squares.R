# this is a stub function that takes a natural_number
# and should return the difference-of-squares as described
# in the README.md
difference_of_squares <- function(natural_number) {
  
  if (natural_number > 0) {
    sum(1:natural_number)^2 - sum(sapply(1:natural_number, FUN = function(x){ x^2 } ))
  } else {
    0
  }
}
