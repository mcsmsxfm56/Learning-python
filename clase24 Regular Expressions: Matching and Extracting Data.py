#re.search() returns True/False depending on whether the string matches the regular expression
#if we actually want the matching strings to be extracted, we use re.findall()
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)#match all characters between 0-9 and + indicates that take more
#than one character (so instead of 2 1 9 4 2 with + returns 2 19 42)
print(y)#['2', '19', '42']

#warning: greedy matching
#the repeat characters (* and +) push outward in both directions(greedy)
#to match the arget possible string
import re
x = 'From: Using the : character'
y = re.findall('^F.+', x)
print(y)#['From: Using the :']
#because is greedy instead of From:, matched all the way until Using the :"

#Non-Greedy matching
#Not all expression repeat codes are greedy!
#if you add a ? character, the + and * chill out a bit
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)#['From:']
#+? one or more characters but not greedy

x = 'From stephen.marquard@uct.ac.za'
y = re.findall('\S+@\S+', x)
y = re.findall('^From (\S+@\S+)',x)
print(y)#['stephen.marquard@uct.ac.za'], doesnt match from because with the parentesios we indicate that only returns
#what matches with the regexp, so only return \S+@\S+
