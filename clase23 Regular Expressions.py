#regular expression quick guide
#^ matches the beginning of a line
#$ matches the end of a line
#. matches any character
#\s matches whitespace
#\S matches any non-whitespace character
#* repeats a character zero or more times
#*? repeats a character zero or more times (non-greedy)
#+ repeats a character one or more times
#+? repeats a character one or more times (non-greedy)
#[aeiou] matches a single character in the listed set
#[^XYZ] matches a single character not in the listed set
#[a-z0-9] the set of characters can include a range
#( indicates where string extraction is to start
#) indicates where string extraction is to end

#before you can use regular expressions in your program, you must import the library using "import re"
#you can use re.search() to see if a string matches a regular expression, similar to using the find() method for strings
#you can use re.findall() to extract portions of a string that match your regular expression, similar to a combination of find() and slicing: var[5:10]

#using re.search() like find()
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

#using re.search() like startswith()
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') >= 0:
        print(line)

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

#the dot character matches any character
#if you add the asterisk character, the character is "any number of times"

#X.*: 
#(X match the start of the line, . match any character * many times, : ends match)
#match all things that starts with X followed by any characters and ended with :
#(X-Sieve:) CMU Sieve 2.3 (matched)
#(X-DSPAM-Result:) Innocent (matched)
#(X-DSPAM-Confidence:) 0.8475 (matched)
#(X-Content-Type-Message-Body:) text/plain (matched)

#X-\S+:
#everything that starts with X-, That doesnt is a whitespace(\S), and match nonwhitespaces one or more times(+), match ends in :
#X-Sieve: CMU Sieve 2.3 (matched)
#X-DSPAM-Result: Innocent (matched)
#X-Plane is behind schedule: two weeks (no match)
