from configurator import Configurator
from writerLog import WriterLog
from tape import Tape

class TuringMachine:

    def __init__(self):
        self.CNF = Configurator()
        self.ConfData = self.CNF.getConfigData()
        self.WL = WriterLog ( self.ConfData['logfile']['filepath'], self.ConfData['logfile']['filename'])
        self.TP = Tape (self.ConfData['tape']['filepath'], self.ConfData['tape']['filename'], self.ConfData['tape']['separator'])
        self.TP.readInput()
    
    def getConfigData(self):
        print ( self.ConfData )
    
    def writeLog (self,message):
        self.WL.writeLog(message)

    def getInput(self):
        print (self.TP.getInput() )

TM = TuringMachine()
TM.getConfigData()
TM.writeLog("Test message log")
TM.getInput()

