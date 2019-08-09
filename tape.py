from pathlib import Path
from configurator import Configurator

class Tape:

    def __init__(self, id, name, description):
        self.name = name
        self.id = id
        self.description = description
        self.cells = []
        CNF = Configurator()
        self.ConfData = CNF.getConfigData()
    
    def readInput(self):
        tape = Path("./tape.tm")
        if tape.is_file():
           tape = open(self.ConfData['tape']['filename'],"r")
           content = tape.readline()
           self.cells = content.split(self.ConfData['tape']['separator'])
        else:
            raise Exception ("Missing tape.tm file")

    def getInput(self):
        return self.cells