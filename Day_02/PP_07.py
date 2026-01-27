# Q17. Reverse a string using a loop (no slicing).
a = input("Enter a string: ")
rev = ""

for ch in a:          
    rev = ch + rev    

print("Reversed string:", rev)