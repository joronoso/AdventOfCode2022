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
        if self.monkey_list[self.deps[0]].number is not None and self.monkey_list[self.deps[1]].number is not None:
            self.number = eval(str(self.monkey_list[self.deps[0]].number)+self.operator+str(self.monkey_list[self.deps[1]].number))

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

for l in lista:
    Monkey.add_monkey(l)
    
pending_monkeys = Monkey.monkey_list.keys()
while 'root' in pending_monkeys:
    new_pending_monkeys = []
    for m in pending_monkeys:
        if not Monkey.monkey_list[m].calculate_self():
            new_pending_monkeys.append(m)
    pending_monkeys = new_pending_monkeys
            
print('Star 1', Monkey.monkey_list['root'].number)

                              
