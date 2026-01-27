# Q12. Take marks as input and print the Grade (A/B/C/D/F).
m  = float(input("Enter your marks "))
if(m > 90 and m <=100):
    print("Hey u got great rank and your grade is A")
elif(m >80 and m<=90):
    print("Hey u got nice rank and your grade is B")
elif(m > 70 and m<=80):
    print("Hey u got good rank and your grade is C")
elif(m > 60 and m<= 70):
    print("Hey u can better your grades, grade is D")
else:
    print("You didnt perform well ur grade is F")