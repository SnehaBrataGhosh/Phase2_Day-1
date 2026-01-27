# Q18. Print the multiplication table of a number (e.g., 5 × 1 … 5 × 10).
a = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")