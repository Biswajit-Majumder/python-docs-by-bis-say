# python 


#  Python is a high level( high level languages are those languages that are easily understandable and readable for programmers and uses natural language construcs and abstructions to hide low level details ) , interpret ( that gets executed by interpreter means there is no compiler to complie the code before hence can be used to see results real time executes programme line by line ) , interactive () , object oriented , open sourced , general purpose programming language.



x = 10
y = 10


if (x is not y):
    print("x is not y")
else:
    print("x is y")


# It was created by Guido van Rossum, and released in 1991. 


#! Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.




#  Python is designed to be highly readable.
#  It uses English keywords frequently where as other languages use punctuation , and it has fewer syntactical constructions than other languages.
#  Python is a MUST for students and working professionals to become a great Software Engineer specially when they are working in Web Development Domain.

#  Python is a programming language that lets you work quickly and integrate systems more efficiently.
#  There are two major Python versions Python 2 and Python 3. Both are quite different.
#  Python 2.x is legacy , Python 3.x is the present and future of the language.
#  Python 3.0 was released in 2008. The final 2.x version 2.7 release came out in mid 2010 , with a statement of extended support for this end-of-life release.
#  Python 2.7 will not be maintained past 2020.
#  Python 3.0 was designed to be backwards incompatible , many projects have not yet made the switch , as it would involve rewriting tens of thousands of lines of code.
#  Python 3.0 makes breaking changes to the language , but many projects have been slow to port their code to the new version , or are prevented from doing so by their dependencies.

# Where do we use python ? 

# 1. Web Development : Python can be used to make web applications at many levels of complexity.
# 2. Game Development : Python is also used in development of interactive games.
# 3. Machine Learning and Artificial Intelligence : Python is widely used in AI , ML and Deep Learning.
# 4. Data Science and Data Visualization : Python is used to perform data analysis , create beautiful visualizations and perform machine learning.
# 5. Desktop GUI : Python is used to build desktop applications.
# 6. Web Scraping Applications : Python is used to build web scraping applications to extract data from websites.
# 7. Business Applications : Python is also used to build applications that do business related tasks.
# 8. Audio and Video Applications : Python is used to build applications that can read , write and play sound and videos.
# 9. Embedded Applications : Python is also used in embedded applications.
# 10. 3D CAD Applications : Python is also used in 3D CAD applications.




# python is a dynamically types language that ..... here answer dynamically typed vs static stype




# Go to python.org to download python

# what is precedence ------ > precedence is the condition of giving importance to someone over someone (the condition of being considered more important than someone or something else; priority in importance, order, or rank. definition -- google )

# now download a desired ide for code writting editing and manupulating

# now make a folder where you will keep you python files hirarchyly and it will keep your files clean

#  then make a file called programmehelloworld.py

#! notice that you have to write the .py extension after the python file it's a convention ( conventions are widely known or accepted standars, practices or rules that are follewed in a pratical field or groud of people or community or )

# Python Indentation

# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

# first write this instruction into your text editor 

print("Hello, World!")  

# as we made our hello world programme let's write a little comment to make it more memorable 

# so what is a comment 

# In programming, a comment is a piece of text that is added to the source code of a program to provide additional information or to explain the purpose of the code. Comments are ignored by the compiler or interpreter, so they do not affect the behavior of the program.

# now write the smallest expression 
# 2 + 2 


# Warning!
# An “octothorpe” is also called a “pound”, “hash”, “mesh”, or any number of names. Pick the one that makes you chill out.


# why python is popular 

# 1 for it's design philosophy ( readability , well indented )
# 2 batteries included <fun turm> ( many function are already there to do the tasks smoothly we don't have to re-invent the wheel they are abstructed away by python inbuilt  --- )

# 3 free and open source ( python is free and open source and it's community is very large and active )

# 4 portability ( python is portable means it can be run on any platform like windows , linux , mac , raspberry pi etc. )

# 5 general purpose ( supports many programming paradigms we can make many things )



# python is case sensitive


# now let's understand what we are doing here 
# we are using a function called print() to print something on the screen
# print() is a function that takes a string as an argument and prints it on the screen
# a string is a sequence of characters enclosed in single or double quotes
# print() is a built-in function in python
# a function is a block of code that performs a specific task
# print() is a function that prints a string on the screen


# ok now lets learn python variables 
# question number one 
# make a programme that swap two values

# so to tackle this question we have to have 2 values lets assume one is 69 and another is 420 ...
# now the question is how we are going to identify and access this values ... to solve this problem we have variable 
# we can store values inside a varirable and use modify in whatever way we want

# so what is a variable ?



# to make a veriable we have to give it a name and we will give it a value
# python is case sensitive  keep in that mind

