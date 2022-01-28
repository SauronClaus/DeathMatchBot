peopleFile = open("people.txt", encoding='utf8')

people = peopleFile.read().split("\n")
newPeople = []
exit = ":D"
personAnswer = ":("
while personAnswer != exit:
    personAnswer = input("Enter Person to Check: ")
    if personAnswer in people:
        print(personAnswer + " is already in people!")
    else:
        print("Adding " + personAnswer + " to list.")
        peopleNewFile = open("NewPeopleToAdd.txt", "a")
        peopleNewFile.write("\n" + personAnswer)