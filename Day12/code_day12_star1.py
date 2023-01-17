import numpy as np

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

start=None
end=None
heights = []
for iline, line in enumerate(lista):
    h_line = []
    for ic, c in enumerate(line):
        if c=='S':
            start = (iline, ic)
            c='a'
        elif c=='E':
            end = (iline, ic)
            c='z'
        h_line.append(ord(c)-ord('a'))
    heights.append(h_line)
    
path = np.zeros((len(heights), len(heights[0])), dtype=int)-1
path[start[0], start[1]] = 0

current_calc = [ start ]

star1 = None
step = 0
while(star1 is None):
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
            if path[a[0]][a[1]]==-1 and heights[a[0]][a[1]]-curr_height<=1:
                new_current_calc.add(a)
                path[a[0]][a[1]]=step
                if a==end:
                    star1 = step
                    break
    current_calc = new_current_calc
    
print('Star 1: '+str(star1))
        


