# Math

# + is addition
# - is subtraction
# * is multiplication
# / is devision
# ** identifies an exponent
# () is parentesis

# PEMDAS is in play

# Addition

print(1 + 1)

# Subtraction

print(5 - 3)

# Multiplication

print(9 * 9)

# Devision

print(100 / 4) # will return as a float
# to get an integer value displayed after dividing, use //. This will delete the decimal and all behind it.
print(100 // 4)
# you could also round the final value to the nearest wanted value with round(x,y) where x is the value and y is the desired decimal place
print(round(800 / 3.1315)) # excluding the second number rounds the value to an integer
print(round(800 / 3.1315, 5)) # including the second number rounds the value to the desired decimal

# Exponents

print(2 ** 3)

# Parenthesis

# forces the formula within the () to happen first.

print(2 - 1 + 3) #without parethesis python reads from left to right. Output = 4
print(2 - (1 + 3)) #with parethesis 1+3 happens before being subtracted from 2. Output = -2

# PEMDAS

#Parethesis
#Exponents
#Multiplication & Division
#Addition & Subtraction

print((3 - 1) ** 2 * 4 + 8 / 2)

# What's happening?
#First, parethesis
print(3 - 1) # (2) ** 2 * 4 + 8 / 2
#Exponents next
print(2 ** 2) # (4) * 4 + 8 / 2
#Multiplication and Devision 
print(4 * 4, 8 / 2) #(16) + (4.0)
#Adiition and Subtraction
print(16 + 4.0)

# Using Variables

#you can use variables in a python formula

income = 4852.36
expenses = 2799.41
profit = income - expenses

print(profit)

#Use

print("Are you old enough to drink alcohol?")

age = int(input("How old are you? "))
age_to_drink = 21
able_to_drink = age - age_to_drink

if able_to_drink >= 0:
    print("You can drink alcohol responsibly.")
else:
    print(f"You need to wait {able_to_drink * -1} years.")