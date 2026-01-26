# Find Largest Number
# Take three numbers as input and print the largest one.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if(a>b and a>c):
    print("Largest nos is ", a)
elif(b>a and b>c):
    print("Largest nos is ", b)
else:
    print("Largest nos is ", c)