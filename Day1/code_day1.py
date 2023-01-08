f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

partial = 0
elf = []

for line in lista:
    if line.strip() == '':
        elf.append(partial)
        partial=0
    else: partial = partial+int(line)
    
elf.append(partial)

print("Star 1: "+str(max(elf)))

max3 = 0
for i in range(3):
    parc_max = max(elf)
    max3 = max3 + parc_max
    elf.remove(parc_max)
    
print('Star 2: '+str(max3))