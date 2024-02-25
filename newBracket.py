bracketFile = open("LogMHAMatch.txt", "r", encoding='utf-8')
newBracket = open("OASISBracketRound2.txt", "w", encoding='utf-8')
bracket = bracketFile.read().split("\n")

personFile = open("mhaCharacters.txt", "r", encoding='utf-8')
people = personFile.read().split("\n")

personFile.close()
bracketFile.close()

movingOn = []
for match in bracket:
    if match != "":
        matchInfo = match.split("|")
        print(match)
        if matchInfo[3] == "Tie":
            movingOn.append(matchInfo[0])
            movingOn.append(matchInfo[1])
        else:
            movingOn.append(matchInfo[3])

for person in movingOn:
    if person in people:
        newBracket.write("\n" + person)
    else:
        print(person + " is not in people!")

newBracket.close()