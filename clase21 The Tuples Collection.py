#tuple example
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])#Joseph

#the diference with list its that you cant alter a tuples element
#x[0] = 0#ERR0R

#YOU CANT USE .sort() .append() .reverse() on tuples
t = tuple()#starts an empty tuple
print(dir(t))#methods of tuples, count and index methods

#the advantage of tuples its they are more efficient in memory use and performance

(x, y) = (4, 'fred')
print(y)#fred
(a, b) = (99, 98)
print(a)#99

#in dictionarys the items() method returns a list of (key, value) tuples
d = dict()
d['a'] = 1
d['b'] = 2
tups = d.items()
print(tups)#[('a', 1), ('b', 2)]

#you can also compare tuples
#if the first item is equal, python goes to the second and so on until it finds one that differs
(0, 1, 2) < (5, 1, 2)#True
(0, 1, 20000000) < (0, 3, 4)#True
('Jones', 'Sally') < ('Jones', 'Sam')#True
#Jones = Jones
#S = S
#a = a
#l < m because a=1 b=2 l=11 m=12
('Jones', 'Sally') > ('Adams', 'Sam') #True
#the letters are evaluated