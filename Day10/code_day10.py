f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

x_value = []
x = 1
for line in lista:
    x_value.append(x)
    if line[:4]=='addx':
        x_value.append(x)
        x += int(line.split()[1])
        
print('Star 1: '+str(20*x_value[19]+60*x_value[59]+100*x_value[99]+
                     140*x_value[139]+180*x_value[179]+220*x_value[219]))
print('Star 2:')
for j in range(6):
    line = ''
    for i in range(40):
        if abs(x_value[40*j+i]-i)<2:
            line += '#'
        else:
            line += '.'
    print(line)
    