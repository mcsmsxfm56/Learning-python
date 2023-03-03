#Dictionary is a bag of values, each with its own label
#Dictionary are kinda like javascript objects
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)#['money': 12, 'tissues': 75, 'candy': 3]
print(purse['candy'])#3
purse['candy'] = purse['candy'] + 2#candy now is 5

#you can also make an empty dictionary with {}, like javacript
dictionary = {}