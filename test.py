import xlwt

#wb = xlwt.Workbook()
#ws = wb.add_sheet("Sheet 1")
#ww = wb.add_sheet("Winners")
#wl = wb.add_sheet("Losers")

bigFile = open("LogCADiscord.txt", "r")
peopleFile = open("people.txt", "r")

bracketsFull = bigFile.read()
peopleFull = peopleFile.read()
people = peopleFull.split("\n")
oeople = peopleFull.split("\n")
brackets = bracketsFull.split("\n")

peopleScoreRaw = {}
totalVotesThatMatch = {}

passed = []
competitiedList = []

for match in brackets:
    matchInfo = match.split("|")
    competitiedList.append(matchInfo[0])
    competitiedList.append(matchInfo[1])
    if matchInfo[3] == "Tie!":
        passed.append(matchInfo[0])
        passed.append(matchInfo[1])
    else:
        passed.append(matchInfo[3])
    score = matchInfo[2].split("-")
    peopleScoreRaw[matchInfo[0]] = int(score[0]) - 1
    peopleScoreRaw[matchInfo[1]] = int(score[1]) - 1
    
    totalVotesThatMatch[matchInfo[0]] = (int(score[0]) + int(score[1])) - 2
    totalVotesThatMatch[matchInfo[1]] = (int(score[0]) + int(score[1])) - 2

peopleOrig = len(people)
for person in oeople:
    if person in competitiedList:
        people.remove(person)
writeFile = open("CABracket.txt", "w")
for person in passed:
    writeFile.write(person+"\n")

foo = 0
win = 0
lose = 0
for person in oeople:
    lateral = 0
    if peopleScoreRaw[person] / totalVotesThatMatch[person] == 0:
        print(person)
    #ws.write(foo, lateral, person)
    #ws.write(foo, lateral+1, str(peopleScoreRaw[person]))
    #ws.write(foo, lateral+2, str(totalVotesThatMatch[person]))
    #if person in passed:
        #ww.write(win, lateral, person)
        #ww.write(win, lateral+1, str(peopleScoreRaw[person]))
        #ww.write(win, lateral+2, str(totalVotesThatMatch[person]))
        #win+=1
    #else:
        #wl.write(lose, lateral, person)
        #wl.write(lose, lateral+1, str(peopleScoreRaw[person]))
        #wl.write(lose, lateral+2, str(totalVotesThatMatch[person]))
        #lose+=1
    foo+=1
writeFile.close()
#wb.save("Information2.xls")
print(str(peopleOrig) + "|" + str(len(competitiedList)) + "|" + str(len(people)))