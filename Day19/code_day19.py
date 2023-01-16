import re
import numpy as np

# We will represent each possible status with an array row:
#  #ore_robots, #clay_robots, #obsidian_robots, #geode_robots, #ore, #clay, #obidian, #geode
# Each formula in a blueprint can be represented as + the robot - the materials in the same format

re_blueprint = re.compile('Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

blueprints = []

for l in lista:
    gr = re_blueprint.match(l).groups()
    blueprints.append(np.array( [ [0,0,0,0,0,0,0,0], # This represents the possibility of not doing anything 
                                  [1,0,0,0,-int(gr[0]),0,0,0], 
                                  [0,1,0,0,-int(gr[1]),0,0,0],
                                  [0,0,1,0,-int(gr[2]),-int(gr[3]),0,0],
                                  [0,0,0,1,-int(gr[4]),0,-int(gr[5]),0] ], ndmin=2) )

def calculateEndState(num_hours, bl, initial_state=None):
    state = initial_state if initial_state is not None else np.array([1,0,0,0,0,0,0,0], ndmin=2) # We start with an ore robot and zero of everything
    num_obs = -bl[:,6].min()
    max_ore_cost = -bl[:,5].min()

    for i in range(num_hours):
        if state.shape[0]==0: # No options
            state = np.array([0,0,0,0,0,0,0,0], ndmin=2) # So that we get a zero
            break
        
        # This commented out part works fine but it's terribly slow.
        # new_state = None
        # for st in state:
        #     add_mat = np.append(np.array([0,0,0,0]), st[:4]).reshape(1,-1)
        #     # We will make the assumption that we never buy more than one robot in a turn
        #     new_state_p = bl + st.reshape(1,-1)
            
        #     # Eliminate rows with negatives
        #     new_state_p = new_state_p[new_state_p.min(axis=1)>=0,:]
            
        #     # Finally, we add the new materials            
        #     new_state_p = new_state_p + add_mat        
            
        #     if new_state is None:
        #         new_state = new_state_p
        #     else:
        #         new_state = np.append(new_state, new_state_p, axis=0)
        
        # Getting rid of the loop and rewriting it as numpy array operations is much faster
        state_repeated = np.repeat(state, repeats=5, axis=0)
        
        new_state = state_repeated + np.resize(bl, (state_repeated.shape[0],8))
        add_mat = np.append( np.zeros((new_state.shape[0], 4), dtype=int), state_repeated[:, :4], axis=1)
        
        mask_negatives = new_state.min(axis=1)>=0
        new_state = new_state[mask_negatives, :] + add_mat[mask_negatives, :]

        # Remove duplicate rows
        new_state = np.unique(new_state, axis=0)

        # From here on we purge states that we can tell will not be optimal, to speed things up

        # Assuming the optimal path is the one that gets geode robots the fastest
        new_state = new_state[new_state[:,3]>=new_state[:,3].max()]
        
        # Those states that accumulate more than twice the ore of the cost of the most expensive robot can't be optimal
        new_state = new_state[new_state[:,4]<=5*max_ore_cost]

        # Prune those states that have too much unused obsidian 
        new_state = new_state[(new_state[:,6]<2*num_obs)]
        
        state = new_state
    return state
    
max_hours = 24
max_hours2 = 32
quality_levels = []
star2_geodes = 1
for idbl, bl in enumerate(blueprints):
    state = calculateEndState(max_hours, bl)
    quality_levels.append(state[:,7].max()*(idbl+1))
        
    if idbl<3:
        state = calculateEndState(max_hours2-max_hours, bl, state)
        star2_geodes =  star2_geodes * state[:,7].max()

print('Star 1: '+str(sum(quality_levels)))
print('Star 2: '+str(star2_geodes))
