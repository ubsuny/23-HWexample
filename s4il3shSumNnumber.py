print("This program will help you to find the sum of first n number.")
ask = int(input('input the number \n'))

s = 0
for i in range(ask+1):
    s+=i
print("The sum of the first", ask, " number is", s, ".")
