def addition(x, y):
   k =  x + y 
   return k 
   
def mulit(x, y):
   k = x * y 
   return k 
   
print(addition(1, 5))
print(mulit(5, 50))


print("Hello Goods")

name = "Goods yarn"

first_name = name[0:7]

print(first_name)

import math

def hypotenuse(a, b):

    result = math.sqrt(a**2 + b**2)
    return result

a = float(input("Enter a: "))
b = float(input("Enter b: "))

result = hypotenuse(a, b)

print(f"{result:.2f}")


def main():
    amount = int(input("Enter cash amount: "))
    print(f"I'm giving you P{givegift(amount)}")

def givegift(x):
    g = 200 if x % 2 == 1 else 100
    return x * 3 + g

main()

def compare(num1, num2, num3):

     return max(num1, num2, num3)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

greatest_value = compare(num1, num2, num3)

print(f"Greatest: {greatest_value}")

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print(f"Returned value from function = {findDistinctnumber(a, b, c)}")

def findDistinctnumber(a, b, c):
    if a == b == c:
        return a
    elif a !=b and b == c:
        return a
    elif b != a and a == c:
        return a
    elif c != a and a == b:
        return c
    else:
        return -999

main()

def main():
    size = int(input("Enter the size of the array: "))
    print("Enter the strings separated by enter: ")
    array = []
    for x in range(size):
        array.append(input().lower())
    print(f"Longest common prefix: {longest(array)}")

def longest(words):
    if not words:
        return ""

    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

main()

def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print("Reversed string:", result)


n = 0
sales = 0
while True:
    n = int(input("Enter value: "))
    if n == -1:
        break
    sales += n
    if sales >= 2000:
        break
    elif sales > 1499:
        print("You're almost there!")
    elif sales > 999:
        print("You're half throught!")
    elif sales > 499:
        print("You're off to a good start!")
if sales < 2000:
    print(f"Program was terminated. Your total sales are: {sales}")
else:
    print(f"Congratulations! Your total sales are: {sales}")
    
print("Hello World!")

name = 

print(type(name))  



def colors(choice):
    if choice == 'Y':
        print("Yellow")
    elif choice == 'R':
        print("Red")
    elif choice == 'B':
        print("Blue")
    else:
        print("No colors")
    return
choice = input("The colors you want (Y,R,B): ")

result = colors(choice)

print(result)
    
    
rows = int(input("Enter the rows: "))
space = int(input("Enter the space: ")) 
symbol = input("Enter a symbol: ") 
for i in range(rows):
    for j in range(space):   
        print(symbol, end=" ")
    print()
    
    
string = 'hello' 

print(string.lower())
    
import re
input = "Hello, World!"
pattern = r"hello"
	
is_match = re.search(pattern, input, re.IGNORECASE)
	
print(is_match)


import re
	
input = "apple"
pattern = r"[aeiou]+"
	
match = re.search(pattern, input)
	
print(match.group())


import re
	
input = "apple, orange, banana"
pattern = r"(\w+), (\w+), (\w+)"
	
match = re.search(pattern, input)
	
print(match.group(2))


import re

# Ask the user to input a string
user_input = input("Enter a string: ")

# Use regex to check if the string contains a digit
if re.search(r'\d', user_input):
    print("Found a digit!")
else:
    print("No digit found.")
    
import re

# Ask the user to input a string
user_input = input("Enter a string: ")

# Use regex to check if the string contains a capital letter
if re.search(r'[A-Z]', user_input):
    print("Found a capital letter!")
else:
    print("No capital letter found.")
