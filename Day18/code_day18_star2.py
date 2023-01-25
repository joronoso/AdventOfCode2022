f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

min_x = float('inf')
min_y = float('inf')
min_z = float('inf')
max_x = float('-inf')
max_y = float('-inf')
max_z = float('-inf')

lava = set()
for l in lista: 
    sq = eval('('+l+')')
    if sq[0]>max_x: max_x = sq[0]
    if sq[0]<min_x: min_x = sq[0]
    if sq[1]>max_y: max_y = sq[1]
    if sq[1]<min_y: min_y = sq[1]
    if sq[2]>max_z: max_z = sq[2]
    if sq[2]<min_z: min_z = sq[2]
    lava.add(sq)

last_batch = set()
for x in range(min_x-1, max_x+2):
    for y in range(min_y-1, max_y+2):
        for z in range(min_z-1, max_z+2):
            if x==min_x-1 or x==max_x+1 or y==min_y-1 or y==max_y+1 or z==min_z-1 or z==max_z+1:
                last_batch.add((x,y,z))
water = last_batch
while(len(last_batch)>0):
    new_batch = set()
    for sq in last_batch:
        if sq[0]+1<max_x: new_batch.add((sq[0]+1, sq[1], sq[2]))
        if sq[0]-1>min_x: new_batch.add((sq[0]-1, sq[1], sq[2]))
        if sq[1]+1<max_y: new_batch.add((sq[0], sq[1]+1, sq[2]))
        if sq[1]-1>min_y: new_batch.add((sq[0], sq[1]-1, sq[2]))
        if sq[2]+1<max_z: new_batch.add((sq[0], sq[1], sq[2]+1))
        if sq[2]-1>min_z: new_batch.add((sq[0], sq[1], sq[2]-1))
    new_batch = new_batch.difference(lava).difference(water)
    water.update(new_batch)
    last_batch = new_batch
    
faces = 0
for sq in lava:
    if (sq[0]+1, sq[1], sq[2]) in water: faces +=1
    if (sq[0]-1, sq[1], sq[2]) in water: faces +=1
    if (sq[0], sq[1]+1, sq[2]) in water: faces +=1
    if (sq[0], sq[1]-1, sq[2]) in water: faces +=1
    if (sq[0], sq[1], sq[2]+1) in water: faces +=1
    if (sq[0], sq[1], sq[2]-1) in water: faces +=1
    
print('Star 2: '+str(faces))

 