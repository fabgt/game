
from sys import argv

script, filename = argv

txt = open(filename)

print(f"We are going to erase {filename}.")
print("If you don't want to press CTRL+C")
print("If you do want it, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()

print("Let's reopen it and verify the content.")

reopen = open(filename)
print(reopen.read())
#formatter = "{} {}"
#print(formatter.format(
#        "Try",
#        "****ker"))
#_______________
#Jumping lines
#tryVar = "Jan\nFeb\nMarch"
#print(tryVar)
#print("""
#Here is some text
#""")
#______________
#Asking QUESTION:
#print("What is your name?", end=' ')
#name=input()
#print(f"Hello {name}")
#age=input("how old are you? ")
#print(age)
#____
#print(f"First argument is: {name}, second argument is: {age}")
#prompt="> "
