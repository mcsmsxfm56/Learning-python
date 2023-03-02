# while loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

while True:
    line = input('> ')
    if line == 'done':
        break#stops the loop execution
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':#if the first element of the string is # jump to next iteration and doesnt print
        continue#jumps to next iteration
    if line == "done":
        break
    print(line)
print('Done!')