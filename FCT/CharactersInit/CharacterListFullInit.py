CharactersFile = open("FCT\\CharactersInit\\NewCharacterList.txt", "r", encoding="utf8")

fullFile = CharactersFile.read()
characterList = fullFile.split("\n")

for character in characterList:
    characterName = character.split(" (")[0]
    franchise = character.split(" (")[1]
    franchise = franchise[:len(franchise)-1:]
    print("Character Name: " + str(characterName))

    print("Franchise: " + str(franchise))
    CharacterFile = open("FCT\\Characters\\" + characterName + ".txt", "w")
    CharacterFile.write(characterName + "\n")
    CharacterFile.write(franchise + "\n")
    CharacterFile.write(characterName.split(" ")[0])