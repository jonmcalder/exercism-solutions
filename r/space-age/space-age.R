space_age <- function(seconds, planet) {

  earth_secs <- 31557600
  
  earth_years <- c(
    earth   = 1,
    mercury = 0.2408467,
    venus   = 0.61519726,
    mars    = 1.8808158,
    jupiter = 11.862615,
    saturn  = 29.447498,
    uranus  = 84.016846,
    neptune = 164.79132
  )
  
  round(seconds / earth_secs / earth_years[[planet]], 2)
  
}
