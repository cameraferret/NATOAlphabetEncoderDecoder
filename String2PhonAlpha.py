#User inputs string and NATO phonetic alphabet is returned.
#NATO phonetic encoder
#Randolph K. Wilson III - randolphkwilson3@gmail.com

import clipboard as board

def encodeUserMsg(userInput):
    msg = ""
    NATObet = {
                'A' : "Alpha ",
                'B' : "Bravo ",
                'C' : "Charlie ",
                'D' : "Delta ",
                'E' : "Echo ",
                'F' : "Foxtrot ",
                'G' : "Golf ",
                'H' : "Hotel ",
                'I' : "India ",
                'J' : "Juliet ",
                'K' : "Kilo ",
                'L' : "Lima ",
                'M' : "Mike ",
                'N' : "November ",
                'O' : "Oscar ",
                'P' : "Papa ",
                'Q' : "Quebec ",
                'R' : "Romeo ",
                'S' : "Sierra ",
                'T' : "Tango ",
                'U' : "Uniform ",
                'V' : "Victor ",
                'W' : "Whiskey ",
                'X' : "X-ray ",
                'Y' : "Yankee ",
                'Z' : "Zulu ",
                ' ' : "[space] "
                }
    for ittr in range(len(userInput)):
        if(userInput[ittr].isalpha() or userInput[ittr] == ' '):
            msg += (NATObet[userInput[ittr]])
    board.copy(msg)
    print(msg+"\n")




userInput = input("Please enter a string: ")
encodeUserMsg(userInput.upper())

while True:
    userInput = input("Would you like to continue? Enter 0 to quit or press return to continue: ")
    if (userInput == '0'):
        break
    encodeUserMsg(userInput.upper())