import re

class Monkey:
    re_monkey_number = re.compile('([a-z]{4}): (\d+)')
    re_monkey_operation = re.compile('([a-z]{4}): ([a-z]{4}) (.) ([a-z]{4})')
    
    monkey_list = {}
    
    @classmethod
    def add_monkey(cls, line):
        monkey = Monkey(line)
        cls.monkey_list[monkey.name] = monkey
    
    def __init__(self, line):
        m = self.re_monkey_number.match(line)
        if m is None:
            m = self.re_monkey_operation.match(line)
            gr = m.groups()
            self.name = gr[0]
            self.operator = gr[2]
            self.deps = (gr[1], gr[3])
            self.number = None
        else:
            gr = m.groups()
            self.name = gr[0]
            self.number = int(gr[1])

    def calculate_self(self):
        if self.number is not None: return True
        if self.name == 'humn': return False
        if self.monkey_list[self.deps[0]].number is not None and self.monkey_list[self.deps[1]].number is not None:
            self.number = eval(str(self.monkey_list[self.deps[0]].number)+self.operator+str(self.monkey_list[self.deps[1]].number))

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

for l in lista:
    Monkey.add_monkey(l)
    
# Adaptations for Star 2
Monkey.monkey_list['humn'].number = None
root = Monkey.monkey_list['root']
root.operator = '=='

pending_monkeys = [ m for m in Monkey.monkey_list.keys() if Monkey.monkey_list[m].number is None ]
save_pending_monkeys = pending_monkeys

y1 = []
y2 = []
x = (0,10000000000000)
for humn in x:
    Monkey.monkey_list['humn'].number = humn
    while root.deps[0] in pending_monkeys or root.deps[1] in pending_monkeys:
        new_pending_monkeys = []
        for m in pending_monkeys:
            if not Monkey.monkey_list[m].calculate_self():
                new_pending_monkeys.append(m)
        pending_monkeys = new_pending_monkeys
    y1.append(Monkey.monkey_list[root.deps[0]].number)
    y2.append(Monkey.monkey_list[root.deps[1]].number)

    for spm in save_pending_monkeys:
        Monkey.monkey_list[spm].number = None
    pending_monkeys = save_pending_monkeys

if y1[0]==y1[1]:
    y_t = y1[0]
    y_0 = y2[0]
    dy = y2[1] - y2[0]
else:
    y_t = y2[0]
    y_0 = y1[0]
    dy = y1[1] - y1[0]
    
star2 = (y_t-y_0)*(x[1]-x[0])/dy
    
print('Star 2:', int(round(star2,0)))

                              
