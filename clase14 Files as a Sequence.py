xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
#a file handle open for read can be treated as a sequence of strings
#where each line in the file is a string in the sequence
#we can use the for statement to iterate to a text file
#cheese represent each line of mbox.txt

#counting number of lines of mbox.txt
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

#we can read the whole file into a single string
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))#length of the string inp
print(inp[:20])

#we can put an if statement in our for loop to only print lines that meet some criteria
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('Testing'):
        print(line)
#printing this gives you blank lines(empty lines)
#this problem occurs becase the text haves \n but at the end of every print
#statement closes with \n
#Testing Reading In python \n in txt file
#\n added by print
#Testing Reading In python 2\n in txt file
#\n added by print
#Testing Reading In python 3\n in txt file

#searching through file fixed
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()#this removes the \n of the txt file
    if line.startswith('Testing'):
        print(line)

#skipping a line with continue
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Testing'):
        continue
    print(line)


#ask the user for a filename
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()#quit stops execution here because otherwise the next lines will be executed and the program will crash
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

