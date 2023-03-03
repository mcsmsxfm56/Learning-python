#open() function opens files
#open() returns a "file handle", a variable used to perform operations on the file
#handle = open(filename, mode)
#with handle variable you can manipulate the file
#filename is a string
#mode is optional and should be r if we are planning to read the file and w if you want to write it
try:
    fhand = open('mbox.txt', 'r')
    print(fhand)
#options for open() are open,read,write and close

#fhand = open('mbox.txt)
#print(fhand)
#<_io.TextIOWrapper name='mbox.txt' mode='r' encoding='UTF-8'>

#if the file you want to open doesnt exist python returns an error

#\n in python means new line
except:
    stuff = 'Hello \nWorld!'
    #Hello
    #World!
    print(stuff)