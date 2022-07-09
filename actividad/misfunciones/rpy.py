from rpy2.robjects import r

r('''
n=20
  
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
  
''')





