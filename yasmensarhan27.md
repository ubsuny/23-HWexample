# My goals for this semester
 
  - to master the computational methods taught vis this course and beyond
  - to get A grades in all courses for this semster
  - to accomplish all the tasks required in this semester befor the deadline and have some time to chill.
  - to acheive all the courses requirements and be qualified for my dream research topic
  - to be discipline and never lose the track during the whole learning process

# A code that calculate fibonacci series and allow you to get each index in the series:

def fibonacci(n):
  ###
  This function calculates the Fibonacci number at the nth index.
 
  Args:
    n: The index of the number in fibonacci series.
    x: The 1st element in the fibonacci series.
    y: The 2nd element in the fibonacci series

  Returns:
    After  you will entre n as the index of the number in fibonacci series, the coder will resturn the nth index in Fibonacci series.

  ###
  x, y = 0, 1
  for i in range(n):
    x, y = y, x + y
  return x

n = int(input("type the index number you want to know: "))
print(fibonacci(n))
