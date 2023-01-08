f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

total = 0
total2 = 0
for line in lista:
    r = line.split(',')
    r0 = r[0].split('-')
    r1 = r[1].split('-')
    if (int(r0[0])<=int(r1[0]) and int(r0[1])>=int(r1[1])) or (int(r0[0])>=int(r1[0]) and int(r0[1])<=int(r1[1])):
        total = total + 1
        total2 = total2 + 1
    elif ((int(r0[0])>=int(r1[0]) and int(r0[0])<=int(r1[1])) or (int(r0[1])>=int(r1[0]) and int(r0[1])<=int(r1[1]))):
        total2 = total2 + 1
    
print('Star 1: '+str(total))
print('Star 2: '+str(total2))