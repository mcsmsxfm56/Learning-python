#split breaks a string into parts and produces a list of strings
abc = 'With three words'
stuff = abc.split()
print(stuff)#['With', 'three', 'words']
print(len(stuff))#3
print(stuff[0])#With

#when you do not specify a delimiter, multiple spaces are treated like one delimiter
line = 'A lot                   of spaces'
etc = line.split()#['A', 'lot', 'of', 'spaces']

#you can specify a delimiter (;) in split
line = 'first;second;third'
thing = line.split()#['first;second;third']
secondthing = line.split(';')#['first', 'second', 'third']