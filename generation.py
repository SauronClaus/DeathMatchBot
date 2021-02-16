import discord
from discord.utils import get

import random

def generatePerson():
    peerFile = open("peer.txt", "r")
    peerArray = peerFile.read().split("\n")
    personFile = open("people.txt", "r")
    personArray = personFile.read().split("\n")
    randomNum = random.randint(0, len(personArray)-1)
    person = personArray[randomNum]
    indexOfID = peerArray.index(person) + 1
    personInfo = [person, "DEPRECATED", peerArray[indexOfID]]
    return personInfo
#Returns a list with the person, emoji object, and the person's emoji id. 
def generateWeapon():
    weaponTierFile = open("Armory\\Tiers\\weaponTiers.txt", "r")
    weaponTierFull = weaponTierFile.read()
    weaponTierArray = weaponTierFull.split('\n')
    weaponTier1Num = random.randint(0, len(weaponTierArray)-1)
    weaponTier1Name = "Armory\\Tiers\\" + weaponTierArray[weaponTier1Num] + ".txt"
    weaponFile1 = open(weaponTier1Name, "r")
    weaponSet1 = weaponFile1.read().split('\n')
    randomNum = random.randint(0, len(weaponSet1)-1)
    weapon = weaponSet1[randomNum]
    return weapon
#Returns a random weapon
def generateWeaponPair():
    weaponTierFile = open("Armory\\Tiers\\weaponTiers.txt", "r")
    weaponTierFull = weaponTierFile.read()
    weaponTierArray = weaponTierFull.split('\n')
    weaponTier1Num = random.randint(0, len(weaponTierArray)-1)
    weaponTier1Name = "Armory\\Tiers\\" + weaponTierArray[weaponTier1Num] + ".txt"
    weaponFile1 = open(weaponTier1Name, "r")
    weaponSet1 = weaponFile1.read().split('\n')
    randomNum1 = random.randint(0, len(weaponSet1)-1)
    randomNum2 = random.randint(0, len(weaponSet1)-1)
    if randomNum1 == randomNum2:
        while randomNum1 == randomNum2:
            randomNum2 = random.randint(0, len(weaponSet1)-1)
    weapon1 = weaponSet1[randomNum1]
    weapon2 = weaponSet1[randomNum2]
    weaponPair = [weapon1, weapon2]
    return weaponPair
#Generates a tiered pair of weapons. 
def generateAdjective():
    adjectiveTierFile = open("Adjectives\\adjectiveTiers.txt", "r")
    adjectiveTierFull = adjectiveTierFile.read()
    adjectiveTierArray = adjectiveTierFull.split('\n')
    adjectiveTier1Num = random.randint(0, len(adjectiveTierArray)-1)
    adjectiveTier1Name = adjectiveTierArray[adjectiveTier1Num] + ".txt"
    adjectiveFile1 = open("Adjectives\\" + adjectiveTier1Name, "r")
    adjectiveSet1 = adjectiveFile1.read().split('\n')
    randomNum = random.randint(0, len(adjectiveSet1)-1)
    adjective = adjectiveSet1[randomNum]
    return adjective
#Returns a random Adjective
def generateAdjectivePair():
    adjectiveTierFile = open("Adjectives\\adjectiveTiers.txt", "r")
    adjectiveTierFull = adjectiveTierFile.read()
    adjectiveTierArray = adjectiveTierFull.split('\n')
    adjectiveTier1Num = random.randint(0, len(adjectiveTierArray)-1)
    adjectiveTier1Name = adjectiveTierArray[adjectiveTier1Num] + ".txt"
    adjectiveFile1 = open("Adjectives\\" + adjectiveTier1Name, "r")
    adjectiveSet1 = adjectiveFile1.read().split('\n')
    randomNum1 = random.randint(0, len(adjectiveSet1)-1)
    randomNum2 = random.randint(0, len(adjectiveSet1)-1)
    if randomNum1 == randomNum2:
        while randomNum1 == randomNum2:
            randomNum2 = random.randint(0, len(adjectiveSet1)-1)
    adjective1 = adjectiveSet1[randomNum1]
    adjective2 = adjectiveSet1[randomNum2]
    adjectivePair = [adjective1, adjective2]
    return adjectivePair
