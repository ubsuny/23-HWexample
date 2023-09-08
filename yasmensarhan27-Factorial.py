print("This function is used to calculate the factorial")
n= int(input("write a number you want to calculate the factorial for: "))
def factorial(n):
    if n==0:
        return 1;
    if n<0:
        print("No Factorial for this number")
        return "none";
    else:
        return n * factorial(n-1);
print(factorial(n))
