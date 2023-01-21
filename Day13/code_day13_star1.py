def compare(val1, val2):
    if type(val1)==list:
        if type(val2)==list:
            for i in range(min(len(val1), len(val2))):
                c = compare(val1[i], val2[i])
                if c!=0: 
                    return c
            if len(val1)>len(val2): return -1
            elif len(val1)<len(val2): return 1
            else: return 0
        else:
            return compare(val1, [val2])
    else:
        if type(val2)==list:
            return compare([val1], val2)
        else:
            if val1>val2: return -1
            elif val1<val2: return 1
            else: return 0

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

star1 = 0
for i in range(0, len(lista), 3):
    print(lista[i])
    if compare(eval(lista[i]), eval(lista[i+1]))!=-1: 
        print('Sumamos '+str((i/3) + 1))
        star1 += (i/3) + 1
    
print(star1)