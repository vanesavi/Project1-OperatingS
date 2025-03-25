from datetime import datetime
import sys


# COLLECTS INPUT FROM COMMAND LINE
if len(sys.argv) != 2:
    sys.exit()
arg1 = sys.argv[1]



loggingQuitBool = True



def logToFile(fileName,message):
    now = datetime.now()
    formattedTime = now.strftime("%Y-%B-%d %H:%M")
    logFile = open(fileName, "+a")
    messageOutput = str(formattedTime)+" "+message+"\n"
    logFile.write(messageOutput)
    logFile.close()
    # print(formattedTime)


while loggingQuitBool == True:
    messageInput = input()
    if messageInput.upper() == "QUIT":
        loggingQuitBool = False
    elif messageInput.upper() == "!INIT_COMMENT!":
        logToFile(arg1,"[START] Logging started.")
    else:
        logToFile(arg1,messageInput)