def factorial(n):
  if(n == 0):   # base case ( n == 0 )
    return 1
  else:         # recursive case ( n > 0 )
    return n * factorial(n-1) 

print(factorial(4))