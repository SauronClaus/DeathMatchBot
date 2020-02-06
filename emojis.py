import discord
from discord.utils import get

import random
import wikipedia
import os.path
client = discord.Client()

def checkForEmoji(ID):
    print("ID: " + str(ID))
    for i in client.guilds:
            if i.name in discordEmojiList:
                #print(i.name)
                for emoji in i.emojis:
                    #print ("Emoji: " + emoji.name + "/" + str(emoji.id))
                    if str(emoji.id) == ID:
                        return emoji
    print("Failure")
#Returns an emoji object with the passed in ID. 
def findEmojiID(personName):
    peerFile = open("peer.txt", "r")
    peerFull = peerFile.read()
    peer = peerFull.split("\n")
    peoplePeerIndex = []
    personIndex = peer.index(personName)
    emojiID = peer[personIndex + 1]
    return emojiID
#Return the emoji ID from the person's name
def getEmoji(personName):
    emojiID = findEmojiID(personName)
    print(personName + "(" + str(emojiID) + ")")
    emoji = checkForEmoji(emojiID)
    return emoji
#Combines checkForEmoji() and findEmojiID()