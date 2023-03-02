# Math symbols
#+ addition
#- subtraction
#* multiplication
#/ division
#** power
#% remainder
x = 1 + 2 * 3 - 4 / 5 ** 6
#which order of evaluation follows python?
#1
#2 * 3 = 6
#5 ** 6 = 15625
#4 / 15625 = 0,000256
#1 + 6 + 0,000256 = 7,000256

#operator precedence rules
#1)parenthesis
#2)power
#3)multiplication
#4)addition
#5)left to right
#its good practice to use parentheses and keep math expressions simple

#types
#+ means addition for numbers and concatenate for strings
#y = "hello" + 1
#you cannot add 1 to a string, it returns an error
#if an error its return line 29 and 30 wont execute so i commented out
print(type(1))#returns <class 'int'>, saying that 1 its a type integer
print(type('hello'))#return <class 'str'> type string
#0.96 <class 'float'>
#when you put an integer and a float the integer implicitly converts to float
#you can control this with the built-in functions int() and float()
print(float(99) + 100)
#integer division produces floating results
print(10 / 2)#5.0

#you can also do string conversions in python
string = '123'
string = int(string)
#now its an integer, one hundred and twenty three
string2 = 'Hello world'
#string2 = int(string2) returns an error because hello world doesnt have a number
name = input('Who are you?')
#input allows the user to, in this case, write the content of the variable name
#input() its a function that allows to read data from the user
print('Welcome', name)
#if you want to read a number from the user you must convert it (because input() only returns strings)
inp = input('Europe floor?')#0
usf = int(inp) + 1#1
print('US floor', usf)#1
#European elevators start at 0, US elevator starts at 1, this code converts european floors to US floors