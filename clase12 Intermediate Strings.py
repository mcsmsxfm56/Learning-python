s = 'Monty Python'
print(s[0:4])#Mont [0-4)
print(s[6:7])#P [6-7)
print(s[6:20])#Python
print(s[:2])#Mo
print(s[8:])#thon
print(s[:])#Monty Python

#in its useful to check things
fruit = 'banana'
'n' in fruit#True
'm' in fruit
if 'a' in fruit:
    print('Found it!')

#methods of strings
greet = 'Hello Bob'
zap = greet.lower()
print(zap)#hello bob

#str.capitalize()
#str.center(width[, fillchar])

#str.endswith(suffix[, start[, end]])
#str.startswith(suffix[, start[, end]])
line = 'Please have a nice day'
line.startswith('Please')#returns True
line.startswith('p')#returns False

#str.find(sub[, start[, end]])
fruit = 'banana'
pos = fruit.find('na')
print(pos)#2, finds the first ocurrence of the string, in this case index 2
aa = fruit.find('z')
print(aa)#-1, find returns -1 when doesnt find anything

#str.lstrip([chars])
greet = '       Hello Bob             '
greet.lstrip()#'Hello Bob             '

#str.replace(old, new[, count])
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)#Hello Jane
nstr = greet.replace('o', 'X')
print(nstr)#HellX BXb

#str.lower() todo minuscula

#str.rstrip([chars]) removes whitespace from right
greet = '       Hello Bob             '
greet.rstrip()#'       Hello Bob'

#str.strip([chars])
greet = '       Hello Bob             '
greet.strip()#'Hello Bob'

#str.upper() makes all letters uppercase