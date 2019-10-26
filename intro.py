import os
from sys import argv

script, first_Arg, sec_Arg = argv

formatter = "{} {}"
print(formatter.format(
        "Try",
        "****ker"))
#_______________
#Jumping lines
tryVar = "Jan\nFeb\nMarch"
print(tryVar)
print("""
Here is some text
""")
#______________
#Asking QUESTION:
print("What is your name?", end=' ')
name=input()
print(f"Hello {name}")
age=input("how old are you? ")
print(age)
#____
print(f"First argument is: {first_Arg}, second argument is: {sec_Arg}")
