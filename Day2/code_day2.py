vals = { 'A X': 3+1,
         'A Y': 6+2,
         'A Z': 0+3,
         'B X': 0+1,
         'B Y': 3+2,
         'B Z': 6+3,
         'C X': 6+1,
         'C Y': 0+2,
         'C Z': 3+3 }

val2 = { 'A X': 0+3,
         'A Y': 3+1,
         'A Z': 6+2,
         'B X': 0+1,
         'B Y': 3+2,
         'B Z': 6+3,
         'C X': 0+2,
         'C Y': 3+3,
         'C Z': 6+1 }

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

points = 0
points2 = 0
for line in lista:
    points = points + vals[line]
    points2 = points2 + val2[line]

print("Star 1: "+str(points))
print("Star 2: "+str(points2))

