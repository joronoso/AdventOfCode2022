class Packet:
    
    def compare(val1, val2):
        if type(val1)==list:
            if type(val2)==list:
                for i in range(min(len(val1), len(val2))):
                    c = Packet.compare(val1[i], val2[i])
                    if c!=0: 
                        return c
                if len(val1)>len(val2): return -1
                elif len(val1)<len(val2): return 1
                else: return 0
            else:
                return Packet.compare(val1, [val2])
        else:
            if type(val2)==list:
                return Packet.compare([val1], val2)
            else:
                if val1>val2: return -1
                elif val1<val2: return 1
                else: return 0
    
    def __init__(self, packet):
        self.packet = packet

    def __lt__(self, other):
        return False if Packet.compare(self.packet, other.packet)==-1 else True

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

sep1 = Packet([[2]])
sep2 = Packet([[6]])
list_packets = [sep1, sep2]
for i in range(0, len(lista), 3):
    list_packets.append(Packet(eval(lista[i])))
    list_packets.append(Packet(eval(lista[i+1])))
    
list_packets.sort()

print('Star 2: '+str((list_packets.index(sep1)+1)*(list_packets.index(sep2)+1)))