variable_name = "value"

variable_name

# the things  "value" 





example_value_1 = 69
example_value_2 = 420

# we made two variables example_variable_1 and example_variable_2 and gave them 69 and 420 values respectivly ..... now we can swap them very easily 

# there are many ways to do this problem but we are going to see only 2 of them on is with a third variable and another is arithmetically 
# 
# lets make a third variable to store any on of the value 
temp_swapping_var = example_value_1
# now change the value of a variable
example_value_1 = example_value_2
# then get the value from the temp vairable to the second variable
example_value_2 = example_value_1
#  


# now lets do it in another way
# we can do in in using arithmetic operations 

# first we have to add the two values and store it in the first variable
example_value_1 = example_value_1 + example_value_2
# now we have to subtract the second value from the first value and store it in the second variable
example_value_2 = example_value_1 - example_value_2
# now we have to subtract the second value from the first value and store it in the first variable
example_value_1 = example_value_1 - example_value_2


print("The changed value is a =", example_value_1, "b =", example_value_2)

# Python is completely object oriented, and not "statically typed".
# You do not need to declare variables before using them, or declare
# their type. Every variable in Python is an object.

# Unlike other programming languages, Python has no command for
# declaring a variable. A variable is created the moment you first assign
# a value to it.

# A variable can have a short name (like x and y) or a more descriptive name
# (age, carname, total_volume).

# Rules for Python variables:
# - A variable name must start with a letter or the underscore character.
# - A variable name cannot start with a number.
# - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# - Variable names are case-sensitive (age, Age and AGE are three different variables).
# """

#

_aaraia_1 = 1



# Python Numbers
# There are three numeric types in Python:
# - Integers
# - Floating point numbers
# - Complex numbers
# - string / text

# Variables of numeric types are created when you assign a value to them:


# - Integers: 
x = 5
# - Floats: 
x = 5.0
# - Complex: 
x = 1j
# """



# Python Casting

# Specify a Variable Type
# There may be times when you want to specify a type on to a variable.
# This can be done with casting. Python is an object-orientated language,
# and as such it uses classes to define data types, including its primitive types.


# Casting in python is therefore done using constructor functions:
# - int(x)
# - float(x)
# - str(x)


# Python Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# """

# You can display a string literal with the print() function:
# print("Hello")
# now let's talk about the print funtion.... ok now you can have a question that what is this function ? 

# so in simple terms function is a block of code that performs specific task
# the python print is a king of function that prints the desired output for us it can be string litrals , any variable, any numeric value or any anything 
# keep in that mind in print function if we put something between double quote ("Somethng-can-be-anything") then it will print as it is.
# but if we put something without double quote then it will try to find a variable with that name and print it's value
# for example
# print("Hello") # it will print Hello
# print(Hello) # it will try to find a variable named Hello and print it's value

# python print funciton is really powerful it can print many things together and the level of flexibility is also astonishing 
# for example
# print("Hello", "World") # it will print Hello World and there is  a ' ' separator between every object it is given by the python function and it changes the to new line when at the of the print we can put any thing between



# Multiline Strings

# You can assign a multiline string to a variable by using three quotes:
# """
# You can use three double quotes:
# """
# or three single quotes:
# '''
# """

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
# a = "Hello, World!"
# print(a[1])


# to check the data type we use type function 

# example 
# var1 = 13221
# print(type(var1)) // it will show integer 


# assigning multiple variables 
var1, var2, var3 = "value1", "value2", "value3"

# we can also assign same value to multiple variables
var1 = var2 = var3 = "value"

# we can also assign multiple values to multiple variables
cities = ["Kolkata", "London", "Las Vegas"]

first_city , second_city , third_city = cities

print(f"First we will visit {first_city}, then {second_city}, {third_city}")


#! conditions


# let's understand operators in python 

# there are many types of operators in python
# 1. Arithmetic operators
# 2. Assignment operators
# 3. Comparison operators
# 4. Logical operators
# 5. Identity operators

# 6. Membership operators
# 7. Bitwise operators
# 8. Augmented assignment operators
# 9. Special operators

