#we can create a new list by adding two existing lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)#[1, 2, 3, 4, 5, 6]
print(a)#[1, 2, 3]

#list can be sliced
a[0:2]

#you can use the dir command to see all the list methods
x = list()#creates a list, if no argument its passed creates []
print(type(x))#see type
print(dir(x))#append, count, extend, index, insert, pop, remove, reverse, sort

#creating a list fromt scratch
stuff = list()
stuff.append('book')#append add an item to the list
stuff.append(99)
print(stuff)
stuff.append('cookie')

#is something in a list?
some = [1, 9, 21, 10, 16]
9 in some#True
15 in some#False
20 not in some#True

#order list
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()#sort() orders alphabetically
#['Glenn', 'Joseph', 'Sally']

#built in functions in lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))#6
print(max(nums))#74
print(min(nums))#3
print(sum(nums))#154
print(sum(nums)/len(nums))#25.6
