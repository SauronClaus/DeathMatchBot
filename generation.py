import discord
from discord.utils import get

import random
from emojis import getEmoji

def generatePerson():
    peerFile = open("peer.txt", "r")
    peerArray = peerFile.read().split("\n")
    personFile = open("people.txt", "r")
    personArray = personFile.read().split("\n")
    fileNum = len(personArray)
    randomNum = random.randint(1, fileNum)
    person = personArray[randomNum]
    indexOfID = peerArray.index(person) + 1
    personInfo = [person, getEmoji(person), peerArray[indexOfID]]
    return personInfo
#Returns a list with the person, emoji object, and the person's emoji id. 
def generateWeapon():
    weaponTierFile = open("weaponTiers.txt", "r")
    weaponTierFull = weaponTierFile.read()
    weaponTierArray = weaponTierFull.split('\n')
    weaponTier1Num = random.randint(1, len(weaponTierArray) - 1)
    weaponTier1Name = weaponTierArray[weaponTier1Num] + ".txt"
    weaponFile1 = open(weaponTier1Name, "r")
    weaponSet1 = weaponFile1.read().split('\n')
    randomNum = random.randint(1, len(weaponSet1))
    weapon = weaponSet1[randomNum]
    return weapon
#Returns a random weapon
def generatePlace():
    places = "placesName.txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(1, len(placeArray))
    place = placeArray[randomNum]
    return place
#Returns a random place