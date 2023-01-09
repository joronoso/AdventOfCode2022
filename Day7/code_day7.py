class Dir:
    
    totalDirs = []
    
    def __init__(self, name, parent):
        self.dirs = {}
        self.files = []
        self.name = name
        if parent is None: 
            self.parent = self
            self.level = 0
        else: 
            self.parent = parent
            self.level = self.parent.level + 1
    
    def getSize(self):
        size = 0
        for dir in self.dirs.values(): size += dir.getSize()
        for file in self.files: size += file.size
        return size
        
    def getSubdir(self, path):
        subdirs = path.split('/')
        dir = self
        for s in subdirs:
            if s=='': continue
            dir = dir.dirs[s]
        return dir
            
    def addDir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Dir(name, self)
            self.totalDirs.append(self.dirs[name])

class File:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        

f = open("input.txt", "r")
lista = f.read().splitlines()
f.close()

root = Dir('', None)
currentDir = root

for line in lista:
    if line[0:6] == '$ cd /': 
        currentDir = root.getSubdir(line[5:])
    elif line[0:7] == '$ cd ..': 
        currentDir = currentDir.parent
    elif  line[0:5] == '$ cd ':
        currentDir = currentDir.getSubdir(line[5:])
    elif line[0:4] == '$ ls':
        pass
    elif line[0:3] == 'dir':
        currentDir.addDir(line[4:])
    else:
        sp = line.split(' ')
        currentDir.files.append(File(sp[1], int(sp[0])))
        
star1 = 0
deletionTarget = 30000000 -( 70000000 - root.getSize() )
star2 = 70000000
for d in Dir.totalDirs:
    s = d.getSize()
    if s<=100000: star1 += s
    if s<star2 and s>=deletionTarget: star2 = s

print('Star 1: '+str(star1))
print('Star 2: '+str(star2))
          
