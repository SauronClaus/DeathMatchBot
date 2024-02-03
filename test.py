




characters = open("mhaCharacters.txt", "r", encoding='utf-8')
suggestionsFull = characters.read()
suggestions = suggestionsFull.split("\n")

for character in suggestions:
    newFile = open("MHA Characters\\" + character + ".txt", "w", encoding='utf-8')
    newFile.write(character)