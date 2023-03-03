#we can use the in operator to see if a key its in the dictionary
ccc = {}
'key' in ccc#False

#the get method for dictionaries
#the pattern of checking to see if a key is already in a dictionary
#and assuming a default value if the key is not there
#is so common that there is a method called get()
#that does this for us
#default value if key does not exist (and no traceback)
counts = {}
name = 'zhen'
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)#in counts dictionary pick the key name, if name its not available assign it a default value, 0 in this case
