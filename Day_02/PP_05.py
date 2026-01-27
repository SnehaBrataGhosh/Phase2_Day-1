# Q15. Ask the user for a password until they enter the correct one.
pas = "Jeet@3430"

while True:
    usr = input("Enter your password: ")
    if usr == pas:
        print("Correct Access Granted")
        break
    else:
        print("Try again")
