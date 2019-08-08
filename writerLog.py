from datetime import date
import datetime

class WriterLog:
    def __init__(self, filePath, fileName):
        self.filePath = filePath
        self.fileName = fileName
        self.fullLogName = self.filePath + "\\" + str(date.today()) + "_" + self.fileName
        self.logFile = open(self.fullLogName,"a")
        self.logFile.close() 
    
    def writeLog (self,message):
        self.logFile = open(self.fullLogName,"a")
        self.logFile.write(str(datetime.datetime.now().isoformat()) + ": " + message)
        self.logFile.write("\n")
        self.logFile.close() 