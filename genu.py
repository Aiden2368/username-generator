import random, sys, os, getopt

def ErrorQuit(errMSG):
    print(errMSG)
    sys.exit()

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:l:w:")
except Exception as e:
    ErrorQuit(f"ERROR: {e}")

ADJECTIVES = open(os.path.dirname(os.path.realpath(__file__)) + "/resources/adjectives.txt", "r").read().splitlines()
NOUNS = open(os.path.dirname(os.path.realpath(__file__)) + "/resources/nouns.txt", "r").read().splitlines()
N_USERNAMES = 1
USE_USRLEN = False
MAX_USERLEN = 8
HAS_ARGS = len(opts) > 0
AMOUNT_WORDS_IN_USRNAME = 2

if HAS_ARGS:
    for opt, arg in opts:
        if opt == "-n":
            N_USERNAMES = int(arg)
        if opt == "-l":
            USE_USRLEN = True
            MAX_USERLEN = int(arg)
        if opt == "-w":
            AMOUNT_WORDS_IN_USRNAME = int(arg)

def genUsername(useSpecificLen, maxUsrLen, amountOfWords):
    listToUse = getListItemsByLength(NOUNS, maxUsrLen) if useSpecificLen else NOUNS
    toReturn = ""
    i = amountOfWords
    while i > 0:
        i -= 1
        toReturn += f"{random.choice(listToUse)}"
    return toReturn
def getListItemsByLength(varList, stringLen):
    toReturnList = []
    for item in varList:
        if len(item) <= stringLen:
            toReturnList.append(item)
    return toReturnList

# Generate username(s)
printText = ""
i = N_USERNAMES
while i > 0:
    i -= 1
    printText += f"{genUsername(USE_USRLEN, MAX_USERLEN, AMOUNT_WORDS_IN_USRNAME)}"
    if i > 0:
        printText += "\n"
print(printText)