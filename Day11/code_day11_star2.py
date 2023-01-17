import numpy as np

class Monkey:

    monkey_list = []
    initial_items = []
    
    @classmethod
    def add_monkey(cls, items, operation, div_test, if_true, if_false):
        cls.initial_items.append(items)
        cls.monkey_list.append( Monkey(operation, div_test, if_true, if_false, len(cls.monkey_list)) )
       
    @classmethod
    def initialize(cls):
        ownership_list = []
        items = []
        for idx, x in enumerate(cls.initial_items):
            ownership_list += [idx]*len(x)
            items += x
        cls.ownership = np.array(ownership_list)
        cls.divisors = np.array([m.div_test for m in cls.monkey_list]).reshape((-1,1))
        cls.rests = np.array(items)
        cls.rests = np.resize(cls.rests, (len(cls.monkey_list), len(items))) 
        cls.rests = cls.rests % cls.divisors
    
    def __init__(self, operation, div_test, if_true, if_false, num):
        self.operation = operation
        self.div_test = div_test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_counter = 0
        self.num = num
        
    def take_turn(self, star2=False):
        mask = (Monkey.ownership == self.num)
        
        # Apply the operation to the corresponding entries and recalculate rests
        Monkey.rests[:,mask] = self.operation(Monkey.rests[:,mask]) % Monkey.divisors
        
        # Now change ownership of items
        mask2 = Monkey.rests[self.num,:] == 0
        Monkey.ownership[ mask & mask2 ] = self.if_true 
        Monkey.ownership[ mask & np.logical_not(mask2) ] = self.if_false
        self.inspect_counter += int(mask.sum())
    
    def __lt__(self, other):
        return self.inspect_counter<other.inspect_counter
            
Monkey.add_monkey([83, 88, 96, 79, 86, 88, 70],
                  lambda x: x*5,
                  11, 2, 3) 
Monkey.add_monkey([59, 63, 98, 85, 68, 72],
                  lambda x: x*11,
                  5, 4, 0) 
Monkey.add_monkey([90, 79, 97, 52, 90, 94, 71, 70],
                  lambda x: x+2,
                  19, 5, 6) 
Monkey.add_monkey([97, 55, 62],
                  lambda x: x+5,
                  13, 2, 6) 
Monkey.add_monkey([74, 54, 94, 76],
                  lambda x: x*x,
                  7, 0, 3) 
Monkey.add_monkey([58],
                  lambda x: x+4,
                  17, 7, 1) 
Monkey.add_monkey([66, 63],
                  lambda x: x+6,
                  2, 7, 5) 
Monkey.add_monkey([56, 56, 90, 96, 68],
                  lambda x: x+7,
                  3, 4, 1) 

Monkey.initialize()

for i in range(10000):
    for m in Monkey.monkey_list:
        m.take_turn(True)

Monkey.monkey_list.sort()
print('Star 2: '+str(Monkey.monkey_list[-1].inspect_counter*Monkey.monkey_list[-2].inspect_counter))

        