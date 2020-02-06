#This file sorts up places.txt into a list without the "in"s and "on"s, and saves it in new.txt. 

placeFile = open("places.txt", "r")
placeArray = placeFile.read().split("\n")
remakeString = ""
for i in placeArray:
    words = i.split(" ")
    words.pop(0)
    newWord = ""
    for word in words:
        newWord = newWord + word + " "
    newWord.strip()
    remakeString = remakeString + newWord + "\n"
remakeString.strip()
newFile = open("new.txt", "w")
newFile.write(remakeString)
newFile.close()

