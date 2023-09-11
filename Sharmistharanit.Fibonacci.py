def generate_fibonacci(n):
    fibonacci_series = []
    
    
    a, b = 0, 1
    
    
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    
    return fibonacci_series
num_terms = 10
fib_series = generate_fibonacci(num_terms)
print("Fibonacci Series:")
print(fib_series)
