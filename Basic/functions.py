from math import * # importing math functions for numbers

# in-built functions in python for strings
phrase = "Kayode Oluwalusi"

print(phrase.lower()) # lower() converts a string to lowercase
print(phrase.upper()) # converts to uppercase
print(phrase.isupper()) # return a boolean if the string is in upper or lower case
print(phrase.upper().isupper()) # chaining functions
print(len(phrase)) # return the number of characters in the string
print(phrase[0]) # return the first character of the string
print(phrase.index("a")) # returns the index of the character
print(phrase.replace("Kayode", "Kayo")) # replaces a word or character with another

# in-built functions in python for numbers
my_num = -5

print(abs(my_num)) # abs() returns the absolute value of a number
print(pow(3, 2)) # pow() return the second power of 3
print(max(4, 6)) # max() returns the maximum value of two numbers
print(min(4, 6))  # min() returns the minimum value of two numbers
print(round(3.6)) # round() rounds the number up or down
print(floor(3.7)) # floor() rounds a number down no matter the decimal value
print(ceil(3.7)) # ceil() rounds a number up no matter the decimal value
print(int(5)) # int() converts a number to a whole integer
print(float(4.6)) # float() converts a number to decimal number