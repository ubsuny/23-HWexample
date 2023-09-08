Title: This semester will be awesome.
I would like to learn a couple of things this semester.
Data analysis by Python
C++
From syntax error, I would like to code properly without the help of chat gpt.
Quantum computing a bit.
I would like to learn to create structured data with sets, tuples, and list.


Here is the Python code for the Fibonacci series


def fibonacci(n):
    
    fib_series = [0, 1]

    
    while len(fib_series) < n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series


num_terms = 10  


result = fibonacci(num_terms)
print(result)
