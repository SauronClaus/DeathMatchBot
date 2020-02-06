import discord
from discord.utils import get

import random
import wikipedia
import os.path
def newGenerateNum(fileNumber, peopleList):
    rando = random.randint(0, fileNumber)
    if rando in peopleList:
        print("Generation Failed: " + str(rando) + " already in list")
        for i in peopleList:
           print("List: " + str(i))
        return peopleList
    else:
        #print (str(rando) + " added to list!")
        peopleList.append(rando)
        return peopleList
#Generate the number and makes sure that the person isn't in the list already.
def generateNumRep(fileNumber, listOfNumbers):
    rando = random.randint(0, fileNumber)
    listOfNumbers.append(rando)
    return listOfNumbers
#Generates a number but its okay if its repeating something already in the list.