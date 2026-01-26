
# Swap Two Numbers
# Swap two variables without using a third variable.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"The element a is {a} and element b is {b} before swapping")
a, b = b, a
print(f"The element a is {a} and element b is {b} after swapping")