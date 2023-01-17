import numpy as np

monkey_list = []

class Monkey:
    def __init__(self, items, operation, div_test, if_true, if_false):
        self.items = np.array(items)
        self.operation = operation
        self.div_test = div_test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_counter = 0
        
    def take_turn(self):
        self.items = self.operation(self.items)
        self.items = (self.items/3).astype(int)
        div_test_res = (self.items%self.div_test==0)
        monkey_list[self.if_true].items = np.concatenate((monkey_list[self.if_true].items, self.items[div_test_res]))
        monkey_list[self.if_false].items = np.concatenate((monkey_list[self.if_false].items, self.items[np.logical_not(div_test_res)]))
        self.inspect_counter += len(self.items)
        self.items = np.empty((0,), dtype=int)
        
    def __lt__(self, other):
        return self.inspect_counter<other.inspect_counter
            

monkey_list.append( Monkey([83, 88, 96, 79, 86, 88, 70],
                            lambda x: x*5,
                            11, 2, 3) )
monkey_list.append( Monkey([59, 63, 98, 85, 68, 72],
                            lambda x: x*11,
                            5, 4, 0) )
monkey_list.append( Monkey([90, 79, 97, 52, 90, 94, 71, 70],
                            lambda x: x+2,
                            19, 5, 6) )
monkey_list.append( Monkey([97, 55, 62],
                            lambda x: x+5,
                            13, 2, 6) )
monkey_list.append( Monkey([74, 54, 94, 76],
                            lambda x: x*x,
                            7, 0, 3) )
monkey_list.append( Monkey([58],
                            lambda x: x+4,
                            17, 7, 1) )
monkey_list.append( Monkey([66, 63],
                            lambda x: x+6,
                            2, 7, 5) )
monkey_list.append( Monkey([56, 56, 90, 96, 68],
                            lambda x: x+7,
                            3, 4, 1) )

for i in range(20):
    for m in monkey_list:
        m.take_turn()
          
monkey_list.sort()
print('Star 1: '+str(monkey_list[-1].inspect_counter*monkey_list[-2].inspect_counter))
