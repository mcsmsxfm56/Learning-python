def greet(lang):
    #lang its the parameter
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

def greet2():
    return "Hello"#return statement

def add(a, b):
    return a + b

print(add(5, 3))