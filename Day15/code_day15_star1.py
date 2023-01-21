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

y_target_line = 2000000
reLine = re.compile('.*=(-?\d+).*=(-?\d+).*=(-?\d+).*=(-?\d+)')

ranges = []
for line in lista:
    data = [int(x) for x in reLine.match(line).groups()]
    dist = abs(data[0]-data[2]) + abs(data[1]-data[3])
    inc = dist - abs(y_target_line-data[1])
    if inc>0:
        ranges.append([data[0]-inc, data[0]+inc])
    #print(data, dist, inc, [data[0]-inc, data[0]+inc])
    
old_num = 0
new_num = len(ranges)
while old_num!=new_num and new_num>1:
    old_num = new_num
    ranges = join_ranges(ranges)
    new_num = len(ranges)

star1 = 0
for r in ranges:
    star1 += r[1]-r[0]
    
print('Star1: '+str(star1))

    

    
    