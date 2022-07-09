import rpy2.robjects as ro

codigo_r = ('''
prime <- function(n){
    
  # arranging sequence
  x = seq(1, n)
    
  # creating an empty place to store the numbers
  prime_numbers=c()
    
  for (i in seq(2, n)) {
    if (any(x == i)) {
    
      # prime numbers gets stored in a sequence order
      prime_numbers = c(prime_numbers, i)
      x = c(x[(x %% i) != 0], i)
    }

  }
    
  # printing the series
  print(prime_numbers)
} 
''')


number = int(input("Introduce un número: "))

ro.r(codigo_r)
prime_py = ro.globalenv['prime']
prime_py(number)




