# Q16. Write a program to find all factors of a number.
a = int(input("Enter the number: "))

print(f"Factors of {a} are: ", end="")
for i in range(1, a+1):
    if a % i == 0:
        print(i, end=" ")
