# Q14. Write a program to calculate the sum of digits of a number (e.g., 123 → 6).
a = int(input("Enter a number: "))
sum_digits = 0

while a > 0:
    digit = a % 10        
    sum_digits += digit   
    a //= 10              

print("Sum of digits is: ",sum_digits)