#Returns a random tiered Adjective pair
def generatePlace():
    places = "Atlas\\places.txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = placeArray[randomNum]
    return place
#Returns a random place
def generatePlaceAdverb():
    places = "Atlas\\placesName.txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = placeArray[randomNum]
    return place
#Returns a random place without the proposition thing ("in", "on", etc.)
def generateWeaponPairTier(tier):
    weaponFile1 = open("Armory\\Tiers\\" + tier + ".txt", "r")
    weaponSet1 = weaponFile1.read().split('\n')
    randomNum1 = random.randint(0, len(weaponSet1)-1)
    randomNum2 = random.randint(0, len(weaponSet1)-1)
    if randomNum1 == randomNum2 and len(weaponSet1) > 1:
        while randomNum1 == randomNum2:
            randomNum2 = random.randint(0, len(weaponSet1)-1)
    weapon1 = weaponSet1[randomNum1]
    weapon2 = weaponSet1[randomNum2]
    weaponPair = [weapon1, weapon2]
    return weaponPair
#Generates a pair of weapons in the specified tier.
def generateAdjectivePairTier(tier):
    adjectiveFile1 = open("Adjectives\\" + tier + ".txt", "r")
    adjectiveSet1 = adjectiveFile1.read().split('\n')
    randomNum1 = random.randint(0, len(adjectiveSet1)-1)
    randomNum2 = random.randint(0, len(adjectiveSet1)-1)
    if randomNum1 == randomNum2:
        while randomNum1 == randomNum2:
            randomNum2 = random.randint(0, len(adjectiveSet1)-1)
    adjective1 = adjectiveSet1[randomNum1]
    adjective2 = adjectiveSet1[randomNum2]
    adjectivePair = [adjective1, adjective2]
    return adjectivePair
#Generates a pair of adjectives in the specified tier.
def generatePlaceTier(tier):
    places = "Atlas\\" + tier + ".txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = placeArray[randomNum]
    return place
#Generates a place in the specified list.
def generatePlaceTierCleaning(tier):
    places = "Atlas\\" + tier + ".txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = [placeArray[randomNum], randomNum]
    return place
#Generates a place in the specified list tied with the random number.
def generateTime():
    timeFile = open("Competition Exclusive Info\\times.txt", "r")
    timeFull = timeFile.read()
    times = timeFull.split("\n")
    timeRNG = random.randint(0, len(times)-1)
    time = times[timeRNG]
    return time
#Generate a time from the time files
def generateJeopardyCategory():
    categoryFile = open("Contests\\Jeopardy\\categories.txt", "r")
    categoryFull = categoryFile.read()
    categories = categoryFull.split("\n")
    categoryRNG = random.randint(0, len(categories)-1)
    category = categories[categoryRNG]
    return category
#Generate a category from the Jeopardy Contest
def generateBachelor(genderMale):
    bach = ""
    if genderMale == True:
        bachFile = open("Contests\\Lasting Longer in the Bachelor\\bachelors.txt", "r")
        bachFull = bachFile.read()
        baches = bachFull.split("\n")
        bachNG = random.randint(0, len(baches)-1)
        bach = baches[bachNG]
    else:
        bachFile = open("Contests\\Lasting Longer in the Bachelorette\\bachelorettes.txt", "r")
        bachFull = bachFile.read()
        baches = bachFull.split("\n")
        bachNG = random.randint(0, len(baches)-1)
        bach = baches[bachNG]
    return bach
#Used for generating the bachelor/bachelorette for all 4 contest versions
def generateLifeSpeedrunConditions():
    speedRuns = []
    conditionNum = 3
    speedRunFile = open("Contests\\Life Speedrun\\conditions.txt", "r")
    speedRunFull = speedRunFile.read()
    speedRunConditions = speedRunFull.split("\n")
    randomNumList = []
    foo = False
    while foo != True:
        RNG = random.randint(0, len(speedRunConditions)-1)
        if not(RNG in randomNumList):
            randomNumList.append(RNG)
        if len(randomNumList) >= 3:
            foo = True
    for x in range(len(randomNumList)):
        speedRuns.append(speedRunConditions[randomNumList[x]])
    return speedRuns