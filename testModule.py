from state import State
from writerLog import WriterLog

S1 = State("Q0","Q0","Initial state")
print (S1.getDetails())

WL = WriterLog (".\\","TuringLog.txt")
WL.writeLog ("Questo e' un messaggio di prova")

message = S1.getDetails()
WL.writeLog ( message 