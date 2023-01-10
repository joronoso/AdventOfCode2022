input = ['#.########################################################################################################################',
         '#>^v<.<<^v^<><>>>^<vv>^>><<<^^.^v^<<v^v<v>^^>^^<^><^>.^>v<v<v.v<>vv<^^^vvv<.^v^<v^.^.>.<^<^>v^.v^v<>^vv^<<>>v^<<.<vvv^.<<#',
         '#><^>><<vvv.v>^<..<v><v^^>>>v>>vv^^^<^^<><<>v>v<><><<^<<v>v.>.v>vv<>^>.^vv^^.<v<vv.<v<>>^>>><v<.>v>v^<v<>^<<<^v^<.v..v<^>#',
         '#<v^.^>vv.^<^<>v^<^^^<^^>v<<>v><><^v^<v.v<^><<<^^^.>vv<.^<v<v<v^<v>^<v^<.><^^<>^v>..<v..>v^><>>^<.>.vv<<<.v.^^^^^>.<<.<v<#',
         '#>.<<^>^v>>v<v<>>^v^>><>>v.^>.<>>^v<>.^<>^^^<vv<vv^^^v^^<<><v^^>>.v<v^v<.>^^.^>^v><vv<^^<^>>^v>^>^^v^v.<<^.vv<v..^^v.>>v>#',
         '#>v^^>^^.>.^^<>><>v^^^<v>>>v^v^v^^<^<<^<<>><<^<<vv<<^>>>.<^v^><v<v>>v^>><vv..<v><vv^.>.v^vv>^><v.<vv>^vv^^>><v>v>v<v>>^><#',
         '#>^<vvv^><^vvv>><^^vv^^>v<.v^<^<vv<><v<>^^^^<>^>v<^vv><v.<>>..>^^v<><>v.>>vv<><^^><>v<v<>vv^^>v><>>.v<v<>>>^^^v^v<<<^><^<#',
         '#>^><v>>^.^><.^^^^<v>v<.v^>^^^<<<^<<v><><v>>>>v<v>vv<v><>.^><<^v<>^^v<.^^v<^>v<>v^.>.<<.>vv.^^vvv.<.v^>^><v^<^^^^>.^vv^^<#',
         '#><v^vvv>^<v<>^>^<.><v<<<><v<<<^v^>^<v>>v<^<vv<v>v^..^>^^^^<.><<<>vvv>^vv^>v^<<>vv<<v^>^.v>.^<^^..>v<^<v<^>^^<><vv<.^v^.>#',
         '#<^<><v.>.<<^>>v<^..<<.>>v<<^^>v.<v.<.v<.vv<^>^vvv>^>>v<.<>v^<<<<^<v>^<vv>v<<<^^>^^<<<>^>vv>>^.><>^^v^^><v.>v^^<>^^^^<v>>#',
         '#<v.>^><^>>vv^vvvv^<>vv<<v<<v^v^v<><<^.^<><v^^<><.v<^>^v>^<^v^><^>v>^<<<v><v<<^^>v><v<<<<^.v^.<^<v<<>^>>><>vv<.^^..v>v<<>#',
         '#<v<^>v<<^^>>v<^>^^>v>^>v.v<<<>v>><v<vv.v^<<.v<v>v<<^v<<.>^<v>^^>^..<>^^v.^><^vv><v<<>>vvv^^vv<<>^>^v^<^><<^v<.>^>><^^<^<#',
         '#<<>>v^^>>^.<^^<^^^>^^>vv>>>>>v^vv><.v>v>v<^>><^<<v><^>^>^vv^vv^<v<<<v>><v.v>^^<<.^vvv<>vv<><^^^vv>v^.><^<^vv><<.vv^^^.v<#',
         '#<.<v><vv>^<>>^>.^<<v>..^vvv^^v>^<>>v<<<..^vv>^<...^<<>.<^>^<.v><v.>^^.vv<<^<v.>v^v^^>.^^vv.^v^><<>^^^^.v<..>v^<>^<>>vvv>#',
         '#<^<<v^v<^<.^v^>v^<^<.>^^v^<^>.<v>v>^^^.v><v><vv<<v<>v.<^><>.><vv><<^^.vv<.<^.vvvvvv^^^^<vvv.^<.>v.^v>^v>><v^v.>v^^v.<.^<#',
         '#.<<^.<v<<^^<>v.<.>v.^^^<<^v>.v<>v<...>^<v.<v<<><>.v<^^^>.^v>vv^<^.>.^>>^>v.>v>.^^<v><v^<><^^v<v^^<<<>^.>v><<v<<v>.<^v<v>#',
         '#>>><<^v<^>v^>><^^.<v<^<<<^.<v^>v<<^^^>>^^.^v^>v^<>^v.>^><^>.^^v>><<>v<v><^vv<><^v>.v><^><<v>.^>v^^<<^<>.>v<v^^v<v.>v..>>#',
         '#.v>^^.<v.^^>><^v<vv>v<^<>><v>^^v<<v>>.<<v^v<^.v.<^>^vvv<vv^v>><>^v<^><v..<^<vv<<v<.<^^^<<>v^^v>v>>^^^>vvvv<^^<>.<^^^><^.#',
         '#<^^<v<^<>>vv>v<<vv^v<^.<>><<v<<v>^^^^>^<^>>^vv^^<^vv^>vvv>v>^v.><^>^^>.^^v.<<v.v<^<<^v><vv^^^v^>><.^<>v><v<vv^^>>v^>>..>#',
         '#<^>v^^vv>^><^^^^^^>>.v<^.<^<>^><^.v<v<>>v.^.v^<vv^^<<<><..>>><.v<vv>^v^.<>>v^v.<vv><v^<vv<<v<><.<<^^v><.>v<<>v<<^^>>vvv>#',
         '#.><<>>><^vv^v.>.>.^.<>>^^^v^^><>v<><>>>><v<<v^<>^v^v>>^^v^.<>v>vvv>v>>.<>>^>>>>^>^>v<.><vv>>.>>v<>><<^><v.^<<..>.vvv^v<<#',
         '#>^>^<^^v>^^^>v>.v><>^>^v^^.v.>>v>>v^^^>>>v><>.<vv.<<<.<^^<^>^>v<v>^<^v<><>><>.^vv>^>.^>>>^><<^>^v<<^<vv<vv^.^^<vv>>v.<>>#',
         '#><<><v<<vv>^>.^.<<.>.<.v>^>><^>v<>v^.<><^v^>>v<^^<.<^<>.<vv<<>vvvv>vv>v.<<^v<.>v>^^<v><>.>v>^<^<^^..>v<v>v.^<^<^<vv<v><>#',
         '#>>^^<^<v^<v<vv^>..^v.^<^>^.v><^vv^..v.<>v<<.<v..v>v>vvv^>^<v>vv.^.>^.^^>v<^>v>v><>>^^>.v^<<.<^>v^vv><.v..<.><<v<.<<.<vv>#',
         '#><<>^<>><^.^^><v<<^<^^>>v><v.vv><v<<<<.<^<v>v><>v<<^<<>>^>^vv>v<v.vv>v>v>>>><..v^^vv>><<>>vv><>>.>v<<>v<v^vv<v<<v^>>v<^.#',
         '#>.<<><<vv<^.v<v<v<^>>v><v.^>^v.<^v.^^^<<<<.<<v^v>^<.>^vv^<<^^>.v>>>.v^v<v<v><^>v.>>^^>^v>vv<>vv^^<.<.v>^^v>.^^v<^v^>^^v>#',
         '########################################################################################################################.#']

