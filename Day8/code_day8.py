import numpy

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

matrix = None
for line in lista:
    m = numpy.array([int(item) for item in line], ndmin=2)
    if matrix is None:
        matrix = m
    else:
        matrix = numpy.concatenate((matrix, m))
        
visible = 2*(matrix.shape[0] + matrix.shape[1] - 2)
max_scenic = 0
for i in range(1, matrix.shape[0]-1):
    for j in range(1,matrix.shape[1]-1):
        if ( matrix[i,j]>matrix[i,0:j].max() or 
             matrix[i,j]>matrix[i,j+1:].max() or
             matrix[i,j]>matrix[0:i,j].max() or
             matrix[i,j]>matrix[i+1:,j].max() ):
            visible += 1
        
        # Calculate scenic score
        up = 0
        for k in range(i-1, -1, -1):
            up +=1
            if matrix[k,j]>=matrix[i,j]:
                break
        down = 0
        for k in range(i+1, matrix.shape[0]):
            down += 1
            if matrix[k,j]>=matrix[i,j]:
                break
        left = 0
        for k in range(j-1, -1, -1):
            left += 1
            if matrix[i,k]>=matrix[i,j]:
                break
        right = 0
        for k in range(j+1, matrix.shape[1]):
            right += 1
            if matrix[i,k]>=matrix[i,j]:
                break
        sc = up * down * right * left

        if sc > max_scenic:
            max_scenic = sc
             
             
print('Star 1: '+str(visible))
print('Star 2: '+str(max_scenic))