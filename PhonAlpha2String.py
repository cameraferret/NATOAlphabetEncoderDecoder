#User inputs string and NATO phonetic alphabet is returned.
#NATO phonetic encoder
#Randolph K. Wilson III - randolphkwilson3@gmail.com

import clipboard as board

def decodeUserMsg(userInput):
    msg = ""
    DECODEbet = {
                "ALPHA" : "A",
                "BRAVO" : "B",
                "CHARLIE" : "C",
                "DELTA" : "D",
                "ECHO" : "E",
                "FOXTROT" : "F",
                "GOLF" : "G",
                "HOTEL" : "H",
                "INDIA" : "I",
                "JULIET" : "J",
                "KILO" : "K",
                "LIMA" : "L",
                "MIKE" : "M",
                "NOVEMBER" : "N",
                "OSCAR" : "O",
                "PAPA" : "P",
                "QUEBEC" : "Q",
                "ROMEO" : "R",
                "SIERRA" : "S",
                "TANGO" : "T",
                "UNIFORM" : "U",
                "VICTOR" : "V",
                "WHISKEY" : "W",
                "X-RAY" : "X",
                "YANKEE" : "Y",
                "ZULU" : "Z",
                "[SPACE]": " ",
                " " : " "
                }

    # if(str(userInput[0].find(str(DECODEbet.keys())))):
    #     print(str(userInput[0].find(str(DECODEbet.keys()))))
    # for x in range(len(userInput)):
    #     if(str(userInput[x]) in str(DECODEbet.keys())):
    #         print(str(userInput[x]) in str(DECODEbet.keys()))

    for ittr in range(len(userInput)):
        if((str(userInput[ittr]) in DECODEbet)):
            msg += (DECODEbet[userInput[ittr]])


    print(msg+"\n")




userInput = input("Please enter a Nato string to decode: ")
decodeUserMsg(userInput.upper().split())

while True:
    userInput = input("Would you like to continue? Enter 0 to quit or press return to continue: ")
    if (userInput == '0'):
        break
    decodeUserMsg(userInput.upper().split())