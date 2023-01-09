f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

def calculatePositions(num_knots):
    visited = set()
    positions = [(0,0)]*num_knots
    visited.add(positions[-1])
    for line in lista:
        direction, steps = line.split(' ')
        for i in range(int(steps)):
            new_positions = positions.copy()
            if direction=='U': 
                new_positions[0] = (positions[0][0], positions[0][1] + 1)
            elif direction=='D':    
                new_positions[0] = (positions[0][0], positions[0][1] - 1)
            elif direction=='R':
                new_positions[0] = (positions[0][0] + 1, positions[0][1])
            else: # Left
                new_positions[0] = (positions[0][0] - 1, positions[0][1])
        
            for knot in range(1, num_knots):
                if abs(new_positions[knot][0]-new_positions[knot-1][0])>1 or abs(new_positions[knot][1]-new_positions[knot-1][1])>1: 
                    if new_positions[knot][0]==new_positions[knot-1][0]:
                        new_x = new_positions[knot][0]
                    elif new_positions[knot][0]>new_positions[knot-1][0]:
                        new_x = new_positions[knot][0] - 1
                    else:
                        new_x = new_positions[knot][0] + 1
                    
                    if new_positions[knot][1]==new_positions[knot-1][1]:
                        new_y = new_positions[knot][1]
                    elif new_positions[knot][1]>new_positions[knot-1][1]:
                        new_y = new_positions[knot][1] - 1
                    else:
                        new_y = new_positions[knot][1] + 1
                        
                    new_positions[knot] = (new_x, new_y)
            
            positions = new_positions
            visited.add(positions[-1])
    return len(visited)

print('Star 1: '+str(calculatePositions(2)))
print('Star 2: '+str(calculatePositions(10)))

