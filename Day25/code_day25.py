f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

def snafuToDecimal(snafu):
    dec = 0
    base = 1
    for c in reversed(snafu):
        if c=='-': num=-1
        elif c=='=': num=-2
        else: num=int(c)
        dec += base*num
        base = base*5
    return dec
        
def decimalToSnafu(decimal):
    if decimal==1: return '1'
    aprox = '2'
    decaprox = snafuToDecimal(aprox)
    while decaprox<=decimal:
        if decaprox==decimal: return aprox
        aprox += '2'
        decaprox = snafuToDecimal(aprox)

    for i in range(len(aprox)):
        pre_i = aprox[:i]
        post_i = aprox[i+1:]
        prealt = '2'
        for alt in ['1', '0', '-', '=']:
            val2 = snafuToDecimal(pre_i+alt+post_i)
            if val2==decimal: return pre_i+alt+post_i
            if val2>decimal:
                prealt = alt
                aprox = pre_i+alt+post_i
            else:
                aprox = pre_i+prealt+post_i
                break
    return aprox
                
total = 0
for line in lista:
    total += snafuToDecimal(line)
    
print('Star 1: '+str(decimalToSnafu(total)))