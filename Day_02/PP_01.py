# Q11. Check whether a character is a vowel or consonant.
b = input("Enter only a letter : ")
a = b.lower()
if((a == 'a') or (a == 'e') or (a == 'i') or (a =='o') or (a == 'u')):
    print("Vowels")
else:
    print("Consonents")