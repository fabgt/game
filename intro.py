import os
#os.system("ls -l")#

#print("Math example", 5 / 6 < 1)
#print("Math example", 50 % 6)

myVar1 = 12
myVar2 = 10
newVar = myVar1 > myVar2
print("result:",newVar)
car_brand = 'volvo'
print(car_brand)
#f-string example
a = f"My favorite brand is {car_brand}"
print(f"why do you keep saying '{a}'?")

new_f_strg = "This is my new {}"
bool = False

print(new_f_strg.format(bool))
print(a + new_f_strg.format(bool))
