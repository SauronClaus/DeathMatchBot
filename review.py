testFile = open("test2.txt", "r", encoding='utf8').read().split("\n")
deathFile = open("Faculty Death Match.txt", "r", encoding='utf8').read().split("\n")
finalFile = open("Faculty Death Match2.txt", "w", encoding='utf8')
people = []
peopleCorrect = []
peopleID2 = {}
peopleID1 = {}

for person in testFile:
    personName = person.split("|")[0]
    people.append(personName)
    peopleID2[personName] = person.split("|")[1]


for person in deathFile:
    personName = person.replace(" ", "")
    peopleCorrect.append(person)
    #print(personName)
    if not personName in people:
        print("Unfound! " + personName)

for person in peopleCorrect:
    personName = person.replace(" ", "")

    peopleID1[person] = peopleID2[personName]

for person in peopleID1.keys():
    finalFile.write(person + "|" + peopleID1[person] + "\n")