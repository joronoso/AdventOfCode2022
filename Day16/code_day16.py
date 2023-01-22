import numpy as np
import re
import itertools

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

re_valve = re.compile('Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)')

non_zero_valves = []
valves = {}

for line in lista:
    gr = re_valve.match(line).groups()
    valves[gr[0]] = [int(gr[1]), gr[2].split(', ')]
    if gr[1]!='0': non_zero_valves.append(gr[0])

# Now we want to calculate the distances between all non-zero valves
distances = np.zeros((len(non_zero_valves), len(non_zero_valves)), dtype=int)
for orig in range(len(non_zero_valves)-1):
    turn = 0
    old_valves = (non_zero_valves[orig],)
    while np.prod(distances[orig][orig+1:])==0:
        turn += 1
        new_valves = set()
        for v in old_valves:
            new_valves.update(valves[v][1])
        for v in new_valves:
            if v in non_zero_valves:
                ind = non_zero_valves.index(v)
                if distances[orig][ind]==0 and orig!=ind:
                    distances[orig][ind] = turn
        old_valves = new_valves
distances = np.maximum( distances, distances.transpose() )

# Calculate distances from AA
AA_dists = np.zeros(len(non_zero_valves), dtype=int)
turn = 0
old_valves = ('AA',)
while np.prod(AA_dists)==0:
    turn += 1
    new_valves = set()
    for v in old_valves:
        new_valves.update(valves[v][1])
    for v in new_valves:
        if v in non_zero_valves:
            ind = non_zero_valves.index(v)
            if AA_dists[ind]==0:
                AA_dists[ind] = turn
    old_valves = new_valves

def calculate_max_flow(list_valves, mins):
    # Calculate through all permutations of valve the valve list
    uncompleted = [[[x], mins-AA_dists[x]-1, (mins-AA_dists[x]-1)*valves[non_zero_valves[x]][0]] for x in list_valves]
    c_max_flow = 0
    while len(uncompleted)>0:
        new_uncompleted = []
        for u in uncompleted:
            for a in [x for x in list_valves if x not in u[0]]:
                mins = u[1] - distances[a][u[0][-1]] - 1
                if mins<0: # Is this finished?
                    if c_max_flow<u[2]:
                        c_max_flow = u[2]
                else:
                    flow = u[2] + mins*valves[non_zero_valves[a]][0]
                    l = u[0].copy()
                    l.append(a)
                    new_uncompleted.append([l,mins,flow])
        uncompleted = new_uncompleted
    return c_max_flow

print('Star 1: '+str(calculate_max_flow(list(range(len(non_zero_valves))), 30)))

# Find combinations of splits between elephant and self
# We'll assume that the imbalance in the split will not be more than 10-5
max_flow = 0
for comb in itertools.chain(itertools.combinations(range(len(non_zero_valves)),8),
                            itertools.combinations(range(len(non_zero_valves)),9),
                            itertools.combinations(range(len(non_zero_valves)),10)):
    flow = calculate_max_flow(comb, 26) + calculate_max_flow([x for x in range(len(non_zero_valves)) if x not in comb], 26)
    if flow>max_flow: 
        max_flow = flow

print('Star 2: '+str(max_flow))
