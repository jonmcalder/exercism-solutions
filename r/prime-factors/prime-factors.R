prime_factors <- function(number) {

  factors <- c()
  rem <- number
  current_prime <- 2
  while (rem > 1) {
    if (rem %% current_prime == 0) {
      rem <- rem / current_prime
      factors[length(factors) + 1] <- current_prime
    } else {
      current_prime <- current_prime + 1
    }
  }
  factors
  
}
