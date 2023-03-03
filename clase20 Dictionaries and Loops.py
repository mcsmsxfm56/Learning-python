#you can convert the keys of a dictionary into a list
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))#['jan', 'chuck', 'fred']
#you can do the same with jjj.keys()
jjj.values()#[100, 1, 42]
jjj.items()#[('jan', 100), ('chuck', 1), ('fred', 42)]

#Iterate dictionarys with keys and values, aaa its the key, bbb its the value
jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb) #jan 100
    #chuck 1
    #fed 42