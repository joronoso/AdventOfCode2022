f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

rocks = set()
max_y = 0
for line in lista:
    points = line.split(' -> ')
    p_from = tuple([int(x) for x in points[0].split(',')])
    for i in range(1,len(points)):
        p_to = tuple([int(x) for x in points[i].split(',')])
        if p_from[0]!=p_to[0]:
            for j in range(min(p_from[0], p_to[0]), max(p_from[0], p_to[0])+1):
                rocks.add((j, p_from[1]))
        else:
            for j in range(min(p_from[1], p_to[1]), max(p_from[1], p_to[1])+1):
                rocks.add((p_from[0], j))
                
        p_from = p_to
        
        if max_y < max(p_from[1], p_to[1]): max_y = max(p_from[1], p_to[1])

turns = 0
out = False
while not out:
    pos = (500,0)
    blocked = False
    while not blocked:
        possibilities = [(pos[0], pos[1]+1), (pos[0]-1, pos[1]+1), (pos[0]+1, pos[1]+1), (-1,-1)]
        for p in possibilities:
            if p==(-1,-1):
                blocked = True
            elif p not in rocks:
                pos = p
                break
        if pos[1]>max_y: 
            out = True
            blocked = True
    
    rocks.add(pos)
    turns += 1                         

print('Star 1: '+str(turns))