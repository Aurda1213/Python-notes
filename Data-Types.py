# Data Types

# to check an unknown data type use type()

#       String (str)

#Strings are defined by "".
# Any data within "" is a string.

print("This is a string")

#You can concatenate a string with +
#Strings can only concatinate with strings

print("My age is " + "28") # print("My age is " + 28) would not work because there is no "" around 28. This means it is an int, not a str

#if you want to include other data types into your string, you can use an f-string

#       F-String

#string starting with f and uses {}

print(f"My age is {28}")


#       Integer (int)

#Integers are whole numbers.

print(type(28))


#       Float (float)

#floats are numbers with decimals.

print(type(3.1415))

#       Boolean

#Boolean are either
True
#or
False