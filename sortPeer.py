#Alphabetizes peer.txt again and saves it under new.txt
def findEmojiID(personName):
    peerFile = open("peer.txt", "r")
    peerFull = peerFile.read()
    peer = peerFull.split("\n")
    peoplePeerIndex = []
    personIndex = peer.index(personName)
    personID = peer[personIndex + 1]
    return personID
#Gets the emoji ID from the person's name

peerFile = open("peer.txt", "r")
peer = peerFile.read()
peerArray = peer.split("\n")
firstChars = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital = {'A': 'a', 'B': 'b', 'C': 'c', "D": "d", 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', "T": 't', 'U': 'u', 'V': 'v', 'W': 'w', "X": 'x', "Y": 'y', 'Z': 'z'}
for num in range(26):
    char = []
    firstChars.append(char)
for i in peerArray:
    if peerArray.index(i) % 2 != 1:
        print("Index: " + str(peerArray.index(i)))
        personArray = list(i)
        firstChar = personArray[0]
        nonCap = firstChar
        print("First Char: " + firstChar)
        if firstChar in capital:
            nonCap = capital[firstChar]
        letterIndex = alphabet.index(nonCap)
        firstChars[letterIndex].append(i)

newFile = open("new.txt", "w")
for charList in firstChars:
    for name in charList:
        print(name)
        newFile.write(name + '\n')
        newFile.write(str(findEmojiID(name)) + '\n')
newFile.close()
        