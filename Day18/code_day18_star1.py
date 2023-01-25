f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

lava = set()
for l in lista: lava.add(eval('('+l+')'))
faces = 0
for sq in lava:
    if (sq[0]+1, sq[1], sq[2]) not in lava: faces +=1
    if (sq[0]-1, sq[1], sq[2]) not in lava: faces +=1
    if (sq[0], sq[1]+1, sq[2]) not in lava: faces +=1
    if (sq[0], sq[1]-1, sq[2]) not in lava: faces +=1
    if (sq[0], sq[1], sq[2]+1) not in lava: faces +=1
    if (sq[0], sq[1], sq[2]-1) not in lava: faces +=1
    
print('Star 1: '+str(faces))
 