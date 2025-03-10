"""
In this basic program of python we can conclude and see conditionals as the main
character.  this basic programs tells you if ur password is correct or incorrect.
LEST DIVE INTO IT
"""

Num1 = int(input("Enter a number for the data"))
passwordU = input("Enter the password")
password = "Hello1234"
passwordG = False


if passwordU == password:
    print("Your Password is correct")
    passwordG = True
else:
    print("Your password is Incorrect")
    passwordG = False

if passwordG == True:
    print("You have acess to your data")
    print(f"This is the data {Num1}")


