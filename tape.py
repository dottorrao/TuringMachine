from pathlib import Path
from configurator import Configurator

class Tape:

    def __init__(self,path,file,separator):
        self.cells = []
        self.path = path
        self.file = file
        self.separator = separator
    
    def readInput(self):
        fullFileName = self.path+self.file
        tape = Path( fullFileName )
        if tape.is_file():
           tape = open(fullFileName,"r")
           content = tape.readline()
           self.cells = content.split( self.separator )
        else:
            raise Exception ("Missing tape file")

    def getInput(self):
        return self.cells
    