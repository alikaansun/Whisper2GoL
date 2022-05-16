import random
from whisper import get_word_to_number, expend_binary, matrix_construct
import numpy as np
class GameOfLife:
    
    def __init__(self,word):
        self.seed=word
        self.size=50
        self.iterno=0
    
    def initialcond(self):
        if self.seed == "random":
            self.cells = [[1 if random.random() > 0.8 else 0 for i in range(self.size)]
                       for j in range(self.size)] #random filling with ~0.8 fillfactor
        else:
            self.cells=matrix_construct(expend_binary(get_word_to_number(str(self.seed))))
        self.iterno=20+np.mod(int(get_word_to_number(str(self.seed))),10) 
        #decides how many iterations will be done on GoL
    
    def densitycheck(self): #checks density to stop iterations
            count = 0 
            for x in range(self.size):
                for y in range(self.size):
                    if self.cells[x][y]==1:
                        count+=1
            return count

    def cellget(self,x,y): 
        return self.cells[min(x,self.size-1)][min(y,self.size-1)] 
    
    def neighcell(self,x,y): #gets nearby cells
        neigh = [self.cellget(x+dx,y+dy) for dx in [-1,0,1]
                    for dy in [-1,0,1] if not (dx==0 and dy == 0)]
        return len(list(filter(lambda x: x == 1, neigh)))
    
    def deadoralive(self,x,y):
        count = self.neighcell(x,y)
        return 1 if count==3 else (0 if count<2 or count>3 else self.cells[x][y])

    def iter(self):
        for i in range(self.iterno):
            self.cells = [[self.deadoralive(x,y) for x in range(self.size)]
                            for y in range(self.size)]