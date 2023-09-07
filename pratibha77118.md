# BASICS OF USING GIT AND GITHUB

# Five thing that I would like to learn in computation class this semester:
1. Learn about programming using python and C++.
2. Do numerical computation using these programs.
3. Data analysis and numeric computing.
4. Solve linear algebra, nonlinear equation and differention equations using computational method.
5. Learn the basic of quantam computing and version control technicalities.

# Example of python function correctly formatted as code:
Fibonacci function (Fibonacci(n)) calculates the n^th fibonacci number by creating datas of fibonacci sequence up to nth fibonacci number. It first uses
the first two fibonacci number (0 and 1) and then iteratively calculates the subsequent numbers.

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")