# 1. Arithmetic operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
# Here are the arithmetic operators in python
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# / /	Float division	x // y
x = 10 
y = 100
# 5 % 2 -> 1
print(x // y )

5 ** 2  


# 2. Assignment operators
# Assignment operators are used to assign values to the variables.
# Here are the assignment operators in python
# =	x = 5	x = 5
x += 5 ;	x = x + 5
# -=	x -= 5	x = x - 5
# *=	x *= 5	x = x * 5
# /=	x /= 5	x = x / 5
# %=	x %= 5	x = x % 5


# / /=	x //= 5	x = x // 5
# **=	x **= 5	x = x ** 5




# not much used assignment operators
# &=	x &= 5	x = x & 5
# |=	x |= 5	x = x | 5
# ^=	x ^= 5	x = x ^ 5
# >>=	x >>= 5	x = x >> 5
# <<=	x <<= 5	x = x << 5



# 3. Comparison operators
# Comparison operators are used to compare two values.
# Here are the comparison operators in python
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y




# 4. Logical operators
# Logical operators are used to combine conditional statements.
# Here are the logical operators in python
# and	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


newVar = 0



# while not False:
#     print("Hello")
#     newVar += 1
#     if newVar is 100:
#         newVar = "Hello"
#         if newVar is "Hello":
#             break


condition1 = True
condition2 = False
not condition1   #False
condition1 and condition2 #False
condition1 or condition2 #True







# 5. Identity operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# Here are the identity operators in python
# is	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]   #  object   1
y = ["apple", "banana"]   #  object   2

print( " are they same " ,x is not y)


print( False and True)


# x is y	x is y
# x is not y	x is not y
# x is y	x is y
# x is not y	x is not y
# x is y	x is y
# x is not y	x is not y



# 6. Membership operators
# Membership operators are used to test if a sequence is presented in an object.
# Here are the membership operators in python
# in	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# x in y	x in y
# x not in y	x not in y
# x in y	x in y 
# x not in y	x not in y
# x in y	x in y
# x not in y	x not in y
# x in y	x in y
# x not in y	x not in y
# x in y	x in y
# x not in y	x not in y
# x in y	x in y
# x not in y	x not in y
# x in y	x in y
# x not in y	x not in y

# 7. Bitwise operators
# Bitwise operators are used to compare (binary) numbers:
# Here are the bitwise operators in python
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
# x & y	x & y
# x | y	x | y
# x ^ y	x ^ y
# ~x	~x
# x << y	x << y
# x >> y	x >> y
# x & y	x & y
# x | y	x | y
# x ^ y	x ^ y
# ~x	~x


# 8. Operator precedence
# Operator precedence describes the order in which operations are performed in an arithmetic expression.
# Here are the operator precedence in python
# Operator	Description	Example
# ()	Parentheses	(3 + 2) * 6
# **	Exponentiation	2 ** 3
# +x, -x, ~x	Unary plus, Unary minus, Bitwise NOT	+x, -x, ~x
# *, /, //, %	Multiplication, Division, Floor division, Modulus	2 * 3 / 4
# +, -	Addition, Subtraction	2 + 3 - 4
# <<, >>	Bitwise shift operators	2 << 3
# &	Bitwise AND	2 & 3
# ^	Bitwise XOR	2 ^ 3
# |	Bitwise OR	2 | 3
# ==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators	2 == 3




# ! type convertion does not change the real thing it returns a new object
x = 21


def string_to_int_conv(obj):
    return int(obj)



newVAr = int(x)

print(type(x))

# how in and not in operators in python work?


# now lets learn about the modules 
# so whar are modules 
# modules are the python files that contain python code that have been written by other peoples so that we can use them and we don't have to make those things from scratch
# we can import modules in our python code and use them
# we can also create our own modules and use them in our code


# it helps us and saves a lot of time. And that's why we use python 

# so how to import modules in python
# we use import keyword to import modules in python

# import math



import random
# help('modules') 



# print(random.randint(2, 100))


# print(random.randint(1, 100),random.randint(1, 19))


# make a funciton that adds two int number 


def adder( ram , jadu ): # parameter neoya byabsa
    return ram + jadu
    


adder( 2 , 9 ) # arguments  deoya byabsa





# Now let's start loops 


# What is loop
# A loop is a sequence of instructions that is continually repeated until a certain condition is reached.
# Loops are used to repeat a block of code.



# where do we use loops
# we use loops when we want to repeat a block of code
# let's try to write a loop in python
# there are two types of loop in python 
# 1. for loop
# 2. while loop



# first lets check while loop 


# while 
# As the name suggest we will run something while the condition us beging full-filled 
# and when the condition will not meet at that time the while loop while stop 

# lets take an example 

# you have a cart and there are some thing 

# we want to print table of any number 


# number = int( input("Enter any number here") )

# i = 1

# while i <= 10:
#     print( f"{number} * {i} =", number * i)
#     i += 1 





# for loop
# for loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# the for loop is different than other language for loop and it's really powerful ... 





# for i in range(1,11): # internally it is like this for i in 1,2,3,4,5,6,7,8,9,10
#     print(i)

# the range(1,11)  the first is included and the second on is excluded





# the current population of Mathur is 1000 people. And it is increasing 10% every year 