# input = ['#.######',
#           '#>>.<^<#',
#           '#.<..<<#',
#           '#>v.><>#',
#           '#<^v^^>#',
#           '######.#']

class Thingy():
    def __init__(self, initPos, thingy_type, valley):
        self.valley = valley
        self.initPos = initPos
        self.thingy_type = thingy_type
        self.posHistory = [initPos]
    
    # If this thingy will be in position pos in time t, return True
    def checkCollision(self, t, pos):
        if self.thingy_type == '#': 
            return self.initPos == pos
        elif t>=len(self.posHistory):
            # Need to calculate new position
            if self.thingy_type == '<':
                if self.posHistory[-1][0]==1:
                    self.posHistory.append((self.valley.size[0]-2, self.posHistory[-1][1]))
                else:
                    self.posHistory.append((self.posHistory[-1][0]-1, self.posHistory[-1][1]))
            elif self.thingy_type == '>':
                if self.posHistory[-1][0]==(self.valley.size[0]-2):
                    self.posHistory.append((1, self.posHistory[-1][1]))
                else:
                    self.posHistory.append((self.posHistory[-1][0]+1, self.posHistory[-1][1]))
            elif self.thingy_type == '^':
                if self.posHistory[-1][1]==(self.valley.size[1]-2):
                    self.posHistory.append((self.posHistory[-1][0], 1))
                else:
                    self.posHistory.append((self.posHistory[-1][0], self.posHistory[-1][1]+1))
            else: # v
                if self.posHistory[-1][1]==1:
                    self.posHistory.append((self.posHistory[-1][0], self.valley.size[1]-2))
                else:
                    self.posHistory.append((self.posHistory[-1][0], self.posHistory[-1][1]-1))
        return self.posHistory[t] == pos
               

class Valley():
    
    def __init__(self, input):
        self.size = (len(input[0]), len(input))
        self.thingys = []
        for i in range(len(input)):
            for j in range(len(input[i])):
                if input[i][j]=='.': continue
                else:
                    self.thingys.append( Thingy((j, len(input)-i-1), input[i][j], self) )
                    
    def solve(self, t_init, pos_init, target):
        t = t_init
        positions = {pos_init}
        while(True):
            t += 1
            print(t, len(positions))
            positions_old = positions
            positions = set()
            for ini in positions_old:
                options = [ ini ] # Because staying in the same place is always a possibility
                if ini[0] != 1: options.append( (ini[0]-1, ini[1]) ) # Left
                if ini[0] != self.size[0]-2: options.append( (ini[0]+1, ini[1]) ) # Right
                if ini[1] != self.size[1]-1: options.append( (ini[0], ini[1]+1) ) # Up
                if ini[1] != 0: options.append( (ini[0], ini[1]-1) )
            
                # Now check if we've arrived, or have collided
                for opt in options:
                    if opt in positions: continue # This position is already considered
                    if opt == target: return t # We won
                    collided = False
                    for thing in self.thingys:
                        if thing.checkCollision(t, opt):
                            collided = True
                            break
                    if not collided:
                        positions.add(opt)
    
                    
v = Valley(input)
t1 = v.solve(0, (1, v.size[1]-1), (v.size[0]-2, 0))
t2 = v.solve(t1,  (v.size[0]-2, 0), (1, v.size[1]-1))
t3 = v.solve(t2, (1, v.size[1]-1), (v.size[0]-2, 0))

print('Star 1: '+str(t1))
print('Star 2: '+str(t3))



            