f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

orig = lista
lista = list(range(len(orig)))

for x in range(len(orig)):
    i = lista.index(x)
    lista.pop(i)
    num = (i+int(orig[x]))%len(lista)
    lista.insert(num, x)
i = lista.index(orig.index('0'))
print('Star 1:', int(orig[lista[(i+1000)%len(lista)]]) + int(orig[lista[(i+2000)%len(lista)]]) + int(orig[lista[(i+3000)%len(lista)]]) )