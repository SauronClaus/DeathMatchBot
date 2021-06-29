StoryFiles = open("FCT\\validFranchises.txt", "r", encoding="utf8")

fullFile = StoryFiles.read()
storyList = fullFile.split("\n")

for story in storyList:
    print("Story: " + str(story))

    CharacterFile = open("FCT\\Tales\\" + story + ".txt", "w")
    CharacterFile.write(story + "\n")