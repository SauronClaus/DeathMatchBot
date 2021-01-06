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