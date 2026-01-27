# Q13. Print all numbers between 1 and 100 that are divisible by 7.
n  =  int(input("Enter a number: "))
for i in range(1,n+1):
    if(i%7==0):
        print(i)

