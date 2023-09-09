# My Semester Goals

## Things I Want to Learn

- C++ programming
- Python programming
- Data analysis 
- Version control with Git
- Quantum Computing 

## Example Python Function

Here's an example of a Python function that calculates the Fibonacci series and return it as a list:
```python
def fib(n):
    fibonacci_sequence = [] #Declaring an empty list.
    a = 0
    b = 1
    for i in range(n):
        fibonacci_sequence.append(b) #Appending the list each time the loop runs.
        c = b + a
        a = b #New value of a
        b = c #New value of b
    return fibonacci_sequence
```
