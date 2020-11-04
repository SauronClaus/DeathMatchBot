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
    weaponTierFile = open("weaponTiers.txt", "r")
    weaponTierFull = weaponTierFile.read()
    weaponTierArray = weaponTierFull.split('\n')
    weaponTier1Num = random.randint(0, len(weaponTierArray)-1)
    weaponTier1Name = weaponTierArray[weaponTier1Num] + ".txt"
    weaponFile1 = open(weaponTier1Name, "r")
    weaponSet1 = weaponFile1.read().split('\n')
    randomNum = random.randint(0, len(weaponSet1)-1)
    weapon = weaponSet1[randomNum]
    return weapon
#Returns a random weapon
def generatePlace():
    places = "places.txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = placeArray[randomNum]
    return place
#Returns a random place
def generatePlaceAdverb():
    places = "placesName.txt"
    placesFile = open(places, "r")
    placeArray = placesFile.read().split('\n')
    randomNum = random.randint(0, len(placeArray)-1)
    place = placeArray[randomNum]
    return place
#Returns a random place without the proposition thing ("in", "on", etc.)