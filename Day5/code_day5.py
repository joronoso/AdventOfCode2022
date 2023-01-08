import re
import copy

stacks = [ ['S','M','R','N','W','J','V','T'],
           ['B','W','D','J','Q','P','C','V'],
           ['B','J','F','H','D','R','P'],
           ['F','R','P','B','M','N','D'],
           ['H','V','R','P','T','B'],
           ['C','B','P','T'],
           ['B','J','R','P','L'],
           ['N','C','S','L','T','Z','B','W'],
           ['L','S','G'] ]

stacks2 = copy.deepcopy(stacks)
    
re_rule = re.compile('move (\d+) from (\d+) to (\d+)')

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

for line in lista:
    grs = re_rule.match(line).groups()
    
    # Star 1 movement
    for i in range(int(grs[0])):
        stacks[int(grs[2])-1].append( stacks[int(grs[1])-1].pop() )
    
    # Star 2 movement
    stacks2[int(grs[2])-1].extend( stacks2[int(grs[1])-1][-int(grs[0]):] )
    del stacks2[int(grs[1])-1][-int(grs[0]):]

print('Star 1: ', end = '')
for i in stacks: print(i[-1],end = '')

print('\nStar 2: ', end = '')
for i in stacks2: print(i[-1],end = '')