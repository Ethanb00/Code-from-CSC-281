class Towers():
    def __init__(self, nbDisks, From, To, Spare):
        self.n = nbDisks
        self.names = [From,To,Spare]
        self.disks = [[i for i in range(self.n,0,-1)],[],[]] 
        self.nbTowers=3
    
    def draw(self):
        for i in range(self.n):
            line = ''
            for tower in range(self.nbTowers):
                mask = '{0:^12}'                
                if len(self.disks[tower]) < self.n-i:
                    w = mask.format(' ') 
                else:
                    p = self.n - i - 1
                    w = mask.format('**'*self.disks[tower][p])
                line = line+w
            print(line)
        line = ''
        for i in range(self.nbTowers):
            w = mask.format(self.names[i])
            line+= w
        print(line)
    def move(self,From,To):
        n = self.disks[From].pop()
        self.disks[To].append(n)  
        print('Moving from,',self.names[From],'to',self.names[To])
        self.draw()

    def moves(self,n,From,To,Spare):
        if n == 1:
            self.move(From,To)
        else:
            self.moves(n-1,From,Spare,To)
            self.move(From,To)
            self.moves(n-1,Spare,To,From)
    
