f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

board = lista[0:-2]
instructions = []
i=0

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

colsizes = []
for i in range(len(board[0])):
    if board[0][i]!=' ':
        min_y = 0
    else: 
        for j in range(1,len(board)):
            if board[j][i]!=' ': 
                min_y = j
                break
    for j in range(min_y+1,len(board)):
        if len(board[j])<i+1:
            max_y = j-1
            break
        else:
            max_y = len(board)-1
    colsizes.append((min_y, max_y))

rowsizes = []
for i in range(len(board)):
    if board[i][0]!=' ':
        min_x = 0
    else:
        for j in range(len(board[i])):
            if board[i][j]!=' ':
                min_x = j
                break
    rowsizes.append((min_x, len(board[i])-1))
        
y = 0
x = board[0].index('.')
fac = 0 # 0=right, 1=down, 2=left, 3=up

for ins in instructions:
    if ins == 'R': fac = (fac+1)%4
    elif ins == 'L': fac = (fac-1)%4
    else:
        num = int(ins)
        if fac == 0: # Right
            for i in range(num):
                new_x = x+1 
                if new_x>rowsizes[y][1]: new_x = rowsizes[y][0]
                if board[y][new_x]=='#': break
                else: x = new_x
        elif fac == 2:
            for i in range(num):
                new_x = x-1
                if new_x<rowsizes[y][0]: new_x = rowsizes[y][1]
                if board[y][new_x]=='#': break
                else: x = new_x
        elif fac == 1: #Down
            for i in range(num):
                new_y = y+1
                if new_y>colsizes[x][1]: new_y = colsizes[x][0]
                if board[new_y][x]=='#': break
                else: y = new_y
        else: # Up
            for i in range(num):
                new_y = y-1
                if new_y<colsizes[x][0]: new_y = colsizes[x][1]
                if board[new_y][x]=='#': break
                else: y = new_y
        
print('Star 1:',1000*(y+1)+4*(x+1)+fac)
