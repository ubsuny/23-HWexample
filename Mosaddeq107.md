
# This is an example homework for the courese PHY 410

Objectives: In this course, I would like to learn the five most important things as follows:

    1. Implementation of programming in Physics.
    2. To get introduced with Quantam computing.
    3. Woking in a project in GitHub.
    4. Got familiar with git.
    5. Learning programming in C, C++, and Python. 



### Python code of finding a Fibonacci series

    def fibonacci(n):
        a, b = 0, 1
        for i in range(n):
        a, b = b, a + b
        return a


    def main():
        n = int(input("Enter the number of terms: "))
        print("The Fibonacci series is:")
        for i in range(n):
            print(fibonacci(i))


    if __name__ == "__main__":
        main()