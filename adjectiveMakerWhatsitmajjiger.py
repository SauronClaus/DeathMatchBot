import discord
from discord.utils import get

import random
import wikipedia
import os.path

from generateNumbers import generateNumRep
from generateNumbers import newGenerateNum

from embeds import createPlaceEmbed
from embeds import createWeaponEmbed
from embeds import summaryShort
from embeds import checkLinks

from generation import generatePerson
from generation import generateWeapon
from generation import generatePlace
from generation import generatePlaceAdverb
from generation import generateAdjective
from generation import generateWeaponPair
from generation import generateAdjectivePair

intents = discord.Intents.all()
client = discord.Client(intents=intents)

tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])


def setUp():
    channel = client.get_channel(773980861594730518)
    print("Found #" + str(channel.id))
    messageFile = open("Adjectives\\messages.txt", "a")
    messages = []
    #async for message in channel.history(limit=100000000):
        #messages.append(message)
        #try: 
            #messageFile.write("\n" + str(message.content))
        #except: 
            #print("error!")
#Set up. Commented code throws an error right now- I just copy and pasted it when I used it and moved it under on_ready(). If you want to use it, just throw it back under I guess.

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    messageFile = open("Adjectives\\messages copy.txt", "r")
    messageFull = messageFile.read()
    messageFile.close()
    messages = messageFull.split("\n")
    messagesCounted = 1
    
    for message in messages: 
        tier = input("Message #" + str(messagesCounted) + ": " + message)
        tierFile = open("Adjectives\\Tier" + tier + ".txt", "a")
        tierFile.write("\n" + message)
        tierFile.close()

        
    
    
client.run(botToken)

