import random

import discord

from generation import generateWeaponPairTier
from generation import generateAdjectivePairTier
from generation import generatePlaceTier

from generation import generateWeaponPair
from generation import generateAdjectivePair
from generation import generatePlace
from generation import generateTime
from generation import generateJeopardyCategory
from generation import generateBachelor
from generation import generateLifeSpeedrunConditions
from generation import generatePlaceTierCleaning

from embeds import createWeaponEmbed
from embeds import createPlaceLongEmbed
from embeds import createAdjectiveEmbed
from embeds import createContestEmbed
from embeds import createDrinkEmbed
from embeds import createFoodEmbed
from embeds import createFranchiseEmbed
from embeds import createJudgeEmbedCleaning
from embeds import createJudgeEmbedCooking
from embeds import createMarioMinigameEmbed
from embeds import createPieEmbed
from embeds import createSongEmbed
from embeds import createSpaceShipEmbed
from embeds import createJudgeThreeSet

def generateContest():
    contestFile = open("Contests\\ContestList.txt", "r")
    contestFileFull = contestFile.read()
    contestFileArray = contestFileFull.split("\n")

    adjectivesUsed = True
    weaponsUsed = True
    placesUsed = True

    adjectivesFull = ""
    weaponsFull = ""
    placesFull = ""

    coinFlip = random.randint(1,4)
    if coinFlip == 1:
        print("Classic Death Match!")
        adjectivesFull = "All"
        weaponsFull = "All"
        placesFull = "All"
        contest = "Death Match Classic"
        variant = "Classic"
    else:
        randomNum = random.randint(0,len(contestFileArray)-1)
        print(contestFileArray[randomNum] + "!")
        contest = contestFileArray[randomNum]

        variantFile = open("Contests\\" + contest + "\\variants.txt", "r")
        variantFull = variantFile.read()
        variantArray = variantFull.split("\n")

        randomNum = random.randint(0,len(variantArray)-1)
        variant = variantArray[randomNum]
        print("Variant: " + variant)

        adjectivePair = []
        weaponPair = []
        place = ""

        placesFile = open("Contests\\" + contest + "\\locations.txt", "r")
        placesFull = placesFile.read()

        weaponsFile = open("Contests\\" + contest + "\\" + variant+ "weapons.txt", "r")
        weaponsFull = weaponsFile.read()

        adjectivesFile = open("Contests\\" + contest + "\\" + variant + "adjectives.txt", "r")
        adjectivesFull = adjectivesFile.read()
    if adjectivesFull == "None":
        adjectivesUsed = False
    else:
        if adjectivesFull == "All":
            adjectivePair = generateAdjectivePair()
        else:
            adjectivePair = generateAdjectivePairTier(adjectivesFull)
    print("Adjectives Generated!")
    placic = []
    if placesFull == "None":
        placesUsed = False
    else:
        if placesFull == "All":
            place = generatePlace()
        else:
            if placesFull == "Cleaning Competition":
                placic = generatePlaceTierCleaning(placesFull)
                place = placic[0]
            else:
                place = generatePlaceTier(placesFull)
    print("Places Generated!")

    if weaponsFull == "None":
        weaponsUsed = False
    else:
        if weaponsFull == "All":
            weaponPair = generateWeaponPair()
        else:
            weaponPair = generateWeaponPairTier(weaponsFull)
    
    print("Weapons Generated!")
    specialItems = {}
    if contest == "Cleaning Competition":
        file = open("Contests\\" + contest + "\\" + "judges.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")

        judgeSet = fileArray[int(placic[1])]
        judges = judgeSet.split(", ")
        for judge in judges:
            embed = createJudgeEmbedCleaning(judge, "Cleaning", judgeSet)
            specialItems[judge] = embed
    if contest == "Cooking Contest":
        file = open("Contests\\" + contest + "\\" + "dishes.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        dish = fileArray[randomNum]
        specialItems[dish] = createFoodEmbed(dish)

        file = open("Contests\\" + contest + "\\" + "judges.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNumbers = []
        for i in range(4):
            randomNum = random.randint(0, len(fileArray)-1)
            randomNumbers.append(randomNum)
        file.close()
        for rng in randomNumbers:
            judge = fileArray[rng]
            specialItems[judge] = createJudgeEmbedCooking(judge, "Cooking")
            print("Judge: " + judge)
    if contest == "Drinking Contest":
        file = open("Contests\\" + contest + "\\" + "drinks.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        drink = fileArray[randomNum]
        specialItems[drink] = createDrinkEmbed(drink)
    if contest == "Get Sued by Nintendo":
        file = open("Contests\\" + contest + "\\" + "franchise.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        franchise = fileArray[randomNum]
        specialItems[franchise] = createFranchiseEmbed(franchise)
    if contest == "Karaoke Contest":
        file = open("Contests\\" + contest + "\\" + "songs.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        song = fileArray[randomNum]
        specialItems[song] = createSongEmbed(song)
    if contest == "Mario Party 10":
        file = open("Contests\\" + contest + "\\" + "minigames.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        minigame = fileArray[randomNum]
        specialItems[minigame] = createMarioMinigameEmbed(minigame)
    if contest == "Pie Eating Contest":
        file = open("Contests\\" + contest + "\\" + "pies.txt", "r")
        fileFull = file.read()
        fileArray = fileFull.split("\n")
        randomNum = random.randint(0, len(fileArray)-1)
        file.close()
        pie = fileArray[randomNum]
        specialItems[pie] = createPieEmbed(pie)
    if contest == "First to Blow Up the Death Star I":
        specialItems["X-wing"] = createSpaceShipEmbed("X-wing")        
    print("Prep for return")
    contestInformation = [contest, variant]
    returnVariables = [adjectivePair, weaponPair, place, specialItems, contestInformation]
    return returnVariables
    #Return: Adjectives, Weapons, Places, Contest Information [contest name, variant name]
#Generates a contest!
def generateRegular(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#The regular syntax. Should be used for most contests.
def generateCleaningCompetition(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    print("Special Items:")
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
        print(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s) (judged by [%s](%s), [%s](%s), and [%s](%s))" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]], specialItems[1], competitionInfo[4][specialItems[1]], specialItems[2], competitionInfo[4][specialItems[2]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a cleaning contest.
def generateCookingContest(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    print("Special Items:")
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
        print(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])
    time = generateTime()

    specialItems = "making [%s](%s) in %s judged by [%s](%s), [%s](%s), and [%s](%s)" % (specialItems[0], competitionInfo[4][specialItems[0]], time, specialItems[1], competitionInfo[4][specialItems[1]], specialItems[2], competitionInfo[4][specialItems[2]], specialItems[3], competitionInfo[4][specialItems[3]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s (%s) [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, specialItems, place, competitionInfo[3][place])
    return matchMessage
#Used to generate a cooking competition.
def generateDrinkingContest(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    print("Special Items:")
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
        print(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s) (drinking [%s](%s))" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used to generate a drinking contest.
def generateGetSuedNintendo(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    print("Special Items:")
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
        print(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s) (for violating copyright rules on the [%s franchise](%s))" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s to %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used to generate the Get Sued by Nintendo competition
def generateJeopardy(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    print("Special Items:")
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
        print(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    category = generateJeopardyCategory()
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s) contest (Category: %s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], category)

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used to generate the Jeopardy competition
def generateKaraoke(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    competition = "[%s (%s)](%s), singing [%s](%s), " % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used to generate a Karaoke competition
def generateBachelorLong(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    humanWooed = generateBachelor(True)
    competition = "[%s (%s)](%s) with %s" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], humanWooed)

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Lasting Longer in the Bachelor competition
def generateBacheloretteLong(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    humanWooed = generateBachelor(False)
    competition = "[%s (%s)](%s) with %s" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], humanWooed)

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Lasting Longer in the Bachelorette competition
def generateBachelorShort(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    humanWooed = generateBachelor(True)
    competition = "[%s (%s)](%s) with %s" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], humanWooed)

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Lasting the Shortest in the Bachelor competition
def generateBacheloretteShort(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    humanWooed = generateBachelor(False)
    competition = "[%s (%s)](%s) with %s" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], humanWooed)

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Lasting the Shortest in the Bachelorette competition
def generateLifeSpeedrun(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    speedRunConditions = generateLifeSpeedrunConditions()
    competition = "[%s (%s)](%s) (Conditions: %s, %s, %s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], speedRunConditions[0], speedRunConditions[1], speedRunConditions[2])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Life Speedrun competition
def generateMarioParty10(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s) (Minigame: [%s](%s))" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating the Mario Party 10 competition
def generatePieEatingContest(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s) eating [%ss](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo], specialItems[0], competitionInfo[4][specialItems[0]])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a pie eating contest
def generateFirstTo(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s as the %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating "First to" contests!
def generateContestAddition(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s) competition](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a classic contest, but with a "competition" in the contest name
def generateContestMatch(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s) match](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a classic contest, but with a "match" in the contest name
def generateContestGameOf(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a game of %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a classic contest, but with a "game of" in the contest name
def generateContestElections(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    return matchMessage
#Used for generating a classic contest, but with for elections
def generateHDMClassic(competitionInfo, matchRanked):
    #matchInfo = [people, adjectives, weapons, places, specialItems, contestInfo, variant]
    people = []
    adjectives = []
    weapons = []
    specialItems = []
    place = ""

    contestInfo = list(competitionInfo[5].keys())[0]

    print("People:")
    for person in competitionInfo[0]:
        people.append(person)
        print(person)
    print("Adjectives:")
    for adjective in competitionInfo[1]:
        adjectives.append(adjective)
        print(adjective)
    print("Weapons:")
    for weapon in competitionInfo[2]:
        weapons.append(weapon)
        print(weapon)
    for specialItem in competitionInfo[4]:
        specialItems.append(specialItem)
    print("Places:")
    for placen in competitionInfo[3]:
        place = placen
        print(place)
    
    person1 = "[%s](%s)" % (people[0], competitionInfo[0][people[0]])
    person2 = "[%s](%s)" % (people[1], competitionInfo[0][people[1]])
    
    competition = "[%s (%s)](%s)" % (contestInfo, competitionInfo[6], competitionInfo[5][contestInfo])

    adjective1 = ""
    adjective2 = ""
    weapon1 = ""
    weapon2 = ""

    if len(adjectives) >= 2:
        adjective1 = "[%s](%s)" % (adjectives[0], competitionInfo[1][adjectives[0]])
        adjective2 = "[%s](%s)" % (adjectives[1], competitionInfo[1][adjectives[1]])
    if len(weapons) >= 2:
        weapon1 = "with [%s](%s)" % (weapons[0], competitionInfo[2][weapons[0]])
        weapon2 = "with [%s](%s)" % (weapons[1], competitionInfo[2][weapons[1]])
    
    matchMessage = "%s%s %s vs %s%s %s in a %s [%s](%s)" % (adjective1, person1, weapon1, adjective2, person2, weapon2, competition, place, competitionInfo[3][place])
    print("Match Length: " + str(len(matchMessage)))
    return matchMessage
#generates an HDM death match
def generateMatchMessage(competitionInfo, matchRanked):
    print("Competition Info len: " + str(len(competitionInfo)))

    print("---Passed!---")
    print(str(competitionInfo[5].keys()))
    competitionType = list(competitionInfo[5].keys())[0]
    print("Competition: " + competitionType + "\nVariant: " + competitionInfo[6])
    matchMessage = ""

    if competitionType == "Cleaning Competition":
        print("Generating " + competitionType)
        matchMessage = generateCleaningCompetition(competitionInfo, matchRanked)
    else:
        if competitionType == "Cooking Contest":
            print("Generating " + competitionType)
            matchMessage = generateCookingContest(competitionInfo, matchRanked)
        else:
            if competitionType == "Drinking Contest":
                print("Generating " + competitionType)
                matchMessage = generateDrinkingContest(competitionInfo, matchRanked)
            else:
                if competitionType == "Get Sued by Nintendo":
                    print("Generating " + competitionType)
                    matchMessage = generateGetSuedNintendo(competitionInfo, matchRanked)
                else: 
                    if competitionType == "Jeopardy":
                        print("Generating " + competitionType)
                        matchMessage = generateJeopardy(competitionInfo, matchRanked)
                    else: 
                        if competitionType == "Karaoke Contest":
                            print("Generating " + competitionType)
                            matchMessage = generateKaraoke(competitionInfo, matchRanked)
                        else:
                            if competitionType == "Lasting Longer in the Bachelor":
                                print("Generating " + competitionType)
                                matchMessage = generateBachelorLong(competitionInfo, matchRanked)
                            else:
                                if competitionType == "Lasting Longer in the Bachelorette":
                                    print("Generating " + competitionType)
                                    matchMessage = generateBacheloretteLong(competitionInfo, matchRanked)
                                else:
                                    if competitionType == "Lasting the Shortest in the Bachelor":
                                        print("Generating " + competitionType)
                                        matchMessage = generateBachelorShort(competitionInfo, matchRanked)
                                    else:
                                        if competitionType == "Lasting the Shortest in the Bachelorette":
                                            print("Generating " + competitionType)
                                            matchMessage = generateBacheloretteShort(competitionInfo, matchRanked)
                                        else:
                                            if competitionType == "Life Speedrun":
                                                print("Generating " + competitionType)
                                                matchMessage = generateLifeSpeedrun(competitionInfo, matchRanked)
                                            else:
                                                if competitionType == "Mario Party 10":
                                                    print("Generating " + competitionType)
                                                    matchMessage = generateMarioParty10(competitionInfo, matchRanked)
                                                else:
                                                    if competitionType == "Pie Eating Contest":
                                                        print("Generating " + competitionType)
                                                        matchMessage = generatePieEatingContest(competitionInfo, matchRanked)
                                                    else:
                                                        if competitionType == "Death Match Classic":
                                                            print("Generating " + competitionType)
                                                            matchMessage = generateHDMClassic(competitionInfo, matchRanked)
                                                        else:
                                                            if competitionType == "First to Throw the One Ring in Mount Doom" or competitionType == "First to Murderhobo the Odyssey" or competitionType == "First to Blow Up the Death Star I" or competitionType == "First to Become a Saint" or competitionType == "First to Kill Lord Voldemort":
                                                                print("Generating " + competitionType)
                                                                matchMessage = generateFirstTo(competitionInfo, matchRanked)
                                                            else:
                                                                if competitionType == "Deadlift" or competitionType == "Pole Vault" or competitionType == "Mini Golf" or competitionType == "Discus" or competitionType == "Chainsaw Juggling" or competitionType == "Dance Dance Revolution" or competitionType == "Losing a Chess Game" or competitionType == "Racewalking" or competitionType == "Holding Breath Underwater":
                                                                    print("Generating " + competitionType)
                                                                    matchMessage = generateContestAddition(competitionInfo, matchRanked)
                                                                else:
                                                                    if competitionType == "Chessboxing" or competitionType == "Fencing":
                                                                        print("Generating " + competitionType)
                                                                        matchMessage = generateContestMatch(competitionInfo, matchRanked)
                                                                    else:
                                                                        if competitionType == "Chess" or competitionType == "Monopoly" or competitionType == "Minecraft Bedwars" or competitionType == "Mahjong" or competitionType == "Dodgeball" or competitionType == "Super Smash Brothers":
                                                                            print("Generating " + competitionType)
                                                                            matchMessage = generateContestGameOf(competitionInfo, matchRanked)
                                                                        else:
                                                                            if competitionType == "Losing a Presidential Election" or competitionType == "An Episode of Fear Factor":
                                                                                print("Generating " + competitionType)
                                                                                matchMessage = generateContestElections(competitionInfo, matchRanked)
                                                                            else:
                                                                                print("Generating " + competitionType)
                                                                                matchMessage = generateRegular(competitionInfo, matchRanked)
    print("Match Message: " + matchMessage[0:1:].capitalize() + matchMessage[1::] + "!")
    matchMessage = matchMessage[0:1:] + matchMessage[1:2:].capitalize() + matchMessage[2:len(matchMessage)-5:].strip() + matchMessage[len(matchMessage)-4::] + "!"
    print("~" + matchMessage[len(matchMessage)-6:len(matchMessage)-5:] + "~")
    return matchMessage
#Sets up the competition and serves as a staging ground.