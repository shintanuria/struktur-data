def fibonacci(n):
  if n <= 1:
    return n
  else:
    return (fibonacci(n-1) + fibonacci(n-2))

bil = 5
print(fibonacci(bil))
