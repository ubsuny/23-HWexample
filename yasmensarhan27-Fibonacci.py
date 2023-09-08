def fibonacci(n):
  x, y = 0, 1
  for i in range(n):
    x, y = y, x + y
  return x
n=int(input("type the index number you want to know: "))
print(fibonacci(n))
