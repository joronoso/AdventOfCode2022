import re
from itertools import compress

def join_ranges(ranges):
    joined = []
    while len(ranges)>0:
        mask = [False]
        ran = ranges[0]
        for r in ranges[1:]:
            if (r[0]>=ran[0] and r[0]<=ran[1]) or (r[1]>=ran[0] and r[1]<=ran[1]) or (ran[0]>=r[0] and ran[0]<=r[1]):
                ran = [min(r[0], ran[0]), max(r[1], ran[1])]
                mask.append(False)
            else: 
                mask.append(True)
        joined.append(ran)
        ranges = list(compress(ranges, mask))
    return joined

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

reLine = re.compile('.*=(-?\d+).*=(-?\d+).*=(-?\d+).*=(-?\d+)')

lista2 = []
for line in lista:
    l = [int(x) for x in reLine.match(line).groups()]
    l.append(abs(l[0]-l[2]) + abs(l[1]-l[3]))
    lista2.append(l)

for y_target_line in range(4000001):
    ranges = []
    for data in lista2:
        inc = data[4] - abs(y_target_line-data[1])
        if inc>0:
            x = data[0]-inc
            if x<0: x=0
            y = data[0]+inc
            if y>4000000: y=4000000
            ranges.append([x, y])
        
    old_num = 0
    new_num = len(ranges)
    while old_num!=new_num and new_num>1:
        old_num = new_num
        ranges = join_ranges(ranges)
        new_num = len(ranges)

    star1 = 0
    for r in ranges:
        star1 += r[1]-r[0]
    
    if(star1!=4000000): break
    
x_coord = ranges[0][1]+1 if ranges[0][0]==0 else ranges[0][0] -1
print('Star2: '+str(y_target_line + 4000000*x_coord))
    
    