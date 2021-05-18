CharacterFile = open("FCT\\CharactersInit\\CharacterList.txt", "r", encoding="utf8")
CharacterList = []
print("Help!")
for i in range(1348):
    CharacterListLine = CharacterFile.readline()
    CharacterList.append(CharacterListLine)

FranchiseNum = 0
CharacterNum = 0
print(str(len(CharacterList)))
for line in CharacterList:
    if line == "\n":
        FranchiseNum+=1
    else:
        CharacterNum+=1
print(str(len(CharacterList)))
print("Characters: " + str(CharacterNum))
print("Franchises: " + str(FranchiseNum))