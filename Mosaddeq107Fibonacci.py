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
