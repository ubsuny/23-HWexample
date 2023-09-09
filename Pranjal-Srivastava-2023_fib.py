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
