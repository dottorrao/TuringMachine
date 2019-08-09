from pathlib import Path

class Tape:

    def __init__(self, id, name, description):
        self.name = name
        self.id = id
        self.description = description
        self.cells = []
    
    def readInput(self):
        tape = Path("./tape.tm")
        if tape.is_file():
           tape = open("./tape.tm","r")
           content = tape.readline()
           self.cells = content.split(",")
        else:
            raise Exception ("Missing tape.tm file")

    def getInput(self):
        return self.cells