#we can take advantage of the ability to sort a list of tuples
#to get a sorted version of a dictionary
#first we sort the dictionary by the key using the items() method
#and sorted() function
d = {'a': 10, 'b': 1, 'c': 22}
d.items()#[('a', 10), ('c', 22), ('b', 1)]
sorted(d.items())#[('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)

#if we could construct a list of tuples
#of the form (value, key) we could sort by value
#we do this with a for loop that creates a list of tuples
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#even shorted version
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
