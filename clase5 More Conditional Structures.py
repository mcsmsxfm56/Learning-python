# else if in python is elif
x = 9
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("large")##solo corre cuando elif da false
print("all done")

# No Else
x = 5
if x < 2:
    print('Small')
elif x < 10:
    print("medium")
print("All done")
# if x = 50 small and medium wouldnt be printed because theres no else, else run when the upper conditions are false

x = 10
if x < 2:
    print("Small")#if x < 2 runs Small and stops
elif x < 10:
    print("Medium")#if x < 10 runs Medium and stops
elif x < 20:
    print("Big")#if x < 20 runs Big and stops
elif x < 40:
    print("Large")#if x < 40 runs Large and stops
elif x < 100:
    print("Huge")#if x < 100 runs Huge and stops
else:
    print("Ginormous")#if all conditions of upside returns false runs Ginormous


#try/except structure
#if the code in try works the except its skipped
#if the code in try fails it jumps to except
## astr = "Hello bob"
## istr = int(astr)
#here detects an error and the code below doesnt run
## print('First', istr)
## astr = '123'
## istr = int(astr)
## print('Second', istr)

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# Executes
# Hello
# Done -1
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')#Never prints
except:
    istr = -1
print('Done', istr)

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')