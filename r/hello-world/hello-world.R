hello_world <- function(name = NULL) {
  if (is.null(name)) {
    print("Hello, World!")  
  }
  else {
    print(paste("Hello, ", name, "!", sep = ""))
  }
}
