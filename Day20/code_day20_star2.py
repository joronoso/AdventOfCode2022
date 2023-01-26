f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

orig = [811589153*int(x) for x in lista]
lista = list(range(len(orig)))

for repeat in range(10):
    for x in range(len(orig)):
        i = lista.index(x)
        lista.pop(i)
        num = (i+orig[x])%len(lista)
        lista.insert(num, x)
i = lista.index(orig.index(0))
print('Star 2:', orig[lista[(i+1000)%len(lista)]] + orig[lista[(i+2000)%len(lista)]] + orig[lista[(i+3000)%len(lista)]] )