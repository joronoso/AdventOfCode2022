f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

lista[0:-2]
instructions = []
i=0

face_coords = [(50,0), (100,0), (50,50), (0,100), (50,100), (0,150)]

# New face, transf_x, transf_y, new direction
transf_rules = [ [ [ 1, lambda x,y:0, lambda x,y:y, 0], # From 0, right
                   [ 2, lambda x,y:x, lambda x,y:0, 1], # From 0, down
                   [ 3, lambda x,y:0, lambda x,y:49-y, 0],
                   [ 5, lambda x,y:0, lambda x,y:x, 0] ],
                 [ [ 4, lambda x,y:49, lambda x,y:49-y, 2], # From 1, right
                   [ 2, lambda x,y:49, lambda x,y:x, 2],
                   [ 0, lambda x,y:49, lambda x,y:y, 2], # From 1, left
                   [ 5, lambda x,y:x, lambda x,y:49, 3] ],
                 [ [ 1, lambda x,y:y, lambda x,y:49, 3],
                   [ 4, lambda x,y:x, lambda x,y:0, 1], # From 2, down
                   [ 3, lambda x,y:y, lambda x,y:0, 1],
                   [ 0, lambda x,y:x, lambda x,y:49, 3] ],
                 [ [ 4, lambda x,y:0, lambda x,y:y, 0], # From 3, right
                   [ 5, lambda x,y:x, lambda x,y:0, 1],
                   [ 0, lambda x,y:0, lambda x,y:49-y, 0],
                   [ 2, lambda x,y:0, lambda x,y:x, 0] ],
                 [ [ 1, lambda x,y:49, lambda x,y:49-y, 2], # From 4, right
                   [ 5, lambda x,y:49, lambda x,y:x, 2],
                   [ 3, lambda x,y:49, lambda x,y:y, 2],
                   [ 2, lambda x,y:x, lambda x,y:49, 3] ],
                 [ [ 4, lambda x,y:y, lambda x,y:49, 3],
                   [ 1, lambda x,y:x, lambda x,y:0, 1],
                   [ 0, lambda x,y:y, lambda x,y:0, 1],
                   [ 3, lambda x,y:x, lambda x,y:49, 3] ] ]
                       
faces = []
for f in face_coords:
    face = []
    for j in range(f[1], f[1]+50):
        face.append(lista[j][f[0]:f[0]+50])
    faces.append(face)

while i <len(lista[-1]):
    if lista[-1][i]=='L':
        instructions.append('L')
        i+=1
    elif lista[-1][i]=='R':
        instructions.append('R')
        i+=1
    else:
        o=i
        while i<len(lista[-1]) and lista[-1][i] not in 'LR':
            i+=1
        instructions.append(lista[-1][o:i])

face = 0        
y = 0
x = 0
fac = 0 # 0=right, 1=down, 2=left, 3=up

for ins in instructions:
    if ins == 'R': fac = (fac+1)%4
    elif ins == 'L': fac = (fac-1)%4
    else:
        num = int(ins)
        for xo in range(num):
            new_x = x
            new_y = y
            new_face = face
            new_fac = fac
            
            if fac==0: new_x = x+1
            elif fac==1: new_y = y+1
            elif fac==2: new_x = x-1
            else: new_y = y-1
            
            if max(new_x, new_y)>49 or min(new_x, new_y)<0:
                new_face = transf_rules[face][fac][0]
                new_x = transf_rules[face][fac][1](x,y)
                new_y = transf_rules[face][fac][2](x,y)
                new_fac = transf_rules[face][fac][3]
            
            if faces[new_face][new_y][new_x] == '#': 
                break
            else:
                x = new_x
                y = new_y
                fac = new_fac
                face = new_face
        
print('Star 2:',1000*(y+1+face_coords[face][1])+4*(x+1+face_coords[face][0])+fac)
