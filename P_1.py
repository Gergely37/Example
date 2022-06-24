
#variable = a container for a value. Behaves as the value that it contains

#string = a series of characters
first_name = "Bro"
last_name = "Code"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
# print(type(first_name))

#int = a whole integer
age = 21
age += 1
print("Your age is: "+str(age))
# print(type(age))

#float = a decimal number
height = 250.5
print("Your height is: "+str(height)+"cm")
# print(type(height))

#boolean = True or False
human = True
print("Are you a human: "+str(human))
# print(type(human))

##########################################################

# multiple assignment = allows us to assign multiple variables at the same time in one line of code

name = "Bro"
age = 21
attractive = True

name, age, attractive = "Bro", 21, True

print(name)
print(age)
print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

##########################################################

#string methods

name = "Bro"

print(len(name)) #technically this is a function
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*3)

##########################################################

#Type cast

x = 1   #int
y = 2.0 #float
z = "3" #str

x = int(x)
y = int(y)
z = int(z)

x = float(x)
y = float(y)
z = float(z)

x = str(x)
y = str(y)
z = str(z)

print(x)
print(y)
print(z*3)

##########################################################

#User input

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")

##########################################################

##!!!
import math


pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z))

##########################################################

#string slicing

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Bro Code"

first_name = name[:3]       # [0:3]
last_name = name[4:]        # [4:end]
funky_name = name[::2]      # [0:end:2] BoCd
reversed_name = name[::-1]  # [0:end:-1] edoC orB

print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])

##########################################################
