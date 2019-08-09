from state import State
from writerLog import WriterLog
from tape import Tape

S1 = State("Q0","Q0","Initial state")
print (S1.getDetails())

WL = WriterLog (".\\","TuringLog.txt")
WL.writeLog ("Questo e' un messaggio di prova")

message = S1.getDetails()
WL.writeLog ( message )

TP = Tape("T1","T1","Tape")
try:
    TP.readInput()
    print ( TP.getInput() )
    WL.writeLog ( str( TP.getInput() ) )
except Exception as e:
    print (e)
    WL.writeLog ( str(e) )
