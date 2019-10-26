import os

card_red = 'heart'
#f-string example
a = f"My favorite brand is {card_red}"
print(f"why do you keep saying '{a}'?")
#____________
#Use format method
new_f_strg = "This is my new {}"
bool = False
print(new_f_strg.format(bool))
#_____________

formatter = "{} {} {} {}"
print(formatter.format(
        "Try",
        "This",
        "Motha",
        "****ker"
))

#_______________
#Jumping lines
tryVar = "Jan\nFeb\nMarch"
print(tryVar)
print("""
Here is some text
""")
#______________

fat_at="""
I'll write something with a list:
\t* cat
\t* cat
"""
print(fat_at)
#____________
#Asking QUESTION:
print("What is your name?", end=' ')
name=input()
print(f"Hello {name}")
age=input("how old are you? ")
print(age)
