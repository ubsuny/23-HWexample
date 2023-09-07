print("This program will help you to find the sum of first n number.")
ask = int(input('input the number \n'))

s = 0
for i in range(ask+1):
    s+=i
print("The sum using for loop is", s)

#the other way to find the sum is using formula

j = int(ask*(ask+1)/2)
print("the sum using the formula is", j)
