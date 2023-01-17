import numpy as np

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

start=None
heights = []
for iline, line in enumerate(lista):
    h_line = []
    for ic, c in enumerate(line):
        if c=='S':
            c='a'
        elif c=='E':
            start = (iline, ic)
            c='z'
        h_line.append(ord(c)-ord('a'))
    heights.append(h_line)
    
path = np.zeros((len(heights), len(heights[0])), dtype=int)-1
path[start[0], start[1]] = 0

current_calc = [ start ]

star2 = None
step = 0
while(star2 is None):
    step += 1
    new_current_calc = set()
    
    for curr in current_calc:
        curr_height = heights[curr[0]][curr[1]]
        around = []
        if curr[0]>0: around.append((curr[0]-1, curr[1]))
        if curr[1]>0: around.append((curr[0], curr[1]-1))
        if curr[0]<path.shape[0]-1: around.append((curr[0]+1, curr[1]))
        if curr[1]<path.shape[1]-1: around.append((curr[0], curr[1]+1))
        for a in around:
            if path[a[0]][a[1]]==-1 and curr_height-heights[a[0]][a[1]]<=1:
                new_current_calc.add(a)
                path[a[0]][a[1]]=step
                if heights[a[0]][a[1]]==0:
                    star2 = step
                    break
    current_calc = new_current_calc
    
print('Star 2: '+str(star2))
        


