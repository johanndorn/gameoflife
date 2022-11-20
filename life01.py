from copy import deepcopy
import os
import time



class Field:
    rows=5
    cols=5
    matrix = []
  

    def init_matrix(self):
        print("init_matrix()", self.rows, self.cols )
        for i in range(self.rows):
            arrCols = []
            for j in range(self.cols):
                arrCols.append('_')
            self.matrix.append(arrCols )
        

            
    def __init__(self,anzRows, anzCols ): 
        self.rows=anzRows
        self.cols=anzCols
        #self.init_matrix()

    def countPos(self, posRow, posCol):
        try:
            if self.matrix[posRow][posCol] == "X":
                return 1
            else: 
                return 0
        except:  #außerhalb der Indexgrenzen
            return 0
            
            
    
    
    def getNumberOfNeighbors(self, posRow, posCol):
        #print("getNumberOfNeighbors()", posRow, posCol, "Value:",  self.matrix[posRow][posCol] )
        iNBs=0
        
        iNBs=iNBs+self.countPos(posRow-1, posCol-1) + self.countPos(posRow-1, posCol)  + self.countPos(posRow-1, posCol+1) 
        iNBs=iNBs+self.countPos(posRow, posCol-1) + self.countPos(posRow, posCol+1) 
        iNBs=iNBs+self.countPos(posRow+1, posCol-1) + self.countPos(posRow+1, posCol)  + self.countPos(posRow+1, posCol+1) 
        return iNBs
    
    def evolution(self):
        clone = deepcopy(self.matrix)
        #der clone wird aktualisiert auf Basis der aktuellen Matrix
        i=0
        for curRow in clone:
            j=0
            for curCol in curRow:
                if curCol == "X":
                    if ( self.getNumberOfNeighbors(i,j) < 2 or self.getNumberOfNeighbors(i,j) > 3 ) : #TOD
                        clone[i][j] = "_"
                else:
                     if (self.getNumberOfNeighbors(i,j) == 3):  #Geburt
                        clone[i][j] = "X"
                j=j+1
            i=i+1
        self.matrix=clone   #switchover, Matrixfeld auf den neuen Stand bringen, der im Clone erstellt wurde
         

    def print_matrix(self):
        for curRow in self.matrix:
            for curCol in curRow:
                print(curCol,end = " ")
            print("|")

        
    def addStartObj(self, startObj):
        deltaR=16
        deltaC=16
        #es fehlt die Ausnahmebehandlung, Matrixgrenzen!
        i=0
        for curRow in startObj:
            j=0
            for curCol in curRow:
                if curCol == "X":
                    #print ("addStartObj", i, j, "old", self.matrix[i][j] )
                    self.matrix[i+deltaR][j+deltaC]=curCol
                j=j+1
            i=i+1





class Game:
    maxIterations = 100
    currentIteration=0
    currentField = Field(1,1)
    fieldHistory = []
    
    def __init__(self,iterations): 
        self.maxIterations=iterations
        
    def initGame(self, initialField):
        self.currentIteration=0
        self.currentField = initialField
        
    
    
    def playGame(self):
        for i in range(self.maxIterations):
            # Clearing the Screen
            os.system('cls')
            print("EvoNr.: ", self.currentIteration)
            self.currentField.print_matrix()
            time.sleep(100/1000)
            
            self.currentField.evolution()
            self.currentIteration+=1
            self.fieldHistory.append(self.currentField)
            
            
        

if __name__ == "__main__":
    myField = Field(40,40)
    myField.init_matrix()
    #print( myField.matrix)
    
    
    #startObj2=[['_','X','_'], ['X','_','X'], ['_','X','_']]
    startObj2=[['_','_','_'],
               ['X','X','X'], 
               ['_','_','_']]
               
    startGl  =[['_','X','_'],
               ['_','_','X'], 
               ['X','X','X']]
               
               
               
    startMu2  =[['X','X','X'],
                ['X','_','X'], 
                ['X','_','X'],
                ['_','_','_'],
                ['X','_','X'],
                ['X','_','X'],
                ['X','X','X']
               ]               

    startPento=[['_','X','X'],
                ['X','X','_'], 
                ['_','X','_']
               ]


    #print(startObj2)
    myField.addStartObj(startPento)
    
    myGame=Game(500)
    myGame.initGame(myField)
    myGame.playGame()