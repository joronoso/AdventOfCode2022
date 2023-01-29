class Elf:
    elves = []
    elf_positions = set()
    turn = 0
    
    @classmethod
    def add_elf(cls, x, y):
        cls.elf_positions.add((x,y))
        cls.elves.append(Elf(x,y))

    @classmethod
    def take_turn(cls):
        new_elf_positions = set()
        cls.proposals = set()
        cls.clashes = set()
        # First half
        for e in cls.elves:
            p = e.first_half()
            if p is not None:
                if p in cls.proposals:
                    cls.clashes.add(p)
                else:
                    cls.proposals.add(p)
        # Second half
        for e in cls.elves:
            new_elf_positions.add(e.second_half())
        unchanged = (cls.elf_positions==new_elf_positions)
        cls.elf_positions = new_elf_positions
        cls.turn = cls.turn + 1
        return unchanged
        
    @classmethod
    def get_limits(cls):
        max_x = float('-inf')
        max_y = float('-inf')
        min_x = float('inf')
        min_y = float('inf')
        for e in cls.elves:
            if e.x > max_x: max_x = e.x
            if e.y > max_y: max_y = e.y
            if e.x < min_x: min_x = e.x
            if e.y < min_y: min_y = e.y
        return (max_x, min_x, max_y, min_y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.proposal_generator = [ lambda: (self.x, self.y-1),  # N
                                    lambda: (self.x, self.y+1),  # S
                                    lambda: (self.x-1, self.y),  # W
                                    lambda: (self.x+1, self.y) ] # E
        self.recalc_directions()
    
    def recalc_directions(self):
        x = self.x
        y = self.y
        self.north = { (x, y-1), (x-1, y-1), (x+1, y-1) }
        self.south = { (x, y+1), (x-1, y+1), (x+1, y+1) }
        self.east = { (x+1, y), (x+1,y+1), (x+1, y-1) }
        self.west = { (x-1, y), (x-1,y+1), (x-1, y-1) }
        self.directions = [self.north, self.south, self.west, self.east]
        self.around = self.north | self.south | self.east | self.west
    
    def first_half(self):
        self.proposal = None
        if len(self.around & self.elf_positions)!=0: # If there are no elves around, do nothing
            for i in [x%4 for x in range(self.turn, self.turn+4)]:
                if len(self.directions[i] & self.elf_positions)==0: 
                    self.proposal = self.proposal_generator[i]()
                    break
        return self.proposal
    
    def second_half(self):
        if self.proposal is not None and self.proposal not in self.clashes:
            self.x = self.proposal[0]
            self.y = self.proposal[1]
            self.recalc_directions()
        return (self.x, self.y)
 
f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

for i, l in enumerate(lista):
    for j, k in enumerate(l):
        if k=='#':
            Elf.add_elf(j, i)
            
for i in range(10):
    Elf.take_turn()

m = Elf.get_limits()
print('Star 1: ', ((m[0]-m[1]+1)*(m[2]-m[3]+1))-len(Elf.elves))

while not Elf.take_turn():
    i += 1

print('Star 2: ', i+2)


