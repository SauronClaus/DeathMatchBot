import discord
from discord.utils import get

import random
import wikipedia
import os.path
import xlwt
import plotly.express

from generateNumbers import generateNumRep
from generateNumbers import newGenerateNum

from embeds import createPlaceEmbed
from embeds import createWeaponEmbed
from embeds import createPlaceLongEmbed
from embeds import createAdjectiveEmbed
from embeds import summaryShort
from embeds import summaryShortest
from embeds import checkLinks
from embeds import createSongEmbed
from embeds import createMarioMinigameEmbed
from embeds import createSpaceShipEmbed
from embeds import createJudgeEmbedCooking
from embeds import createJudgeEmbedCleaning
from embeds import createFoodEmbed
from embeds import createPieEmbed
from embeds import createDrinkEmbed
from embeds import createContestEmbed
from embeds import createHDMClassicEmbed
from embeds import createFranchiseEmbed

from generation import generatePerson
from generation import generateWeapon
from generation import generatePlace
from generation import generatePlaceAdverb
from generation import generateAdjective
from generation import generateWeaponPair
from generation import generateAdjectivePair

from contestGeneration import generateContest
from contestGeneration import generateMatchMessage

#from tradingCards import createCard
#from tradingCards import grantCard
#from tradingCards import generateStats

#from tradingCardPerson import TradingCard
import time
import urllib.request

from PIL import Image
import requests
import json

pityChart = {}
pityCount = {}
pityNum = 75
currentStats = {}

presidentalNamesFile = open("Pictures\\Lincoln\\presidentLastNames.txt", "r", encoding='utf-8-sig')
presidentalNamesFull = presidentalNamesFile.read()
presidentalNames = presidentalNamesFull.split("\n")

numberOfLincolnPics = 0
roundNumber = int(open("matchNum.txt", "r", encoding='utf-8-sig').read().split("\n")[2])

intents = discord.Intents.all()
client = discord.Client(intents=intents)

discordEmojiList = ["test server", "1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer", "8EmojiServer", "9EmojiServer", "10DiscordEmojis", "11DiscordEmojis", "12DiscordEmojis", "13DiscordEmojis", "CA Teacher Emojis", "2CA Teacher Emojis"]
#List of servers with the Discord Emojis. 

tokenFile = open("token.txt", "r", encoding='utf-8-sig')
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[0]
testToken = tokens[1]
userID = int(tokens[2])

def findPersonPic(person):
    if os.path.exists("Pictures\\" + person.strip() + ".png"):
        return discord.File("Pictures\\" + person + '.png')
    else:
        if os.path.exists("Pictures\\" + person.strip() + ".jpg"):
            return discord.File("Pictures\\" + person + '.jpg')
#Finds the picture of a person
def findPeerIndex(personName):
    peerFile = open("peer.txt", "r", encoding='utf-8-sig')
    peerFull = peerFile.read()
    peer = peerFull.split("\n")
    peoplePeerIndex = []
    personIndex = peer.index(personName)
    return personIndex
#Gets the peer file's index of the person's name

def checkForEmoji(ID):
    print("ID: " + str(ID))
    for i in client.guilds:
        if i.name in discordEmojiList:
            for emoji in i.emojis:
                if str(emoji.id) == ID:
                    return emoji
    print("Failure: Emoji Object Not Found")
#Returns an emoji object with the passed in ID. 
def findEmojiID(personName, teacherBracket=False):
    if teacherBracket == False:
        peerFile = open("peer.txt", "r", encoding='utf-8-sig')
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        peoplePeerIndex = []
        if personName == "Abraham Lincoln": 
            personName = "ï»¿Abraham Lincoln"
        print("Person Name: " + personName)
        if personName != "WildWildWestWoodrowWilson" and personName != "Wild Wild West Woodrow Wilson":
            personIndex = peer.index(personName)
            emojiID = peer[personIndex + 1]
        else:
            emojiID = "1170032763420819517"
    if teacherBracket == True:
        peerFile = open("Faculty Death Match2.txt", "r", encoding='utf-8-sig')
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        for line in peer:
            if line.split("|")[0] == personName:
                print("Person Name: " + personName)
                emojiID = line.split("|")[1].strip()
    return emojiID
#Return the emoji ID from the person's name
def reverseEmojiID(ID):
    peerFile = open("peer.txt", "r", encoding='utf-8-sig')
    peerFull = peerFile.read()
    peer = peerFull.split("\n")
    peoplePeerIndex = []
    personIndex = peer.index(str(ID))
    personName = peer[personIndex - 1]
    return personName
#Returns the person name from the emoji ID
def findEmojiServer(ID):
    print("ID: " + str(ID))
    for i in client.guilds:
        if i.name in discordEmojiList:
            for emoji in i.emojis:
                if str(emoji.id) == ID:
                    smallListCombo = [i.name, emoji.name]
                    return smallListCombo
    print("Failure: Emoji Object Not Found")
#Finds the emoji server from the id
def getEmoji(personName, teacherBracket=False):
    emojiID = findEmojiID(personName, teacherBracket)
    print(personName + " (" + str(emojiID) + ")")
    emoji = checkForEmoji(emojiID)
    return emoji
#Combines checkForEmoji() and findEmojiID()
def createPersonEmbed(person, teacherBracket=False):
    personEmoji = getEmoji(person, teacherBracket)
    title = person
    if teacherBracket == False:
        person = checkLinks(person)
        article = wikipedia.page(person, auto_suggest=False)
        summary = article.summary.split('\n')
        summaryPersonal = summaryShort(str(summary[0]))
        embed = discord.Embed(title=title, description=summaryPersonal, color=0xFF9900)
    if teacherBracket == True:
        peerFile = open("Faculty Death Match2.txt", "r", encoding='utf-8-sig')
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        for line in peer:
            if line.split("|")[0] == person:
                description = line.split("|")[2].strip()
        peerFile.close()
        embed = discord.Embed(title=title, description=description, color=0xFF9900)
    print("Emoji Name: " + personEmoji.name)
    #print(summary[0])
    personURL = str(personEmoji.url)
    embed.set_image(url=personURL)
    if teacherBracket == False:
        embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object created from the inputed person.

def createMHAembed(person, teacherBracket=False):
    personFile = open("MHA Characters\\" + person + ".txt", "r", encoding='utf-8-sig')
    personArray = personFile.read().split("\n")
    personFile.close()
    title = personArray[0]

    summary = personArray[2]
    summaryPersonal = summaryShort(summary)
    embed = discord.Embed(title=title, description=summaryPersonal, color=0xFF9900)
   
    personURL = str(personArray[1])
    embed.set_image(url=personURL)
    
    embed.add_field(name="Link",value=personArray[3])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object created from the inputed person.
def returnResult(matchMessage):
    channel = client.get_channel(773719674927972424)
    messageResults = []
    embeds = matchMessage.embeds
    for embed in embeds:
        if "Round #" + str(roundNumber) in embed.title:
            num = 0
            reactions = {}
            for reaction in matchMessage.reactions:
                reactions[reaction.emoji.id] = reaction.count
            for reaction in reactions: 
                personName = reverseEmojiID(reaction)
            if reactions[matchMessage.reactions[0].emoji.id] > reactions[matchMessage.reactions[1].emoji.id]:
                winnerName = reverseEmojiID(matchMessage.reactions[0].emoji.id)
            else: 
                if reactions[matchMessage.reactions[1].emoji.id] > reactions[matchMessage.reactions[0].emoji.id]:
                    winnerName = reverseEmojiID(matchMessage.reactions[1].emoji.id)
                else:
                    winnerName = "Tie!"
            print("%s|%s|%s-%s|%s" % (reverseEmojiID(matchMessage.reactions[0].emoji.id), reverseEmojiID(matchMessage.reactions[1].emoji.id), reactions[matchMessage.reactions[0].emoji.id], reactions[matchMessage.reactions[1].emoji.id], winnerName)) 
        
    return "%s|%s|%s-%s|%s" % (reverseEmojiID(matchMessage.reactions[0].emoji.id), reverseEmojiID(matchMessage.reactions[1].emoji.id), reactions[matchMessage.reactions[0].emoji.id], reactions[matchMessage.reactions[1].emoji.id], winnerName)

def get_wiki_main_image(title):
    url = 'https://en.wikipedia.org/w/api.php'
    data = {
        'action' :'query',
        'format' : 'json',
        'formatversion' : 2,
        'prop' : 'pageimages|pageterms',
        'piprop' : 'original',
        'titles' : title
    }
    response = requests.get(url, data)
    json_data = json.loads(response.text)
    return json_data['query']['pages'][0]['original']['source'] if len(json_data['query']['pages']) >0 else 'Not found'

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    numberOfLincolnPics = 0
    print("Round Number: " + str(roundNumber))
    pityFile = open("declaredGacha.txt", "r", encoding='utf-8-sig')
    pityArray = pityFile.read().strip().split("\n")
    for line in pityArray:
        contents = line.split("|")
        pityChart[int(contents[0])] = contents[1]
    pityFile.close()
    pityCountFile = open("pityCount.txt", "r", encoding='utf-8-sig')
    pityArray = pityCountFile.read().strip().split("\n")
    for line in pityArray:
        contents = line.split("|")
        pityCount[int(contents[0])] = int(contents[1])
    
    for filename in os.listdir(os.getcwd() + "\\Gacha Storage Characters\\"):
        with open(os.path.join(os.getcwd() + "\\Gacha Storage Characters\\", filename), 'r') as f:
            
            storageFile = open("Gacha Storage Characters\\" + filename, "r", encoding='utf-8-sig')
            fileArray = storageFile.read().strip().split("\n")
            for i in fileArray:
                print("Initalizing " + str(i))
                personInfo = i.split("|")
                try:
                    currentStats[int(filename[0:len(filename)-4])][personInfo[0]] = int(personInfo[1])
                except:
                    currentStats[int(filename[0:len(filename)-4])] = {personInfo[0]: int(personInfo[1])}
    

    



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == userID: 
        if message.content.startswith("*ranked"):
            validRankedServers = {889564564365127751: [], 523962430179770369: []}
            #validRankedServers = {620964009247768586: [], 558662351906275328: []}
            #Other server: 
            #Second one is the testing servers

            roundNumber = int(open("matchNum.txt", "r", encoding='utf-8-sig').read().split("\n")[2])
            channel = message.channel
            quantMessages = 0
            numberOfMatches = 5
            messageResults = []
            async for matchMessage in channel.history(limit=numberOfMatches+5):
                if quantMessages < 5:
                    for embeds in matchMessage.embeds:
                        if "Round #" + str(roundNumber) in matchMessage.embeds[0].title:
                                #messageResults.append(returnResult(matchMessage))
                                quantMessages+=1

            #bracketFile = open("LogCADiscordRound" + str(roundNumber) + ".txt", "a")
            #bracketFile.write("\n")
            #messageResults.reverse()
            #for result in messageResults:
                #bracketFile.write(result)
                #bracketFile.write("\n")
            #bracketFile.close()
            #print("Completed!")
            
            guildID = message.guild.id
            numberOfMatchesFile = open("matchNum.txt", "r", encoding='utf-8-sig')
            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleFile = open("CABracket.txt", "r", encoding='utf-8-sig')

            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            peopleFile.close()
            peopleList = []
            fileNumber = len(peopleArray) - 1

            while (len(peopleList) < 2*numberOfMatches):
                peopleList = newGenerateNum(fileNumber, peopleList)
            
            people = []
            for personIndex in peopleList:
                people.append(peopleArray[personIndex])

            print("People: ")
            for person in people:
                print(person)
            
            weapons = []
            adjectives = []
            places = []
            contests = []
            specialEmbeds = []
            specialItems = []

            matchesInfo = {}
            for serverID in validRankedServers:
                matchesInfo[serverID] = []
            
            ticker = 0
            for matchNum in range(numberOfMatches):
                matchInfo = []
                condenser = {
                    people[ticker]: "",
                    people[ticker+1]: ""
                }
                matchInfo.append(condenser)
                ticker+=2
                for serverID in validRankedServers:
                    matchesInfo[serverID].append(matchInfo)
                    print("Added people to the dict!")
            #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
            for matchNumber in range(numberOfMatches):
                matcherInfo = generateContest()
                #Returned (in order) adjectivePair, weaponPair, place, specialItems, contestInformation
                adjectiveDict = {}
                weaponDict = {}
                placeDict = {}
                variant = ""
                contestDict = {}
                if matcherInfo != None:
                    for adjective in matcherInfo[0]:
                        adjectives.append(adjective)
                        adjectiveDict[adjective] = ""
                matchesInfo[serverID][matchNumber].append(adjectiveDict)
                print("Added adjectives to the final dict!")
                if matcherInfo != None:
                    for weapon in matcherInfo[1]:
                        weapons.append(weapon)
                        weaponDict[weapon] = ""
                matchesInfo[serverID][matchNumber].append(weaponDict)
                print("Added weapons to the final dict of match#" + str(matchNumber) + ": " + str(serverID))
                if matcherInfo != None and matcherInfo != "" and matcherInfo != " ":
                    places.append(matcherInfo[2])
                    placeDict[matcherInfo[2]] = ""
                matchesInfo[serverID][matchNumber].append(placeDict)
                if matcherInfo != None:
                    for specialItem in matcherInfo[3]:
                        specialEmbeds.append(specialItem[1])
                        specialItems.append(specialItem)
                matchesInfo[serverID][matchNumber].append(matcherInfo[3])
                if matcherInfo != None:      
                    contests.append(matcherInfo[4])
                    contestDict[matcherInfo[4][0]] = ""
                    variant = matcherInfo[4][1]
                matchesInfo[serverID][matchNumber].append(contestDict)
                matchesInfo[serverID][matchNumber].append(variant)

            print(str(matchesInfo))

            for serverID in validRankedServers:
                server = client.get_guild(serverID)

                pollChannel = message.channel
                peopleInfo = message.channel
                placeInfo = message.channel
                weaponsInfo = message.channel
                adjectivesInfo = message.channel
                contestInfo = message.channel
                contestItemsInfo = message.channel

                for channel in server.text_channels:
                    if channel.name == "historical-death-match-polls":
                        print("found #" + channel.name)
                        pollChannel = channel
                    if channel.name == "historical-people-info":
                        print("found #" + channel.name)
                        peopleInfo = channel
                    if channel.name == "historical-weapons-info":
                        print("found #" + channel.name)
                        weaponsInfo = channel
                    if channel.name == "historical-places-info":
                        print("found #" + channel.name)
                        placeInfo = channel
                    if channel.name == "historical-adjectives-info":
                        print("found #" + channel.name)
                        adjectivesInfo = channel
                    if channel.name == "historical-contests-info":
                        print("found #" + channel.name)
                        contestInfo = channel
                    if channel.name == "historical-contest-specific-info":
                        print("found #" + channel.name)
                        contestItemsInfo = channel
                
                validRankedServers[serverID].append(pollChannel)
                validRankedServers[serverID].append(peopleInfo)
                validRankedServers[serverID].append(weaponsInfo)
                validRankedServers[serverID].append(placeInfo)
                validRankedServers[serverID].append(adjectivesInfo)
                validRankedServers[serverID].append(contestInfo)
                validRankedServers[serverID].append(contestItemsInfo)

                
            
            print("Poll Channel: #" + pollChannel.name)

            lastInfo = open("lastInfo.txt", "w", encoding='utf-8-sig')
            stringsList = []
            for person in people:
                stringsList.append(person)
            for weapon in weapons:
                stringsList.append(weapon)
            for adjective in adjectives:
                stringsList.append(adjective)
            for place in places:
                stringsList.append(place)

            for i in stringsList:
                lastInfo.write(i + "\n")
            
            peopleInfoLinks = []
            weaponInfoLinks = []
            placeInfoLinks = []
            adjectiveInfoLinks = []
            specialItemInfoLinks = []
            contestInfoLinks = []


            matchMessages = []
            matchSet = 0

            specialItemsInfo = []
            for i in range(numberOfMatches):
                specialItemsInfo.append({})

            for serverID in validRankedServers:
                matchMessages.append([])

            for serverID in validRankedServers:
                linker = "https://discord.com/channels/" + str(serverID) + "/"
                ticker = 0
                for match in matchesInfo[serverID]:
                    print("~~Match: ~~ " + str(match))
                    pollChannel = validRankedServers[serverID][0]
                    for person in match[0]:
                        embed = createPersonEmbed(person)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        peopleInfo = validRankedServers[serverID][1]
                        print("Sent person to " + str(serverID) + "; channel " + str(validRankedServers[serverID][1]))
                        embedInfo = await peopleInfo.send(embed=embed)
                        peopleInfoLinks.append(embedInfo.id)
                        match[0][person] = str(embedInfo.id)     
                    for weapon in match[2]:
                        embed = createWeaponEmbed(weapon)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        
                        weaponsInfo = validRankedServers[serverID][2]
                        print("Sent weapon to " + str(serverID) + ".")
                        embedInfo = await weaponsInfo.send(embed=embed)
                        weaponInfoLinks.append(embedInfo.id)
                        match[2][weapon] = str(embedInfo.id)
                    for adjective in match[1]:
                        embed = createAdjectiveEmbed(adjective)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        adjectivesInfo = validRankedServers[serverID][4]
                        print("Sent adjective to " + str(serverID) + ".")
                        embedInfo = await adjectivesInfo.send(embed=embed)
                        adjectiveInfoLinks.append(embedInfo.id)
                        match[1][adjective] = str(embedInfo.id)
                    for place in match[3]:
                        print("Place (Checking for Null): ~" + place + "~")
                        if place != "":
                            embed = createPlaceLongEmbed(place)
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            placeInfo = validRankedServers[serverID][3]
                            print("Sent place to " + str(serverID) + "; channel " + str(validRankedServers[serverID][3]))
                            embedInfo = await placeInfo.send(embed=embed)
                            placeInfoLinks.append(embedInfo.id)
                            match[3][place] = str(embedInfo.id)
                    for specialItem in match[4]:
                        contest = ""
                        
                    for contest in match[5]:
                        embedsArray = []
                        #print("Server/" + pollChannel.guild.name + ": Special Item: " + str(match[4][specialItem]))
                        if contest == "Cleaning Competition":
                            file = open("Contests\\" + contest + "\\" + "judges.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")

                            judgeSet = fileArray[int(match[6][1])]
                            judges = judgeSet.split(", ")
                            for judge in judges:
                                embedsArray.append(createJudgeEmbedCleaning(judge, "Cleaning", judgeSet))
                                
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
                                embedsArray.append(createJudgeEmbedCooking(judge, "Cooking"))
                                print("Judge: " + judge)
                        if contest == "Drinking Contest":
                            file = open("Contests\\" + contest + "\\" + "drinks.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            drink = fileArray[randomNum]
                            embedsArray.append(createDrinkEmbed(drink))
                        if contest == "Get Sued by Nintendo":
                            file = open("Contests\\" + contest + "\\" + "franchise.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            franchise = fileArray[randomNum]
                            embedsArray.append(createFranchiseEmbed(franchise))
                        if contest == "Karaoke Contest":
                            file = open("Contests\\" + contest + "\\" + "songs.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            song = fileArray[randomNum]
                            embedsArray.append(createSongEmbed(song))
                        if contest == "Mario Party 10":
                            file = open("Contests\\" + contest + "\\" + "minigames.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            minigame = fileArray[randomNum]
                            embedsArray.append(createMarioMinigameEmbed(minigame))
                        if contest == "Pie Eating Contest":
                            file = open("Contests\\" + contest + "\\" + "pies.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            pie = fileArray[randomNum]
                            embedsArray.append(createPieEmbed(pie))
                        if contest == "First to Blow Up the Death Star I":
                            embedsArray.append(createSpaceShipEmbed("X-wing"))
                        for embed in embedsArray:        
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            embedInfo = await contestItemsInfo.send(embed=embed)
                            print(str(specialItemsInfo) + "/" + str(ticker) + "/" + str(embed.title))
                            specialItemsInfo[ticker][embed.title] = str(embedInfo.id)
                            print("EmbedInfo.id: " + str(embedInfo.id))

                        contestItemsInfo = validRankedServers[serverID][5]
                        specialItemInfoLinks.append(embedInfo.id)
                        #match[4][specialItem] = str(embedInfo.id)

                        if contest != "Death Match Classic":
                            embed = createContestEmbed(contest, match[6])
                        else:
                            embed = createHDMClassicEmbed()
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        contestInfo = validRankedServers[serverID][6]
                        embedInfo = await contestInfo.send(embed=embed)
                        contestInfoLinks.append(embedInfo.id)
                        match[5][contest] = str(embedInfo.id)
                        print("SpecialItemsInfoTest: " + str(specialItemsInfo))
                    ticker+=1

                print("SpecialItemsInfo: " + str(specialItemsInfo))
                #Fix the special info (specifically for White Wine)
                peopleLinks = []
                weaponLinks = []
                adjectiveLinks = []
                placeLinks = []
                itemLinks = []
                contestLinks = []
                #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
                ticker = 0
                for match in matchesInfo[serverID]:
                    smallTicker = 0
                    for person in match[0]:
                        match[0][person] = linker + str(peopleInfo.id) + "/" + match[0][person]
                    for adjective in match[1]:
                        match[1][adjective] = linker + str(adjectivesInfo.id) + "/" + match[1][adjective]
                    for weapon in match[2]:
                        match[2][weapon] = linker + str(weaponsInfo.id) + "/" + match[2][weapon]
                    for place in match[3]:
                        if place != "":
                            match[3][place] = linker + str(placeInfo.id) + "/" + match[3][place]
                    for specialItem in specialItemsInfo[ticker]:
                        print(str(smallTicker) + ": Check Special Items Info: " + str(specialItem) + ": " + str(specialItemsInfo[ticker]))
                        print("\tLinker: " + str(linker))
                        specialItemsInfo[ticker][specialItem] = linker + str(contestItemsInfo.id) + "/" + specialItemsInfo[ticker][specialItem]
                        smallTicker+=1
                    for contest in match[5]:
                        match[5][contest] = linker + str(contestInfo.id) + "/" + match[5][contest]
                    ticker+=1

                
                matchNum = 0
                for match in matchesInfo[serverID]:
                    match[4] = specialItemsInfo[matchNum]
                    print("match[4]: " + str(specialItemsInfo[matchNum]))
                    matchMessage = generateMatchMessage(match, True)
                    embed = discord.Embed(title="Round #" + str(numberOfRounds) + " Match #" + str(numberOfMatchesRound + matchNum) + " (Total Match #" + str(numberOfMatchesTotal + matchNum) + ")", description=matchMessage, color=0xFF9900)
                    pollChannel = validRankedServers[serverID][0]
                    matchMessage = await pollChannel.send(embed=embed)
                    matchMessages[matchSet].append(matchMessage)
                    matchNum+=1

                matchSet+=1
            numberOfMatchesFile.close()
            numberOfMatchesFile = open("matchNum.txt", "w", encoding='utf-8-sig')
            numberOfMatchesFile.write(str(numberOfMatchesTotal + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfMatchesRound + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfRounds))
            numberOfMatchesFile.close()
            
            for serverID in validRankedServers:
                server = client.get_guild(serverID)
                for role in server.roles:
                    if role.name == "Historical Death Match Notifee":
                        pollChannel = validRankedServers[serverID][0]
                        await pollChannel.send("<@&" + str(role.id) + ">")
            
            personIDList = []
            for i in people:
                personID = findEmojiID(i)
                personIDList.append(personID)       

            personEmojiList = []
            for personID in personIDList:
                personEmoji = checkForEmoji(personID)
                personEmojiList.append(personEmoji)

            for person in people:
                peopleArray.remove(person)

            peopleFile.close()
            peopleFile = open("CABracket.txt", "w", encoding='utf-8-sig')
            peerString = ""
            for name in peopleArray:
                peerString = peerString + "\n" + name
            stringPeer = peerString[1:len(peerString)]
            peopleFile.write(stringPeer)
            peopleFile.close()
            
            emojiTicker = 0
            matchNumber = 0
            for match in matchMessages[0]:
                for matchSet in matchMessages:
                    await matchSet[matchNumber].add_reaction(personEmojiList[emojiTicker])
                    await matchSet[matchNumber].add_reaction(personEmojiList[emojiTicker + 1])
                matchNumber+=1
                emojiTicker+=2
            print("Completed!")
        #Ranked matches for the CA Discord.             
        if message.content.startswith("*dailies"):
            validRankedServers = {1173402242989166702: []}
            #validRankedServers = {620964009247768586: []}
            #Other server: 
            #Second one is the testing servers

            roundNumber = int(open("matchNumOASI.txt", "r", encoding='utf-8-sig').read().split("\n")[2])
            channel = message.channel
            quantMessages = 0
            numberOfMatches = 5
            messageResults = []
            async for matchMessage in channel.history(limit=numberOfMatches+5):
                if quantMessages < 5:
                    for embeds in matchMessage.embeds:
                        if "Round #" + str(roundNumber) in matchMessage.embeds[0].title:
                                #messageResults.append(returnResult(matchMessage))
                                quantMessages+=1

          
            
            guildID = message.guild.id
            numberOfMatchesFile = open("matchNumOASI.txt", "r", encoding='utf-8-sig')
            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleFile = open("OASIBracket.txt", "r", encoding='utf-8-sig')

            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            peopleFile.close()
            peopleList = []
            fileNumber = len(peopleArray) - 1

            while (len(peopleList) < 2*numberOfMatches):
                peopleList = newGenerateNum(fileNumber, peopleList)
            
            people = []
            for personIndex in peopleList:
                people.append(peopleArray[personIndex])

            print("People: ")
            for person in people:
                print(person)
            
            weapons = []
            adjectives = []
            places = []
            contests = []
            specialEmbeds = []
            specialItems = []

            matchesInfo = {}
            for serverID in validRankedServers:
                matchesInfo[serverID] = []
            
            ticker = 0
            for matchNum in range(numberOfMatches):
                matchInfo = []
                condenser = {
                    people[ticker]: "",
                    people[ticker+1]: ""
                }
                matchInfo.append(condenser)
                ticker+=2
                for serverID in validRankedServers:
                    matchesInfo[serverID].append(matchInfo)
                    print("Added people to the dict!")
            #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
            for matchNumber in range(numberOfMatches):
                matcherInfo = generateContest()
                #Returned (in order) adjectivePair, weaponPair, place, specialItems, contestInformation
                adjectiveDict = {}
                weaponDict = {}
                placeDict = {}
                variant = ""
                contestDict = {}
                if matcherInfo != None:
                    for adjective in matcherInfo[0]:
                        adjectives.append(adjective)
                        adjectiveDict[adjective] = ""
                matchesInfo[serverID][matchNumber].append(adjectiveDict)
                print("Added adjectives to the final dict!")
                if matcherInfo != None:
                    for weapon in matcherInfo[1]:
                        weapons.append(weapon)
                        weaponDict[weapon] = ""
                matchesInfo[serverID][matchNumber].append(weaponDict)
                print("Added weapons to the final dict of match#" + str(matchNumber) + ": " + str(serverID))
                if matcherInfo != None and matcherInfo != "" and matcherInfo != " ":
                    places.append(matcherInfo[2])
                    placeDict[matcherInfo[2]] = ""
                matchesInfo[serverID][matchNumber].append(placeDict)
                if matcherInfo != None:
                    for specialItem in matcherInfo[3]:
                        specialEmbeds.append(specialItem[1])
                        specialItems.append(specialItem)
                matchesInfo[serverID][matchNumber].append(matcherInfo[3])
                if matcherInfo != None:      
                    contests.append(matcherInfo[4])
                    contestDict[matcherInfo[4][0]] = ""
                    variant = matcherInfo[4][1]
                matchesInfo[serverID][matchNumber].append(contestDict)
                matchesInfo[serverID][matchNumber].append(variant)

            print(str(matchesInfo))

            for serverID in validRankedServers:
                server = client.get_guild(serverID)

                pollChannel = message.channel
                peopleInfo = message.channel
                placeInfo = message.channel
                weaponsInfo = message.channel
                adjectivesInfo = message.channel
                contestInfo = message.channel
                contestItemsInfo = message.channel

                for channel in server.text_channels:
                    if channel.name == "historical-death-match-polls":
                        print("found #" + channel.name)
                        pollChannel = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        peopleInfo = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        weaponsInfo = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        placeInfo = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        adjectivesInfo = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        contestInfo = channel
                    if channel.name == "kiri-information":
                        print("found #" + channel.name)
                        contestItemsInfo = channel
                
                validRankedServers[serverID].append(pollChannel)
                validRankedServers[serverID].append(peopleInfo)
                validRankedServers[serverID].append(weaponsInfo)
                validRankedServers[serverID].append(placeInfo)
                validRankedServers[serverID].append(adjectivesInfo)
                validRankedServers[serverID].append(contestInfo)
                validRankedServers[serverID].append(contestItemsInfo)

                
            
            print("Poll Channel: #" + pollChannel.name)

            lastInfo = open("lastInfoOASI.txt", "w", encoding='utf-8-sig')
            stringsList = []
            for person in people:
                stringsList.append(person)
            for weapon in weapons:
                stringsList.append(weapon)
            for adjective in adjectives:
                stringsList.append(adjective)
            for place in places:
                stringsList.append(place)

            for i in stringsList:
                lastInfo.write(i + "\n")
            
            peopleInfoLinks = []
            weaponInfoLinks = []
            placeInfoLinks = []
            adjectiveInfoLinks = []
            specialItemInfoLinks = []
            contestInfoLinks = []


            matchMessages = []
            matchSet = 0

            specialItemsInfo = []
            for i in range(numberOfMatches):
                specialItemsInfo.append({})

            for serverID in validRankedServers:
                matchMessages.append([])

            for serverID in validRankedServers:
                linker = "https://discord.com/channels/" + str(serverID) + "/"
                ticker = 0
                for match in matchesInfo[serverID]:
                    print("~~Match: ~~ " + str(match))
                    pollChannel = validRankedServers[serverID][0]
                    for person in match[0]:
                        embed = createPersonEmbed(person)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        peopleInfo = validRankedServers[serverID][1]
                        print("Sent person to " + str(serverID) + "; channel " + str(validRankedServers[serverID][1]))
                        embedInfo = await peopleInfo.send(embed=embed)
                        peopleInfoLinks.append(embedInfo.id)
                        match[0][person] = str(embedInfo.id)     
                    for weapon in match[2]:
                        embed = createWeaponEmbed(weapon)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        
                        weaponsInfo = validRankedServers[serverID][2]
                        print("Sent weapon to " + str(serverID) + ".")
                        embedInfo = await weaponsInfo.send(embed=embed)
                        weaponInfoLinks.append(embedInfo.id)
                        match[2][weapon] = str(embedInfo.id)
                    for adjective in match[1]:
                        embed = createAdjectiveEmbed(adjective)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        adjectivesInfo = validRankedServers[serverID][4]
                        print("Sent adjective to " + str(serverID) + ".")
                        embedInfo = await adjectivesInfo.send(embed=embed)
                        adjectiveInfoLinks.append(embedInfo.id)
                        match[1][adjective] = str(embedInfo.id)
                    for place in match[3]:
                        print("Place (Checking for Null): ~" + place + "~")
                        if place != "":
                            embed = createPlaceLongEmbed(place)
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            placeInfo = validRankedServers[serverID][3]
                            print("Sent place to " + str(serverID) + "; channel " + str(validRankedServers[serverID][3]))
                            embedInfo = await placeInfo.send(embed=embed)
                            placeInfoLinks.append(embedInfo.id)
                            match[3][place] = str(embedInfo.id)
                    for specialItem in match[4]:
                        contest = ""
                        
                    for contest in match[5]:
                        embedsArray = []
                        #print("Server/" + pollChannel.guild.name + ": Special Item: " + str(match[4][specialItem]))
                        if contest == "Cleaning Competition":
                            file = open("Contests\\" + contest + "\\" + "judges.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")

                            judgeSet = fileArray[int(match[6][1])]
                            judges = judgeSet.split(", ")
                            for judge in judges:
                                embedsArray.append(createJudgeEmbedCleaning(judge, "Cleaning", judgeSet))
                                
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
                                embedsArray.append(createJudgeEmbedCooking(judge, "Cooking"))
                                print("Judge: " + judge)
                        if contest == "Drinking Contest":
                            file = open("Contests\\" + contest + "\\" + "drinks.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            drink = fileArray[randomNum]
                            embedsArray.append(createDrinkEmbed(drink))
                        if contest == "Get Sued by Nintendo":
                            file = open("Contests\\" + contest + "\\" + "franchise.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            franchise = fileArray[randomNum]
                            embedsArray.append(createFranchiseEmbed(franchise))
                        if contest == "Karaoke Contest":
                            file = open("Contests\\" + contest + "\\" + "songs.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            song = fileArray[randomNum]
                            embedsArray.append(createSongEmbed(song))
                        if contest == "Mario Party 10":
                            file = open("Contests\\" + contest + "\\" + "minigames.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            minigame = fileArray[randomNum]
                            embedsArray.append(createMarioMinigameEmbed(minigame))
                        if contest == "Pie Eating Contest":
                            file = open("Contests\\" + contest + "\\" + "pies.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            pie = fileArray[randomNum]
                            embedsArray.append(createPieEmbed(pie))
                        if contest == "First to Blow Up the Death Star I":
                            embedsArray.append(createSpaceShipEmbed("X-wing"))
                        for embed in embedsArray:        
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            embedInfo = await contestItemsInfo.send(embed=embed)
                            print(str(specialItemsInfo) + "/" + str(ticker) + "/" + str(embed.title))
                            specialItemsInfo[ticker][embed.title] = str(embedInfo.id)
                            print("EmbedInfo.id: " + str(embedInfo.id))

                        contestItemsInfo = validRankedServers[serverID][5]
                        specialItemInfoLinks.append(embedInfo.id)
                        #match[4][specialItem] = str(embedInfo.id)

                        if contest != "Death Match Classic":
                            embed = createContestEmbed(contest, match[6])
                        else:
                            embed = createHDMClassicEmbed()
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        contestInfo = validRankedServers[serverID][6]
                        embedInfo = await contestInfo.send(embed=embed)
                        contestInfoLinks.append(embedInfo.id)
                        match[5][contest] = str(embedInfo.id)
                        print("SpecialItemsInfoTest: " + str(specialItemsInfo))
                    ticker+=1

                print("SpecialItemsInfo: " + str(specialItemsInfo))
                #Fix the special info (specifically for White Wine)
                peopleLinks = []
                weaponLinks = []
                adjectiveLinks = []
                placeLinks = []
                itemLinks = []
                contestLinks = []
                #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
                ticker = 0
                for match in matchesInfo[serverID]:
                    smallTicker = 0
                    for person in match[0]:
                        match[0][person] = linker + str(peopleInfo.id) + "/" + match[0][person]
                    for adjective in match[1]:
                        match[1][adjective] = linker + str(adjectivesInfo.id) + "/" + match[1][adjective]
                    for weapon in match[2]:
                        match[2][weapon] = linker + str(weaponsInfo.id) + "/" + match[2][weapon]
                    for place in match[3]:
                        if place != "":
                            match[3][place] = linker + str(placeInfo.id) + "/" + match[3][place]
                    for specialItem in specialItemsInfo[ticker]:
                        print(str(smallTicker) + ": Check Special Items Info: " + str(specialItem) + ": " + str(specialItemsInfo[ticker]))
                        print("\tLinker: " + str(linker))
                        specialItemsInfo[ticker][specialItem] = linker + str(contestItemsInfo.id) + "/" + specialItemsInfo[ticker][specialItem]
                        smallTicker+=1
                    for contest in match[5]:
                        match[5][contest] = linker + str(contestInfo.id) + "/" + match[5][contest]
                    ticker+=1

                
                matchNum = 0
                for match in matchesInfo[serverID]:
                    match[4] = specialItemsInfo[matchNum]
                    print("match[4]: " + str(specialItemsInfo[matchNum]))
                    matchMessage = generateMatchMessage(match, True)
                    embed = discord.Embed(title="Round #" + str(numberOfRounds) + " Match #" + str(numberOfMatchesRound + matchNum) + " (Total Match #" + str(numberOfMatchesTotal + matchNum) + ")", description=matchMessage, color=0xFF9900)
                    pollChannel = validRankedServers[serverID][0]
                    matchMessage = await pollChannel.send(embed=embed)
                    matchMessages[matchSet].append(matchMessage)
                    matchNum+=1

                matchSet+=1
            numberOfMatchesFile.close()
            numberOfMatchesFile = open("matchNumOASI.txt", "w", encoding='utf-8-sig')
            numberOfMatchesFile.write(str(numberOfMatchesTotal + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfMatchesRound + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfRounds))
            numberOfMatchesFile.close()
                        
            personIDList = []
            for i in people:
                personID = findEmojiID(i)
                personIDList.append(personID)       

            personEmojiList = []
            for personID in personIDList:
                personEmoji = checkForEmoji(personID)
                personEmojiList.append(personEmoji)

            for person in people:
                peopleArray.remove(person)

            peopleFile.close()
            peopleFile = open("OASIBracket.txt", "w", encoding='utf-8-sig')
            peerString = ""
            for name in peopleArray:
                peerString = peerString + "\n" + name
            stringPeer = peerString[1:len(peerString)]
            peopleFile.write(stringPeer)
            peopleFile.close()
            
            emojiTicker = 0
            matchNumber = 0
            for match in matchMessages[0]:
                for matchSet in matchMessages:
                    await matchSet[matchNumber].add_reaction(personEmojiList[emojiTicker])
                    await matchSet[matchNumber].add_reaction(personEmojiList[emojiTicker + 1])
                matchNumber+=1
                emojiTicker+=2
            print("Completed!")
        if message.content.startswith("*mhaMatch"):
            validRankedServers = {1173402242989166702: []}
            #validRankedServers = {620964009247768586: []}
            #Other server: 
            #Second one is the testing servers

            roundNumber = int(open("mhaMatchNumOASI.txt", "r", encoding='utf-8-sig').read().split("\n")[2])
            channel = message.channel
            quantMessages = 0
            numberOfMatches = 5
            messageResults = []
            async for matchMessage in channel.history(limit=numberOfMatches+5):
                if quantMessages < 5:
                    for embeds in matchMessage.embeds:
                        if "Round #" + str(roundNumber) in matchMessage.embeds[0].title:
                                #messageResults.append(returnResult(matchMessage))
                                quantMessages+=1

          
            
            guildID = message.guild.id
            numberOfMatchesFile = open("mhaMatchNumOASI.txt", "r", encoding='utf-8-sig')

            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            

            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleFile = open("mhaBracket.txt", "r", encoding='utf-8-sig')

            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            peopleFile.close()
            peopleList = []
            fileNumber = len(peopleArray) - 1

            while (len(peopleList) < 2*numberOfMatches):
                peopleList = newGenerateNum(fileNumber, peopleList)
            
            people = []
            for personIndex in peopleList:
                people.append(peopleArray[personIndex])

            print("People: ")
            for person in people:
                print(person)
            
            weapons = []
            adjectives = []
            places = []
            contests = []
            specialEmbeds = []
            specialItems = []

            matchesInfo = {}
            for serverID in validRankedServers:
                matchesInfo[serverID] = []
            
            ticker = 0
            for matchNum in range(numberOfMatches):
                matchInfo = []
                condenser = {
                    people[ticker]: "",
                    people[ticker+1]: ""
                }
                matchInfo.append(condenser)
                ticker+=2
                for serverID in validRankedServers:
                    matchesInfo[serverID].append(matchInfo)
                    print("Added people to the dict!")
            #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
            for matchNumber in range(numberOfMatches):
                matcherInfo = generateContest()
                #Returned (in order) adjectivePair, weaponPair, place, specialItems, contestInformation
                adjectiveDict = {}
                weaponDict = {}
                placeDict = {}
                variant = ""
                contestDict = {}
                if matcherInfo != None:
                    for adjective in matcherInfo[0]:
                        adjectives.append(adjective)
                        adjectiveDict[adjective] = ""
                matchesInfo[serverID][matchNumber].append(adjectiveDict)
                print("Added adjectives to the final dict!")
                if matcherInfo != None:
                    for weapon in matcherInfo[1]:
                        weapons.append(weapon)
                        weaponDict[weapon] = ""
                matchesInfo[serverID][matchNumber].append(weaponDict)
                print("Added weapons to the final dict of match#" + str(matchNumber) + ": " + str(serverID))
                if matcherInfo != None and matcherInfo != "" and matcherInfo != " ":
                    places.append(matcherInfo[2])
                    placeDict[matcherInfo[2]] = ""
                matchesInfo[serverID][matchNumber].append(placeDict)
                if matcherInfo != None:
                    for specialItem in matcherInfo[3]:
                        specialEmbeds.append(specialItem[1])
                        specialItems.append(specialItem)
                matchesInfo[serverID][matchNumber].append(matcherInfo[3])
                if matcherInfo != None:      
                    contests.append(matcherInfo[4])
                    contestDict[matcherInfo[4][0]] = ""
                    variant = matcherInfo[4][1]
                matchesInfo[serverID][matchNumber].append(contestDict)
                matchesInfo[serverID][matchNumber].append(variant)

            print(str(matchesInfo))

            for serverID in validRankedServers:
                server = client.get_guild(serverID)

                pollChannel = message.channel
                peopleInfo = message.channel
                placeInfo = message.channel
                weaponsInfo = message.channel
                adjectivesInfo = message.channel
                contestInfo = message.channel
                contestItemsInfo = message.channel

                for channel in server.text_channels:
                    if channel.name == "mha-death-match":
                        print("found #" + channel.name)
                        pollChannel = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        peopleInfo = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        weaponsInfo = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        placeInfo = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        adjectivesInfo = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        contestInfo = channel
                    if channel.name == "mha-info":
                        print("found #" + channel.name)
                        contestItemsInfo = channel
                
                validRankedServers[serverID].append(pollChannel)
                validRankedServers[serverID].append(peopleInfo)
                validRankedServers[serverID].append(weaponsInfo)
                validRankedServers[serverID].append(placeInfo)
                validRankedServers[serverID].append(adjectivesInfo)
                validRankedServers[serverID].append(contestInfo)
                validRankedServers[serverID].append(contestItemsInfo)

                
            
            print("Poll Channel: #" + pollChannel.name)

            lastInfo = open("lastInfoMHA.txt", "w", encoding='utf-8-sig')
            stringsList = []
            for person in people:
                stringsList.append(person)
            for weapon in weapons:
                stringsList.append(weapon)
            for adjective in adjectives:
                stringsList.append(adjective)
            for place in places:
                stringsList.append(place)

            for i in stringsList:
                lastInfo.write(i + "\n")
            
            peopleInfoLinks = []
            weaponInfoLinks = []
            placeInfoLinks = []
            adjectiveInfoLinks = []
            specialItemInfoLinks = []
            contestInfoLinks = []


            matchMessages = []
            matchSet = 0

            specialItemsInfo = []
            for i in range(numberOfMatches):
                specialItemsInfo.append({})

            for serverID in validRankedServers:
                matchMessages.append([])

            for serverID in validRankedServers:
                linker = "https://discord.com/channels/" + str(serverID) + "/"
                ticker = 0
                for match in matchesInfo[serverID]:
                    print("~~Match: ~~ " + str(match))
                    pollChannel = validRankedServers[serverID][0]
                    for person in match[0]:
                        embed = createMHAembed(person)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        peopleInfo = validRankedServers[serverID][1]
                        print("Sent person to " + str(serverID) + "; channel " + str(validRankedServers[serverID][1]))
                        embedInfo = await peopleInfo.send(embed=embed)
                        peopleInfoLinks.append(embedInfo.id)
                        match[0][person] = str(embedInfo.id)     
                    for weapon in match[2]:
                        embed = createWeaponEmbed(weapon)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        
                        weaponsInfo = validRankedServers[serverID][2]
                        print("Sent weapon to " + str(serverID) + ".")
                        embedInfo = await weaponsInfo.send(embed=embed)
                        weaponInfoLinks.append(embedInfo.id)
                        match[2][weapon] = str(embedInfo.id)
                    for adjective in match[1]:
                        embed = createAdjectiveEmbed(adjective)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        adjectivesInfo = validRankedServers[serverID][4]
                        print("Sent adjective to " + str(serverID) + ".")
                        embedInfo = await adjectivesInfo.send(embed=embed)
                        adjectiveInfoLinks.append(embedInfo.id)
                        match[1][adjective] = str(embedInfo.id)
                    for place in match[3]:
                        print("Place (Checking for Null): ~" + place + "~")
                        if place != "":
                            embed = createPlaceLongEmbed(place)
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            placeInfo = validRankedServers[serverID][3]
                            print("Sent place to " + str(serverID) + "; channel " + str(validRankedServers[serverID][3]))
                            embedInfo = await placeInfo.send(embed=embed)
                            placeInfoLinks.append(embedInfo.id)
                            match[3][place] = str(embedInfo.id)
                    for specialItem in match[4]:
                        contest = ""
                        
                    for contest in match[5]:
                        embedsArray = []
                        #print("Server/" + pollChannel.guild.name + ": Special Item: " + str(match[4][specialItem]))
                        if contest == "Cleaning Competition":
                            file = open("Contests\\" + contest + "\\" + "judges.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")

                            judgeSet = fileArray[int(match[6][1])]
                            judges = judgeSet.split(", ")
                            for judge in judges:
                                embedsArray.append(createJudgeEmbedCleaning(judge, "Cleaning", judgeSet))
                                
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
                                embedsArray.append(createJudgeEmbedCooking(judge, "Cooking"))
                                print("Judge: " + judge)
                        if contest == "Drinking Contest":
                            file = open("Contests\\" + contest + "\\" + "drinks.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            drink = fileArray[randomNum]
                            embedsArray.append(createDrinkEmbed(drink))
                        if contest == "Get Sued by Nintendo":
                            file = open("Contests\\" + contest + "\\" + "franchise.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            franchise = fileArray[randomNum]
                            embedsArray.append(createFranchiseEmbed(franchise))
                        if contest == "Karaoke Contest":
                            file = open("Contests\\" + contest + "\\" + "songs.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            song = fileArray[randomNum]
                            embedsArray.append(createSongEmbed(song))
                        if contest == "Mario Party 10":
                            file = open("Contests\\" + contest + "\\" + "minigames.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            minigame = fileArray[randomNum]
                            embedsArray.append(createMarioMinigameEmbed(minigame))
                        if contest == "Pie Eating Contest":
                            file = open("Contests\\" + contest + "\\" + "pies.txt", "r")
                            fileFull = file.read()
                            fileArray = fileFull.split("\n")
                            randomNum = random.randint(0, len(fileArray)-1)
                            file.close()
                            pie = fileArray[randomNum]
                            embedsArray.append(createPieEmbed(pie))
                        if contest == "First to Blow Up the Death Star I":
                            embedsArray.append(createSpaceShipEmbed("X-wing"))
                        for embed in embedsArray:        
                            embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                            embedInfo = await contestItemsInfo.send(embed=embed)
                            print(str(specialItemsInfo) + "/" + str(ticker) + "/" + str(embed.title))
                            specialItemsInfo[ticker][embed.title] = str(embedInfo.id)
                            print("EmbedInfo.id: " + str(embedInfo.id))

                        contestItemsInfo = validRankedServers[serverID][5]
                        specialItemInfoLinks.append(embedInfo.id)
                        #match[4][specialItem] = str(embedInfo.id)

                        if contest != "Death Match Classic":
                            embed = createContestEmbed(contest, match[6])
                        else:
                            embed = createHDMClassicEmbed()
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        contestInfo = validRankedServers[serverID][6]
                        embedInfo = await contestInfo.send(embed=embed)
                        contestInfoLinks.append(embedInfo.id)
                        match[5][contest] = str(embedInfo.id)
                        print("SpecialItemsInfoTest: " + str(specialItemsInfo))
                    ticker+=1

                print("SpecialItemsInfo: " + str(specialItemsInfo))
                #Fix the special info (specifically for White Wine)
                peopleLinks = []
                weaponLinks = []
                adjectiveLinks = []
                placeLinks = []
                itemLinks = []
                contestLinks = []
                #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
                ticker = 0
                for match in matchesInfo[serverID]:
                    smallTicker = 0
                    for person in match[0]:
                        match[0][person] = linker + str(peopleInfo.id) + "/" + match[0][person]
                    for adjective in match[1]:
                        match[1][adjective] = linker + str(adjectivesInfo.id) + "/" + match[1][adjective]
                    for weapon in match[2]:
                        match[2][weapon] = linker + str(weaponsInfo.id) + "/" + match[2][weapon]
                    for place in match[3]:
                        if place != "":
                            match[3][place] = linker + str(placeInfo.id) + "/" + match[3][place]
                    for specialItem in specialItemsInfo[ticker]:
                        print(str(smallTicker) + ": Check Special Items Info: " + str(specialItem) + ": " + str(specialItemsInfo[ticker]))
                        print("\tLinker: " + str(linker))
                        specialItemsInfo[ticker][specialItem] = linker + str(contestItemsInfo.id) + "/" + specialItemsInfo[ticker][specialItem]
                        smallTicker+=1
                    for contest in match[5]:
                        match[5][contest] = linker + str(contestInfo.id) + "/" + match[5][contest]
                    ticker+=1

                
                matchNum = 0
                for match in matchesInfo[serverID]:
                    match[4] = specialItemsInfo[matchNum]
                    print("match[4]: " + str(specialItemsInfo[matchNum]))
                    matchMessage = generateMatchMessage(match, True, True)
                    embed = discord.Embed(title="Round #" + str(numberOfRounds) + " Match #" + str(numberOfMatchesRound + matchNum) + " (Total Match #" + str(numberOfMatchesTotal + matchNum) + ")", description=matchMessage, color=0xFF9900)
                    pollChannel = validRankedServers[serverID][0]
                    matchMessage = await pollChannel.send(embed=embed)
                    matchMessages[matchSet].append(matchMessage)
                    matchNum+=1

                matchSet+=1
            numberOfMatchesFile.close()
            numberOfMatchesFile = open("mhaMatchNumOASI.txt", "w", encoding='utf-8-sig')
            numberOfMatchesFile.write(str(numberOfMatchesTotal + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfMatchesRound + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfRounds))
            numberOfMatchesFile.close()
                        
           #personIDList = []
            #for i in people:
             #   personID = findEmojiID(i)
              #  personIDList.append(personID)       

            #personEmojiList = []
            #for personID in personIDList:
             #   personEmoji = checkForEmoji(personID)
              #  personEmojiList.append(personEmoji)

            for person in people:
                peopleArray.remove(person)

            peopleFile.close()
            peopleFile = open("mhaBracket.txt", "w", encoding='utf-8-sig')
            peerString = ""
            for name in peopleArray:
                peerString = peerString + "\n" + name
            stringPeer = peerString[1:len(peerString)]
            peopleFile.write(stringPeer)
            peopleFile.close()
            
            emojiTicker = 0
            matchNumber = 0
            for match in matchMessages[0]:
                for matchSet in matchMessages:
                    await matchSet[matchNumber].add_reaction("🅰️")
                    await matchSet[matchNumber].add_reaction("🅱️")
                matchNumber+=1
                emojiTicker+=2
            print("Completed!")
        
        if message.content.startswith("*sendLastMatchInfo"):
            infoWrite = open("lastInfo.txt", "r", encoding='utf-8-sig')
            infoFull = infoWrite.read()
            info = infoFull.split("\n")
            pollChannel = message.channel
            peopleInfo = message.channel
            weaponsInfo = message.channel
            adjectivesInfo = message.channel
            placesInfo = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "historical-death-match-polls":
                    print("found #" + channel.name)
                    pollChannel = channel
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    weaponsInfo = channel
                if channel.name == "historical-places-info":
                    print("found #" + channel.name)
                    placeInfo = channel
                if channel.name == "historical-adjectives-info":
                    print("found #" + channel.name)
                    adjectivesInfo = channel

            embed = createPersonEmbed(info[0])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[1])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[2])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[3])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[4])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[5])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[6])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[7])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[8])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createPersonEmbed(info[9])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await peopleInfo.send(embed=embed)
            embed = createWeaponEmbed(info[10])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[11])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[12])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[13])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[14])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[15])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[16])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[17])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[18])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createWeaponEmbed(info[19])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await weaponsInfo.send(embed=embed)
            embed = createPlaceLongEmbed(info[20])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await placeInfo.send(embed=embed)
            embed = createPlaceLongEmbed(info[21])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await placeInfo.send(embed=embed)
            embed = createPlaceLongEmbed(info[22])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await placeInfo.send(embed=embed)
            embed = createPlaceLongEmbed(info[23])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await placeInfo.send(embed=embed)
            embed = createPlaceLongEmbed(info[24])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await placeInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[25])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[26])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[27])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[28])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[29])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[30])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[31])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[32])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[33])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
            embed = createAdjectiveEmbed(info[34])
            embed.add_field(name="Return to Poll",value="[Here](https://discord.com/channels/523962430179770369/773719674927972424)", inline=False)
            await adjectivesInfo.send(embed=embed)
        #Send the info in the file "lastInfo.txt"
        if message.content.startswith("*SuleimanSpecial"):
            sentMessage = await message.channel.send("An equal number of Suleiman to the people in this tier list with scimitars vs everyone else in this tier list with longswords at the gates of Vienna!")
            embed = createPersonEmbed("Suleiman the Magnificent")
            peopleInfo = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
            await peopleInfo.send(embed=embed)
            crowdMoji = checkForEmoji(str(670378517585723443))
            SuleimanMoji = checkForEmoji(str(670368394180296744))
            await sentMessage.add_reaction(SuleimanMoji)
            await sentMessage.add_reaction(crowdMoji)
        #Suleiman Special!
        if message.content.startswith("*SuperBowlSpecial"):
            sentMessage = await message.channel.send("The Kansas City Chiefs with bows vs the San Francisco 49ers with MAT-49s in a pottery contest!")
            #embed = createWeaponEmbed("MAT-49")
            peopleInfo = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
            #await peopleInfo.send(embed=embed)
            crowdMoji = checkForEmoji(str(673616029485891612))
            SuleimanMoji = checkForEmoji(str(673616029850664991))
            await sentMessage.add_reaction(crowdMoji)
            await sentMessage.add_reaction(SuleimanMoji)
        #Super Bowl Special!
        if message.content.startswith("*resetBracket"):
            roundNumber = int(open("matchNum.txt", "r", encoding='utf-8-sig').read().split("\n")[2])
            logFile = open("LogCADiscordRound" + str(roundNumber) + ".txt", "r", encoding='utf-8-sig')
            logFull = logFile.read()
            log = logFull.split("\n")
            logFile.close()
            reepFull = ""
            for matchInfo in log:
                match = matchInfo.split("|")
                if match[3] == "Tie!":
                    reepFull = reepFull + "\n" + match[0] + "\n" + match[1]
                else:
                    scores = match[2].split("-")
                    if scores[0] > scores[1]:
                        winner = match[0]
                    if scores[1] > scores[0]:
                        winner = match[1]
                    if winner != match[3]:
                        print("--Error!--")
                    else:
                        reepFull = reepFull + "\n" + match[3]              
            reepFile = open("CABracket.txt", "w", encoding='utf-8-sig')
            reepFile.write(reepFull)
            reepFile.close()
            print("Completed!")
            matchNumFile = open("matchNum.txt", "r", encoding='utf-8-sig')
            matchNumFull = matchNumFile.read().split("\n")
            matchNumber = matchNumFull[0]
            roundInMatch = 1
            roundNumber+=1
            matchNumFile.close()
            matchNumFile = open("matchNum.txt", "w", encoding='utf-8-sig')
            matchNumFile.write(str(matchNumber) + "\n" + str(roundInMatch) + "\n" + str(roundNumber))
            matchNumFile.close()
        #Resets the bracket with the matches in "LogCADiscordRoundn.txt", where n is roundNumber        
        if message.content.startswith("*peoplePics"):
            peopleFile = open("people.txt", "r", encoding='utf-8-sig')
            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            for person in peopleArray:
                if os.path.exists("Pictures\\" + person.strip() + ".png"):
                    await message.channel.send(file=discord.File("Pictures\\" + person + '.png'))
                else:
                    if os.path.exists("Pictures\\" + person.strip() + ".jpg"):
                        await message.channel.send(file=discord.File("Pictures\\" + person + '.jpg'))
                    else:
                        await message.channel.send("<@366709133195476992> : " + person + " does not exist.")
        #Sends all the pictures of the people in the match. 
        if message.content.startswith("*resetRankedBrackets"):
            peopleFile = open("peer.txt", "r", encoding='utf-8-sig')
            peopleFull = peopleFile.read()
            people = peopleFull.split("\n")

            CABracketFile = open("CABracket.txt", "r", encoding='utf-8-sig')
            CABracketFull = CABracketFile.read()
            BackUp = open("CABracketBackUp.txt", "w", encoding='utf-8-sig')
            BackUp.write(CABracketFull)
            CABracketFile.close()
            BackUp.close()

            CABracket = []
            for i in range(len(people)):
                if i % 2 == 0 and (people[i] != "A" and people[i] != "B"):
                    CABracket.append(people[i])
                    print(str(people[i]) + " added.")
            CABracketFile = open("CABracket.txt", "w", encoding='utf-8-sig')
            for person in CABracket:
                CABracketFile.write("\n" + person)
            CABracketFile.close()
            peopleFile.close()
            await message.channel.send("Completed.")
        #Resets the bracket for the CA Discord. 
        if message.content.startswith("*everyInfoEver"):
            for channel in message.guild.text_channels:
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    weaponsInfo = channel
                if channel.name == "historical-places-info":
                    print("found #" + channel.name)
                    placeInfo = channel

            #peopleFile = open("peer.txt", "r", encoding='utf-8-sig')
            #peopleFull = peopleFile.read()
            #people = peopleFull.split("\n")
            #peopleFile.close()
            #for i in range(len(people)):
                #if i % 2 == 0 and (people[i] != "A" and people[i] != "B"):
                    #embed = createPersonEmbed(people[i])
                    #await peopleInfo.send(embed=embed)


            weaponTiersFiles = open("weaponTiers.txt", "r", encoding='utf-8-sig')
            adjectiveTiersFull = weaponTiersFiles.read()
            weaponTiers = adjectiveTiersFull.split("\n")
            weaponTiersFiles.close()
            for weaponTier in weaponTiers:
                weaponFile = open(weaponTier + ".txt", "r", encoding='utf-8-sig')
                weaponFull = weaponFile.read()
                weapons = weaponFull.split("\n")
                weaponFile.close()
                for weapon in weapons: 
                    embed = createWeaponEmbed(weapon)
                    await weaponsInfo.send(embed=embed)

            placesFile = open("places.txt", "r", encoding='utf-8-sig')
            placesFull = placesFile.read()
            places = placesFull.split("\n")
            for place in places:
                embed = createPlaceEmbed(place)
                await placeInfo.send(embed=embed)
        #sends all of the info for all people, weapons, and places. 
        if message.content.startswith("*checkEmoji"):
            for emoji in message.guild.emojis:
                await message.channel.send(emoji.name + "\n" + str(emoji.id))
            print("Completed!")
        #Sends all the emojis with ids in the server. Useful for large emoji batches. 
        if (message.content.startswith("*customMatch") or message.content.startswith("*presidentialBracket")):
            peopleMatch3 = ["George Washington", "John Adams"]

            peopleMatches = [peopleMatch3]

            numberOfMatches = len(peopleMatches)
            matchesVariables = []
            guildID = message.guild.id

            numofMatches = 0

            weaponTierFile = open("Armory\\Tiers\\weaponTiers.txt", "r", encoding='utf-8-sig')
            placesFile = open("Atlas\\places.txt", "r", encoding='utf-8-sig')
            adjectiveTierFile = open("Adjectives\\adjectiveTiers.txt")
            
            people = []

            for match in peopleMatches:
                for person in match:
                    people.append(person)

            print("People: ")
            for person in people:
                print(person)
            
            weapons = []

            for match in range(numberOfMatches):
                weaponSet = generateWeaponPair()
                weapons.append(weaponSet[0])
                weapons.append(weaponSet[1])

    
            print("Weapons: ")
            for weapon in weaponSet:
                print(weapon)

            places = []
            for match in range(numberOfMatches):
                places.append(generatePlace())

            print("Places: ")
            for place in places:
                print(place)

            adjectives = []

            for match in range(numberOfMatches):
                adjectiveSet = generateAdjectivePair()
                adjectives.append(adjectiveSet[0])
                adjectives.append(adjectiveSet[1])
            
            print("Adjectives: ")
            for adjective in adjectives:
                print(adjective)

            pollChannel = message.channel
            peopleInfo = message.channel
            placeInfo = message.channel
            weaponsInfo = message.channel
            adjectivesInfo = message.channel

            for channel in message.guild.text_channels:
                if channel.name == "historical-death-match-polls":
                    print("found #" + channel.name)
                    pollChannel = channel
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    weaponsInfo = channel
                if channel.name == "historical-places-info":
                    print("found #" + channel.name)
                    placeInfo = channel
                if channel.name == "historical-adjectives-info":
                    print("found #" + channel.name)
                    adjectivesInfo = channel
            
            print("Poll Channel: #" + pollChannel.name)

            #lastInfo = open("lastInfo.txt", "w", encoding='utf-8-sig')
            #stringsList = [people[0], people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], weapons[0], weapons[1], weapons[2], weapons[3], weapons[4], weapons[5], weapons[6], weapons[7], weapons[8], weapons[9], places[0], places[1], places[2], places[3], places[4], adjectives[0], adjectives[1], adjectives[2], adjectives[3], adjectives[4], adjectives[5], adjectives[6], adjectives[7], adjectives[8], adjectives[9]]
            #for i in stringsList:
            #    lastInfo.write(i + "\n")
            
            peopleInfoLinks = []
            weaponInfoLinks = []
            placeInfoLinks = []
            adjectiveInfoLinks = []

            for person in people:
                embed = createPersonEmbed(person)
                embedInfo = await peopleInfo.send(embed=embed)
                peopleInfoLinks.append(embedInfo)
            for weapon in weapons:
                embed = createWeaponEmbed(weapon)
                embedInfo = await weaponsInfo.send(embed=embed)
                weaponInfoLinks.append(embedInfo)
            for adjective in adjectives:
                embed = createAdjectiveEmbed(adjective)
                embedInfo = await adjectivesInfo.send(embed=embed)
                adjectiveInfoLinks.append(embedInfo)
            for place in places:
                embed = createPlaceLongEmbed(place)
                embedInfo = await placeInfo.send(embed=embed)
                placeInfoLinks.append(embedInfo)
            
            linker = "https://discord.com/channels/" + str(guildID) + "/"

            peopleLinks = []
            weaponLinks = []
            adjectiveLinks = []
            placeLinks = []

            for personNum in range(len(people)):
                link = linker + str(peopleInfo.id) + "/" + str(peopleInfoLinks[personNum].id)
                peopleLinks.append(link)
            for weaponNum in range(len(weapons)):
                link = linker + str(weaponsInfo.id) + "/" + str(weaponInfoLinks[weaponNum].id)
                weaponLinks.append(link)
            for adjectiveNum in range(len(adjectives)):
                link = linker + str(adjectivesInfo.id) + "/" + str(adjectiveInfoLinks[adjectiveNum].id)
                adjectiveLinks.append(link)
            for placeNum in range(len(places)):
                link = linker + str(placeInfo.id) + "/" + str(placeInfoLinks[placeNum].id)
                placeLinks.append(link)

            matchMessages = []
            weaponPersonAdjectiveTicker = 0

            for matchNum in range(numberOfMatches):
                #match = adjectives[weaponPersonAdjectiveTicker].capitalize()[:1:] + adjectives[weaponPersonAdjectiveTicker][1::] + people[weaponPersonAdjectiveTicker] + " with " + weapons[weaponPersonAdjectiveTicker] + " vs " + adjectives[weaponPersonAdjectiveTicker+1] + people[weaponPersonAdjectiveTicker+1] + " with " + weapons[weaponPersonAdjectiveTicker+1] + " " + places[matchNum] + "!"
                adjectiveFirst = adjectives[weaponPersonAdjectiveTicker].capitalize()[:1:] + adjectives[weaponPersonAdjectiveTicker][1::]
                print("[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker+1], places[matchNum], placeLinks[matchNum]))
                embed = discord.Embed(title="Match #" + str(numofMatches + matchNum), description= "[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker+1], places[matchNum], placeLinks[matchNum]), color=0xFF9900)
                matchMessage = await pollChannel.send(embed=embed)
                matchMessages.append(matchMessage)
                weaponPersonAdjectiveTicker+=2

            await pollChannel.send("<@&613144506757283974>")
            
            personIDList = []
            for i in people:
                personID = findEmojiID(i)
                personIDList.append(personID)       

            personEmojiList = []
            for personID in personIDList:
                personEmoji = checkForEmoji(personID)
                personEmojiList.append(personEmoji)
            
            emojiTicker = 0
            for match in matchMessages:
                await match.add_reaction(personEmojiList[emojiTicker])
                await match.add_reaction(personEmojiList[emojiTicker + 1])
                emojiTicker+=2
            print("Completed!")
        #Quick set up for custom matches and brackets- in this case, the presidential bracket. Just throw the people into the code manually and you're good to go!
        if message.content.startswith("*verifySuggestions"):
            await message.delete()
            suggestionFile = open("suggestions.txt", "r", encoding='utf-8-sig')
            suggestionsFull = suggestionFile.read()
            suggestions = suggestionsFull.split("\n")
            suggestionFile.close()

            peopleFile = open("people.txt", "r", encoding='utf-8-sig')
            peopleFull = peopleFile.read()
            people = peopleFull.split("\n")
            peopleFile.close()

            newList = []
            for suggestion in suggestions:
                if suggestion in people:
                    print(str(suggestion) + " invalid!")
                else:
                    newList.append(suggestion)
            
            newString = ""

            for person in newList:
                newString = newString + "\n" + person

            newFile = open("sanitizedSuggestions.txt", "w", encoding='utf-8-sig')
            newFile.write(newString)
            newFile.close() 
        #Checks if the suggestions are in the bot or not.
        if message.content.startswith("*downloadEmojis"):
            suggestionsFile = open("sanitizedSuggestions.txt", "r", encoding='utf-8-sig')
            suggestionsFull = suggestionsFile.read()
            suggestions = suggestionsFull.split("\n")

            #suggestions = ["Taylor Swift"]
            
            for suggestion in suggestions:
                counter = 1
                article = wikipedia.page(suggestion, auto_suggest=False)
                
                mainPhoto = get_wiki_main_image(suggestion)
                urllib.request.urlretrieve(mainPhoto, "Pictures\\AutoDownload\\" + suggestion + ".png") 
                #img = Image.open("George Washington Photos\\" + suggestion + str("NEW") + ".png") 
                #img.show()
                print("\n")
        #Downloads all emojis.
        if message.content.startswith("*WIT"):
            print("WeaponInfoTesting!")
            adjectiveTiersFile = open("Armory\\Tiers\\weaponTiers.txt", "r", encoding='utf-8-sig')
            adjectiveTiersFull = adjectiveTiersFile.read()
            adjectiveTiersArray = adjectiveTiersFull.split("\n")
            for tier in adjectiveTiersArray:
                print("Tier: " + tier)
                tierFile = open("Armory\\Tiers\\" + tier + ".txt", "r", encoding='utf-8-sig')
                tierFull = tierFile.read()
                tierArray = tierFull.split("\n")
                for weapon in tierArray:
                    print(weapon)
                    weaponEmbed = createWeaponEmbed(weapon)
                    await message.channel.send(embed=weaponEmbed)
        #Sends all the info for each and every weapon.
        if message.content.startswith("*AIT"):
            print("adjectivesInfoTesting!")
            adjectivesQuant = 16
            for numTier in range(adjectivesQuant):
                print("Tier: Tier" + str(numTier+1))
                tierFile = open("Adjectives\\Tier" + str(numTier+1) + ".txt", "r", encoding='utf-8-sig')
                tierFull = tierFile.read()
                tierArray = tierFull.split("\n")
                for adjective in tierArray:
                    print(adjective)
                    adjectiveEmbed = createAdjectiveEmbed(adjective)
                    await message.channel.send(embed=adjectiveEmbed)
        #Sends all the info for each and every adjective.
        if message.content.startswith("*ATLAS"):
            print("Places Info Testing!")
            placeFile = open("Atlas\\placesName.txt", "r", encoding='utf-8-sig')
            placeFull = placeFile.read()
            placeArray = placeFull.split("\n")
            for place in placeArray:
                embed = createPlaceEmbed(place)
                await message.channel.send(embed=embed)
        #Sends all the info for each and every place.
        if message.content.startswith("*messageCreator"):
                matchNum = 0

                pollChannel = message.channel
                peopleInfo = message.channel
                weaponsInfo = message.channel
                adjectivesInfo = message.channel
                placesInfo = message.channel
                for channel in message.guild.text_channels:
                    if channel.name == "historical-death-match-polls":
                        print("found #" + channel.name)
                        pollChannel = channel
                    if channel.name == "historical-people-info":
                        print("found #" + channel.name)
                        peopleInfo = channel
                    if channel.name == "historical-weapons-info":
                        print("found #" + channel.name)
                        weaponsInfo = channel
                    if channel.name == "historical-places-info":
                        print("found #" + channel.name)
                        placeInfo = channel
                    if channel.name == "historical-adjectives-info":
                        print("found #" + channel.name)
                        adjectivesInfo = channel

                person1 = generatePerson()
                personEmbed1 = createPersonEmbed(person1[0])
                person2 = generatePerson()
                personEmbed2 = createPersonEmbed(person2[0])
                weapons = generateWeaponPair()
                weaponEmbeds = [createWeaponEmbed(weapons[0]), createWeaponEmbed(weapons[1])]
                adjectives = generateAdjectivePair()
                adjectiveEmbeds = [createAdjectiveEmbed(adjectives[0]), createAdjectiveEmbed(adjectives[1])]
                place = generatePlace()
                placeEmbed = createPlaceLongEmbed(place)
                adjective1Text = adjectives[0].capitalize()[:1:] + adjectives[0][1::]

                personEmbed1ID = await peopleInfo.send(embed=personEmbed1)
                personEmbed2ID = await peopleInfo.send(embed=personEmbed2)

                weaponEmbed1ID = await weaponsInfo.send(embed=weaponEmbeds[0])
                weaponEmbed2ID = await weaponsInfo.send(embed=weaponEmbeds[1])

                adjectiveEmbed1ID = await adjectivesInfo.send(embed=adjectiveEmbeds[0])
                adjectiveEmbed2ID = await adjectivesInfo.send(embed=adjectiveEmbeds[1])

                placeEmbedID = await placeInfo.send(embed=placeEmbed)

                guildID = message.guild.id
                linker = "https://discord.com/channels/" + str(guildID) + "/"
                
                adjective1Link = linker + str(adjectivesInfo.id) + "/" + str(adjectiveEmbed1ID.id)
                person1Link = linker + str(peopleInfo.id) + "/" + str(personEmbed1ID.id)
                weapons1Link = linker + str(weaponsInfo.id) + "/" + str(weaponEmbed1ID.id)
                adjective2Link = linker + str(adjectivesInfo.id) + "/" + str(adjectiveEmbed2ID.id)
                person2Link = linker + str(peopleInfo.id) + "/" + str(personEmbed2ID.id)
                weapons2Link = linker + str(weaponsInfo.id) + "/" + str(weaponEmbed2ID.id)
                placeLink = linker + str(placeInfo.id) + "/" + str(placeEmbedID.id)

                embed = discord.Embed(title="Match #" + str(matchNum), description="[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjective1Text, adjective1Link, person1[0], person1Link, weapons[0], weapons1Link, adjectives[1], adjective2Link, person2[0], person2Link, weapons[1], weapons2Link, place, placeLink), color=0xFF9900)
                matchMessage = await message.channel.send(embed=embed)
                
                emoji1 = getEmoji(person1[0])
                emoji2 = getEmoji(person2[0])
                await matchMessage.add_reaction(emoji1)
                await matchMessage.add_reaction(emoji2)
        #Tests for the new embed messages!
        if message.content.startswith("*testTradingCards"):
            rarityList = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
            for number in range(5):
                personName = generatePerson()[0]
                personEmoji = getEmoji(personName)
                personURL = str(personEmoji.url)

                personName = checkLinks(personName)
                article = wikipedia.page(personName, auto_suggest=False)
                infoLink = article.url

                summary = article.summary.split('\n')
                summaryPersonal = summaryShortest(str(summary[0]))
                print("--break--")
                rarityNum = random.randint(0, len(rarityList)-1)
                rarity = rarityList[rarityNum]

                stats = generateStats(rarity)
                
                person1 = TradingCard(personName, personURL, infoLink, stats, "Dreamer", rarity, summaryPersonal)
                embed = person1.sendCard()
                await message.channel.send(embed=embed)
                person1.sendGraph()
                await message.channel.send(file=discord.File("file.png"))
        #Test message for creating Trading Cards!
        if message.content.startswith("*allSongs"):        
                songsFile = open("Competition Exclusive Info\\Songs\\songs.txt", "r", encoding='utf-8-sig')
                songsFull = songsFile.read()
                songs = songsFull.split("\n")
                songsFile.close()
                for song in songs:
                    print("Song: " + song)
                    embed = createSongEmbed(song)
                    await message.channel.send(embed=embed)
        #Test message that sends all songs!
        if message.content.startswith("*allMinigames"):
                minigamesFile = open("Competition Exclusive Info\\Mario Party 10 Minigames\\minigames.txt", "r", encoding='utf-8-sig')
                minigamesFull = minigamesFile.read()
                minigames = minigamesFull.split("\n")
                for minigame in minigames:
                    embed = createMarioMinigameEmbed(minigame)
                    await message.channel.send(embed=embed)
        #Test message to send all Mario Party Minigames
        if message.content.startswith("*allJudges"):
                judgesFile = open("Competition Exclusive Info\\Judges\\Cleaning Competition\\judges.txt", "r", encoding='utf-8-sig')
                judgesFull = judgesFile.read()
                judges = judgesFull.split("\n")
                judgesFile.close()
                for judgeTrio in judges:
                    judgesIndiv = judgeTrio.split(", ")
                    for judge in judgesIndiv:
                        embed = createJudgeEmbedCleaning(judge, "Cleaning", judgeTrio)
                        await message.channel.send(embed=embed)
                judgesFile = open("Competition Exclusive Info\\Judges\\Cooking Contest\\judges.txt", "r", encoding='utf-8-sig')
                judgesFull = judgesFile.read()
                judges = judgesFull.split("\n")
                judgesFile.close()
                for judge in judges:
                    embed = createJudgeEmbedCooking(judge, "Cooking")
                    await message.channel.send(embed=embed)
        #Test message to send all judges for both Cooking and Cleaning
        if message.content.startswith("*allFood"):        
                foodsFile = open("Competition Exclusive Info\\Food\\Food\\dishes.txt", "r", encoding='utf-8-sig')
                foodsFull = foodsFile.read()
                foods = foodsFull.split("\n")
                foodsFile.close()
                for food in foods:
                    embed = createFoodEmbed(food)
                    await message.channel.send(embed=embed)
        #Test message to send all food dishes.
        if message.content.startswith("*allPies"):
                piesFile = open("Competition Exclusive Info\\Food\\Pies\\pies.txt", "r", encoding='utf-8-sig')
                piesFull = piesFile.read()
                pies = piesFull.split("\n")
                piesFile.close()
                for pie in pies:
                    embed = createPieEmbed(pie)
                    await message.channel.send(embed=embed)
        #Test message to send all pies.
        if message.content.startswith("*drunkardsUnite"):
                drinksFile = open("Competition Exclusive Info\\Drinks\\drinks.txt", "r", encoding='utf-8-sig')
                drinksFull = drinksFile.read()
                drinks = drinksFull.split("\n")

                for drink in drinks:
                    embed = createDrinkEmbed(drink)
                    await message.channel.send(embed=embed)
        #Test message to send all drinks.
        if message.content.startswith("*mhaCharacters"):
            characterFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')
            characters = characterFile.read().split("\n")

            for character in characters:
                print(character)
                embed = createMHAembed(character)
                await message.channel.send(embed=embed)
        #prints all the MHA characters
        if message.content.startswith("*stats"):
                channel = client.get_channel(773719674927972424)
                print("Channel: " + channel.name)

                peopleFile = open("people.txt", "r", encoding='utf-8-sig')
                peopleFull = peopleFile.read()
                peopleArray = peopleFull.split("\n")

                weaponTierFile = open("Armory\\Tiers\\weaponTierList.txt", "r", encoding='utf-8-sig')
                weaponTierFull = weaponTierFile.read()
                weaponTierArray = weaponTierFull.split("\n")
                weaponArray = []
                weaponMinusFirstWord = []
                for weaponTier in weaponTierArray:
                    weaponFile = open("Armory\\Tiers\\" + weaponTier + ".txt", "r", encoding='utf-8-sig')
                    weaponFull = weaponFile.read()
                    weaponArrayTemp = weaponFull.split("\n")
                    for weapon in weaponArrayTemp:
                        weaponArray.append(weapon)
                        
                placesFile = open("Atlas\\placesName.txt", "r", encoding='utf-8-sig')
                placesFull = placesFile.read()
                placesArray = placesFull.split("\n")

                placesNoPropFile = open("Atlas\\places.txt", "r", encoding='utf-8-sig')
                placesNoPropFull = placesNoPropFile.read()
                placesNoProps = placesNoPropFull.split("\n")

                adjectiveTierFile = open("Adjectives\\TierList.txt", "r", encoding='utf-8-sig')
                adjectiveTierFull = adjectiveTierFile.read()
                adjectiveTierArray = adjectiveTierFull.split("\n")

                adjectiveArray = []
                for adjectiveTier in adjectiveTierArray:
                    adjectiveFile = open("Adjectives\\" + adjectiveTier + ".txt", "r", encoding='utf-8-sig')
                    adjectiveFull = adjectiveFile.read()
                    adjectiveArrayTemp = adjectiveFull.split("\n")
                    for adjective in adjectiveArrayTemp:
                        adjectiveArray.append(adjective)
                
                weaponry = {}
                adjectivry = {}
                placery = {}

                winWeapon = {}
                winAdjective = {}
                winPlace = {}

                for weapon in weaponArray:
                    weaponry[weapon] = 0
                    winWeapon[weapon] = 0
                for adjective in adjectiveArray:
                    adjectivry[adjective] = 0
                    winAdjective[adjective] = 0
                for place in placesArray:
                    placery[place] = 0
                    winPlace[place] = 0
                
                async for message in channel.history(limit=None):
                    embeds = message.embeds
                    for embed in embeds:
                        if not ("Round #2" in embed.title):
                            num = 0
                            print(embed.title + ": " + embed.description)
                            messageContents = embed.description.split("[")
                            for spliter in messageContents:
                                num+=1
                                bit = spliter.split("]")[0]
                                print("Bit #" + str(num) + ": ~" + bit + "~")
                                if bit in weaponArray:
                                    weaponry[bit]+=1
                                if bit in placesArray:
                                    placery[bit]+=1
                                if bit in adjectiveArray:
                                    adjectivry[bit]+=1
                    print(message.content)
                    if message.content != "*ranked" and "vs" in message.content.split(" "):
                        print("Found match")
                        placeSplit = message.content.split(" in ")[0].split(" on ")
                        for bob in placeSplit[0].split("vs"):
                            for person in peopleArray:
                                if person in bob.strip():
                                    thingSplit = bob.strip().split(person)
                                    print("Split by " + person)
                                    for item in thingSplit:
                                        word = item.strip()
                                        if word in weaponArray:
                                            weaponry[word]+=1
                                        if word in placesArray:
                                            placery[word]+=1
                                        if word in adjectiveArray:
                                            adjectivry[word]+=1
                    
                wb = xlwt.Workbook()
                ww = wb.add_sheet("Weapons")
                wa = wb.add_sheet("Adjectives")
                wp = wb.add_sheet("Places")
                row = 0

                for weapon in weaponry:
                    ww.write(row, 0, weapon)
                    ww.write(row, 1, int(weaponry[weapon]))
                    row+=1
                row = 0
                for adjective in adjectivry:
                    wa.write(row, 0, adjective[:len(adjective)-2:])
                    wa.write(row, 1, int(adjectivry[adjective]))
                    row+=1
                row = 0
                for place in placery:
                    wp.write(row, 0, placesNoProps[placesArray.index(place)])
                    wp.write(row, 1, int(placery[place]))
                    row+=1
                wb.save("Round 1 results.xls")
        #Creates an excel file with some statistics on the bot. Run at the end of each round.
        if message.content.startswith("*readResults"):
            numberMessages = message.content.split(" ")[1]
            channel = client.get_channel(773719674927972424)
            print("Channel: " + channel.name + " (" + numberMessages + " messages)")
            messageResults = []
            async for matchMessage in channel.history(limit=int(numberMessages)):
                embeds = matchMessage.embeds
                for embed in embeds:
                    if "Round #" + str(roundNumber) in embed.title:
                        num = 0
                        reactions = {}
                        #print(embed.title + ": " + embed.description)
                        for reaction in matchMessage.reactions:
                            reactions[reaction.emoji.id] = reaction.count
                        for reaction in reactions: 
                            personName = reverseEmojiID(reaction)
                        if reactions[matchMessage.reactions[0].emoji.id] > reactions[matchMessage.reactions[1].emoji.id]:
                            winnerName = reverseEmojiID(matchMessage.reactions[0].emoji.id)
                        else: 
                            if reactions[matchMessage.reactions[1].emoji.id] > reactions[matchMessage.reactions[0].emoji.id]:
                                winnerName = reverseEmojiID(matchMessage.reactions[1].emoji.id)
                            else:
                                winnerName = "Tie!"
                        print("%s|%s|%s-%s|%s" % (reverseEmojiID(matchMessage.reactions[0].emoji.id), reverseEmojiID(matchMessage.reactions[1].emoji.id), reactions[matchMessage.reactions[0].emoji.id], reactions[matchMessage.reactions[1].emoji.id], winnerName)) 
                        messageResults.append("%s|%s|%s-%s|%s" % (reverseEmojiID(matchMessage.reactions[0].emoji.id), reverseEmojiID(matchMessage.reactions[1].emoji.id), reactions[matchMessage.reactions[0].emoji.id], reactions[matchMessage.reactions[1].emoji.id], winnerName))
            bracketFile = open("LogCADiscordRound" + str(roundNumber) + ".txt", "a")
            bracketFile.write("\n")
            messageResults.reverse()
            for result in messageResults:
                bracketFile.write(result)
                bracketFile.write("\n")
            bracketFile.close()
            completeMessage = await message.channel.send("Completed!")
            print("Completed!")
            await message.delete()
            time.sleep(1)
            await completeMessage.delete()
        #Read the results of a match and output. 
        if message.content.startswith("*renameEmoji"):
            print("Renaming Emoji: " + message.guild.name)
            for emoji in message.guild.emojis:
                personName = reverseEmojiID(emoji.id)
                print(personName + " success!")
                if personName == "ï»¿Abraham Lincoln":
                    personName = "Abraham Lincoln"
                personCharSplit = list(personName)
                personName = ""
                for char in personCharSplit:
                    bannedList = [".", " ", "-", "(", ")"]
                    if not (char in bannedList):
                        personName = personName + char
                if emoji.name != personName:
                    await emoji.edit(name=personName.strip())
            await message.channel.send("Completed!")
        #Renames the emojis (minus spaces and special characters, such as dashes) to better fit naming conventions. 
        if message.content.startswith('*findServer'):
            emojiID = message.content.split(" ")[1]
            combo = findEmojiServer(emojiID)
            await message.channel.send(combo[0] + " (" + combo[1] + ")")
        #Finds the server that the given emoji ID comes from.
        if message.content.startswith("*pullContent"):
            channel = message.channel
            file = open("FCT\\franchises.txt", "a")
            stringer = ""
            async for matchMessage in channel.history(limit=None):
                file.write("\n" + matchMessage.content)
            file.close()
            await message.delete()
        #Grabs the past messages in a channel.
        if message.content.startswith("*testFCT"):
                me = message.guild.get_member(int(557273350414794772))
                color = me.color
                embed = discord.Embed(title="Lord of the Rings, but...", description="-Albus Dumbledore as Gandalf\n-She-Ra as Frodo Baggins\n-Catra as Samwise Gamgee\n-Zelda as Aragorn\n-Green Arrow as Legolas\n-Leo Valdez as Gimli\n-Fred Weasley as Pippin\n-George Weasley as Merry\n-Mitch Henderson as Boromir", color=0xFF9900)
                embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
                messageEmbed = await message.channel.send(embed=embed)
                await messageEmbed.add_reaction("✅")
                await messageEmbed.add_reaction("🌐")
                await messageEmbed.add_reaction("❌")
        if message.content.startswith("*teachersBracket"):
            channel = message.channel
            quantMessages = 0
            messageResults = []
                      
            people = []
            weapons = []
            adjectives = []
            places = []
            contests = []
            specialEmbeds = []
            specialItems = []

            match1 = {"Craig Lazarski": "","German Urioste": ""}
            match2 = {"Karen McKenzie": "", "Samuel Abrams": ""}
            match3 = {"Kristi McGauley": "","Heidi Maloy": ""}
            #match4 = {"Karen McKenzie": "","Samuel Abrams": ""}
            #match5 = {"Evelyn Sengelmann": "","Samuel Goeuriot": ""}
            #matches = [match1, match2, match3, match4, match5]
            matches = [match1, match2, match3]
            numberOfRounds = 1
            numberOfMatchesRound = 31
            numberOfMatchesTotal = 31

            matchesInfo = []
            people = []

            for match in matches:
                for person in match.keys():
                    people.append(person)

           
            guildID = message.guild.id
        
            matchesInfo = {}
            for matchNum in range(len(matches)):
                matchesInfo[matchNum] = []

            
            numberOfRounds = 1
            numberOfMatches = 3

            matchesInfo[0].append(match1)
            matchesInfo[1].append(match2)
            matchesInfo[2].append(match3)
            #matchesInfo[3].append(match4)
            #matchesInfo[4].append(match5)
            #numberOfMatches = 5
            numberOfMatches = 3

            for channel in message.guild.text_channels:
                if channel.name == "faculty-death-match-polls":
                    print("found #" + channel.name)
                    pollChannel = channel
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    weaponsInfo = channel
                if channel.name == "historical-places-info":
                    print("found #" + channel.name)
                    placeInfo = channel
                if channel.name == "historical-adjectives-info":
                    print("found #" + channel.name)
                    adjectivesInfo = channel
                if channel.name == "historical-contests-info":
                    print("found #" + channel.name)
                    contestInfo = channel
                if channel.name == "historical-contest-specific-info":
                    print("found #" + channel.name)
                    contestItemsInfo = channel
            
            
            for matchNumber in range(numberOfMatches):
                matcherInfo = generateContest(publicMatches=True)
                #Returned (in order) adjectivePair, weaponPair, place, specialItems, contestInformation
                adjectiveDict = {}
                weaponDict = {}
                placeDict = {}
                variant = ""
                contestDict = {}
                if matcherInfo != None:
                    for adjective in matcherInfo[0]:
                        adjectives.append(adjective)
                        adjectiveDict[adjective] = ""
                matchesInfo[matchNumber].append(adjectiveDict)
                if matcherInfo != None:
                    for weapon in matcherInfo[1]:
                        weapons.append(weapon)
                        weaponDict[weapon] = ""
                matchesInfo[matchNumber].append(weaponDict)
                if matcherInfo != None and matcherInfo != "" and matcherInfo != " ":
                    places.append(matcherInfo[2])
                    placeDict[matcherInfo[2]] = ""
                matchesInfo[matchNumber].append(placeDict)
                if matcherInfo != None:
                    for specialItem in matcherInfo[3]:
                        specialEmbeds.append(specialItem[1])
                        specialItems.append(specialItem)
                matchesInfo[matchNumber].append(matcherInfo[3])
                if matcherInfo != None:      
                    contests.append(matcherInfo[4])
                    contestDict[matcherInfo[4][0]] = ""
                    variant = matcherInfo[4][1]
                matchesInfo[matchNumber].append(contestDict)
                matchesInfo[matchNumber].append(variant)

            pollChannel = message.channel
            peopleInfo = message.channel
            placeInfo = message.channel
            weaponsInfo = message.channel
            adjectivesInfo = message.channel
            contestInfo = message.channel
            contestItemsInfo = message.channel

            for channel in message.guild.text_channels:
                if channel.name == "faculty-death-match-polls":
                    print("found #" + channel.name)
                    pollChannel = channel
                if channel.name == "historical-people-info":
                    print("found #" + channel.name)
                    peopleInfo = channel
                if channel.name == "historical-weapons-info":
                    print("found #" + channel.name)
                    weaponsInfo = channel
                if channel.name == "historical-places-info":
                    print("found #" + channel.name)
                    placeInfo = channel
                if channel.name == "historical-adjectives-info":
                    print("found #" + channel.name)
                    adjectivesInfo = channel
                if channel.name == "historical-contests-info":
                    print("found #" + channel.name)
                    contestInfo = channel
                if channel.name == "historical-contest-specific-info":
                    print("found #" + channel.name)
                    contestItemsInfo = channel
            
            print("Poll Channel: #" + pollChannel.name)

            lastInfo = open("lastInfo.txt", "w", encoding='utf-8-sig')
            stringsList = []
            for person in people:
                stringsList.append(person)
            for weapon in weapons:
                stringsList.append(weapon)
            for adjective in adjectives:
                stringsList.append(adjective)
            for place in places:
                stringsList.append(place)

            for i in stringsList:
                lastInfo.write(i + "\n")
            
            peopleInfoLinks = []
            weaponInfoLinks = []
            placeInfoLinks = []
            adjectiveInfoLinks = []
            specialItemInfoLinks = []
            contestInfoLinks = []

            linker = "https://discord.com/channels/" + str(guildID) + "/"
            #match should be a list of dicts
            for match in matchesInfo.values():
                print("\nMatch: " + str(match))
                for person in match[0]:
                    print(str(match[0]))
                    embed = createPersonEmbed(person, teacherBracket=True)
                    embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                    embedInfo = await peopleInfo.send(embed=embed)
                    peopleInfoLinks.append(embedInfo.id)
                    match[0][person] = str(embedInfo.id)     
                for weapon in match[2]:
                    embed = createWeaponEmbed(weapon)
                    embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                    embedInfo = await weaponsInfo.send(embed=embed)
                    weaponInfoLinks.append(embedInfo.id)
                    match[2][weapon] = str(embedInfo.id)
                for adjective in match[1]:
                    embed = createAdjectiveEmbed(adjective)
                    embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                    embedInfo = await adjectivesInfo.send(embed=embed)
                    adjectiveInfoLinks.append(embedInfo.id)
                    match[1][adjective] = str(embedInfo.id)
                for place in match[3]:
                    print("Place (Checking for Null): ~" + place + "~")
                    if place != "":
                        embed = createPlaceLongEmbed(place)
                        embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                        embedInfo = await placeInfo.send(embed=embed)
                        placeInfoLinks.append(embedInfo.id)
                        match[3][place] = str(embedInfo.id)
                for specialItem in match[4]:
                    embed = match[4][specialItem]
                    embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                    embedInfo = await contestItemsInfo.send(embed=embed)
                    specialItemInfoLinks.append(embedInfo.id)
                    match[4][specialItem] = str(embedInfo.id)
                for contest in match[5]:
                    if contest != "Death Match Classic":
                        embed = createContestEmbed(contest, match[6])
                    else:
                        embed = createHDMClassicEmbed()
                    embed.add_field(name="Return to Poll",value="[Here](%s)" % (str(linker)+str(pollChannel.id)), inline=False)
                    embedInfo = await contestInfo.send(embed=embed)
                    contestInfoLinks.append(embedInfo.id)
                    match[5][contest] = str(embedInfo.id)

            peopleLinks = []
            weaponLinks = []
            adjectiveLinks = []
            placeLinks = []
            itemLinks = []
            contestLinks = []
            #matchInfo = [people, adjectives, weapons, places, specialItems, contest, variant]
            for match in matchesInfo.values():
                print(str(matchesInfo))
                print("Oof: " + str(match))
                for person in match[0]:
                    match[0][person] = linker + str(peopleInfo.id) + "/" + match[0][person]
                for adjective in match[1]:
                    match[1][adjective] = linker + str(adjectivesInfo.id) + "/" + match[1][adjective]
                for weapon in match[2]:
                    match[2][weapon] = linker + str(weaponsInfo.id) + "/" + match[2][weapon]
                for place in match[3]:
                    if place != "":
                        match[3][place] = linker + str(placeInfo.id) + "/" + match[3][place]
                for specialItem in match[4]:
                    match[4][specialItem] = linker + str(contestItemsInfo.id) + "/" + match[4][specialItem]
                for contest in match[5]:
                    match[5][contest] = linker + str(contestInfo.id) + "/" + match[5][contest]
            
            matchMessages = []
            matchNum = 0
            for match in matchesInfo.values():
                matchMessage = generateMatchMessage(match, True)
                embed = discord.Embed(title="Round #" + str(numberOfRounds) + " Match #" + str(numberOfMatchesRound + matchNum) + " (Total Match #" + str(numberOfMatchesTotal + matchNum) + ")", description=matchMessage, color=0xFF9900)
                matchMessage = await pollChannel.send(embed=embed)
                matchMessages.append(matchMessage)
                matchNum+=1


            await pollChannel.send("<@&613144506757283974>")
            
            emojiTicker = 0
            for match in matchMessages:
                await match.add_reaction(getEmoji(people[emojiTicker], teacherBracket=True))
                await match.add_reaction(getEmoji(people[emojiTicker+1], teacherBracket=True))
                emojiTicker+=2
            print("Completed!")
        #Matches for Teacher's Bracket in March Madness 2022
    if message.content.startswith("*info"):
                messageContent = message.content[6::]
                
                peopleFile = open("people.txt", "r", encoding='utf-8-sig')
                peopleFull = peopleFile.read()
                peopleArray = peopleFull.split("\n")

                weaponTierFile = open("Armory\\Tiers\\weaponTierList.txt", "r", encoding='utf-8-sig')
                weaponTierFull = weaponTierFile.read()
                weaponTierArray = weaponTierFull.split("\n")
                weaponArray = []
                weaponMinusFirstWord = []
                for weaponTier in weaponTierArray:
                    weaponFile = open("Armory\\Tiers\\" + weaponTier + ".txt", "r", encoding='utf-8-sig')
                    weaponFull = weaponFile.read()
                    weaponArrayTemp = weaponFull.split("\n")
                    for weapon in weaponArrayTemp:
                        weaponArray.append(weapon)
                        
                placesFile = open("Atlas\\placesName.txt", "r", encoding='utf-8-sig')
                placesFull = placesFile.read()
                placesArray = placesFull.split("\n")

                adjectiveTierFile = open("Adjectives\\TierList.txt", "r", encoding='utf-8-sig')
                adjectiveTierFull = adjectiveTierFile.read()
                adjectiveTierArray = adjectiveTierFull.split("\n")

                adjectiveArray = []
                for adjectiveTier in adjectiveTierArray:
                    adjectiveFile = open("Adjectives\\" + adjectiveTier + ".txt", "r", encoding='utf-8-sig')
                    adjectiveFull = adjectiveFile.read()
                    adjectiveArrayTemp = adjectiveFull.split("\n")
                    for adjective in adjectiveArrayTemp:
                        adjectiveArray.append(adjective)
                
                
                songsFile = open("Competition Exclusive Info\\Songs\\songs.txt", "r", encoding='utf-8-sig')
                songsFull = songsFile.read()
                songsArray = songsFull.split("\n")

                minigamesFile = open("Competition Exclusive Info\\Mario Party 10 Minigames\\minigames.txt", "r", encoding='utf-8-sig')
                minigamesFull = minigamesFile.read()
                minigamesArray = minigamesFull.split("\n")

                print("Query: |" + messageContent + "|")

                if messageContent in peopleArray or messageContent == "Abraham Lincoln":
                    print("Query is Person")
                    embed = createPersonEmbed(messageContent)
                    await message.channel.send(embed=embed)
                else:
                    if messageContent in weaponArray or "a " + messageContent in weaponArray or "an " + messageContent in weaponArray:
                        print("Query is Weapon")
                        if "a " + messageContent in weaponArray:
                            messageContent = "a " + messageContent
                        if "an " + messageContent in weaponArray:
                            messageContent = "an " + messageContent
                        embed = createWeaponEmbed(messageContent)
                        await message.channel.send(embed=embed)
                    else:
                        if messageContent in placesArray or messageContent + " " in placesArray:
                            print("Query is Place")
                            embed = createPlaceEmbed(messageContent + " ")
                            await message.channel.send(embed=embed)
                        else:
                            if messageContent + " " in adjectiveArray:
                                print("Query is Adjective")
                                embed = createAdjectiveEmbed(messageContent + " ")
                                await message.channel.send(embed=embed)
                            else:
                                if messageContent in songsArray:
                                    print("Query is Song")
                                    embed = createSongEmbed(messageContent)
                                    await message.channel.send(embed=embed)
                                else:
                                    if messageContent in minigamesArray:
                                        print("Query is Mario Party 10 Minigame")
                                        embed = createMarioMinigameEmbed(messageContent)
                                        await message.channel.send(embed=embed)
                                    else:
                                        await message.channel.send(messageContent + " was not found.")
    #Grab info on a person, weapon, adjective, or place!
    if message.content.startswith("*newPeopleInfo"):
                weaponTierFile = open("newPeople.txt", "r", encoding='utf-8-sig')
                weaponTierFull = weaponTierFile.read()
                weaponTierArray = weaponTierFull.split('\n')
                weaponsInfo = message.channel
                for channel in message.guild.text_channels:
                    if channel.name == "historical-people-info":
                        print("found #" + channel.name)
                        weaponsInfo = channel
                for v in range(len(weaponTierArray)):
                    if v % 2 == 0:
                        embed = createPersonEmbed(weaponTierArray[v])
                        await weaponsInfo.send(embed=embed)
    #Send the info on the new people. 
    global presidentalNames
    if message.content in presidentalNames:
                global numberOfLincolnPics
                randomNum = random.randint(1,15)
                picturePath = "lincoln" + str(randomNum)
                
                numberOfLincolnPics+=1
                print("Lincoln Pic #" + str(numberOfLincolnPics) + ": " + picturePath + " (User: " + message.author.name + "; command: " + message.content + ")")

                if os.path.exists("Pictures\\Lincoln\\" + picturePath + ".png"):
                    await message.channel.send(file=discord.File("Pictures\\Lincoln\\" + picturePath + ".png"))
                else:
                        if os.path.exists("Pictures\\Lincoln\\" + picturePath + ".jpg"):
                            await message.channel.send(file=discord.File("Pictures\\Lincoln\\" + picturePath + ".jpg"))
    #Get a picture of Abraham Lincoln. Not sure why you want this, but it's good to have options.
    if message.content.startswith("*placeMe"):
                place = generatePlaceAdverb()
                await message.channel.send(place.strip().capitalize() + "!")
    #Generate a place.
    if message.content.startswith("*weaponMe"):
                weapon = generateWeapon()
                await message.channel.send(weapon.strip().capitalize() + "!")
    #Generate a weapon. 
    if message.content.startswith("*adjectiveMe"):
                adjective = generateAdjective()
                await message.channel.send(adjective.strip().capitalize() + "!")
    #Generate an adjective
    if message.content.startswith("*personMe"):
                person = generatePerson()
                await message.channel.send(person[0] + "!")
    #Generate a random historical figure.
    if message.content.startswith("*mhaMe"):
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()
        RNG = random.randint(0, len(peopleArray)-1)
        await message.channel.send(peopleArray[RNG] + "!")
    #Generate a random MHA character.
    if message.content.startswith("*declare"):
        declaredPerson = message.content[9::].strip()
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()

        
        if declaredPerson in peopleArray:
            pityChart[message.author.id] = declaredPerson
            declaredFile = open("declaredGacha.txt", "w", encoding='utf-8-sig')
            #print(str(pityChart))
            for personID in pityChart.keys():
                declaredFile.write(str(personID) + "|" + pityChart[personID] + "\n")
            declaredFile.close()
            await message.channel.send("<@" + str(message.author.id) + "> has declared " + declaredPerson + "!")
        else:
            if declaredPerson == "":
                test = ""
                try:
                    test = pityChart[message.author.id]
                    await message.channel.send("<@" + str(message.author.id) + "> has " + pityChart[message.author.id] + " declared!")
                except:
                    await message.channel.send("<@" + str(message.author.id) + "> has nobody declared!")

            #print("|" + declaredPerson + "|")
            #print(str(peopleArray))
            else:
                await message.channel.send(declaredPerson + " doesn't exist!")
    #Declare a MHA character for the gacha system.
    if message.content.startswith("*roll"):
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()

        RNG = random.randint(0, len(peopleArray))

        chosen = peopleArray[RNG]

        pityFile = open("pityCount.txt", "w", encoding='utf-8-sig')
        pityCurrent = 0
        try:
            pityCurrent = pityCount[message.author.id]
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
        except:
            pityCount[message.author.id] = 0
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")

        immutablePity = pityCurrent
        if pityCurrent >= pityNum:
            pityCurrent = pityNum
        pityCheck = random.randint(pityCurrent, 100)

        test = ""
        try:
            test = pityChart[message.author.id]
        except:
            hello = "yes"
            #print("Nothing listed for declare")
            #pityChart[message.author.id] = "[Error]"
        if pityCheck == 100 or chosen == pityChart[message.author.id]:
            chosen = pityChart[message.author.id]
            pityCount[message.author.id] = 0
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
            try:
                currentStats[message.author.id][chosen]+=1
            except:
                try: 
                    currentStats[message.author.id][chosen] = 1
                except:
                    currentStats[message.author.id] = {chosen: 1}
            writeFile = open("Gacha Storage Characters\\" + str(message.author.id) + ".txt", "w", encoding='utf-8-sig')
            for person in currentStats[message.author.id].keys():
                writeFile.write(person + "|" + str(currentStats[message.author.id][person]) + "\n")
            writeFile.close()
            #print(str(currentStats))
            await message.channel.send("<@" + str(message.author.id) + ">, you got " + chosen + "! (pity count: " + str(immutablePity) + ")")
        else:
            pityCount[message.author.id] += 1
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
            try:
                currentStats[message.author.id][chosen]+=1
            except:
                try: 
                    currentStats[message.author.id][chosen] = 1
                except:
                    currentStats[message.author.id] = {chosen: 1}
            #print(str(currentStats))
            writeFile = open("Gacha Storage Characters\\" + str(message.author.id) + ".txt", "w", encoding='utf-8-sig')
            for person in currentStats[message.author.id].keys():
                writeFile.write(person + "|" + str(currentStats[message.author.id][person]) + "\n")
            writeFile.close()
            await message.channel.send(chosen + "!")
        pityFile.close()
    #Roll on the gacha wheel.
    if message.content.startswith("*currentStats"):
        print(str(currentStats))

        finder = message.content[16:len(message.content)-1:]
        if finder == "":
            finder = message.author.id
        test = []
        try:
            test = currentStats[int(finder)]
        except:
            currentStats[int(finder)] = {}
        print(currentStats[int(finder)])
        statsArray = sorted(currentStats[int(finder)].items(), key=lambda x:x[1], reverse=True)
        newMessage = "__<@" + str(finder) + "> stats:__"
        statsList = dict(statsArray)

        totalNum = 0
        for person in statsList.keys():
            totalNum+=statsList[person]
        for person in statsList.keys():
            if statsList[person] > totalNum * 0.02:
                newMessage = newMessage + "\n" + person + ": " + str(statsList[person])
        newMessage = newMessage + "\n" + "**Total Rolls: ** " + str(totalNum)
        newMessage = newMessage + "\n" + "**Characters Obtained: **" + str(len(statsList.keys())) + "/220"
        
        mhaFile = open("mhaCharacters.txt", "r", encoding="utf-8-sig")
        mhaArray = mhaFile.read().split("\n")
        if len(statsList.keys()) >= 200 and len(statsList.keys()) < 220:
            newMessage = newMessage + "\n" + "**Characters Remaining: **"
            for character in mhaArray:
                if not character in statsList.keys():
                    newMessage = newMessage + character + ", "
            newMessage = newMessage[0:len(newMessage)-2:]
        await message.channel.send(newMessage)
    #Check your current stats with the gacha.      
    if message.content.startswith("*pity"):
        pityCurrent = 0
        finder = message.content[8:len(message.content)-1:]
        if finder == "":
            finder = message.author.id

        try:
            pityCurrent = pityCount[int(finder)]
        except:
            pityCount[int(finder)] = 0
        await message.channel.send("<@" + str(finder) + "> has a current pity count of " + str(pityCurrent))
    #Checks your current pity.  
    if message.content.startswith("*checkCharacter"):
        characterName = message.content[16::]
        finder = message.author.id
        print(str(len(message.content)))
        if characterName == "" or len(message.content) == 15:
            try:
                test = currentStats[int(finder)]
            except:
                currentStats[int(finder)] = {}
            print(currentStats[int(finder)])
            statsArray = sorted(currentStats[int(finder)].items(), key=lambda x:x[1], reverse=True)
            newMessage = "__<@" + str(finder) + "> Characters:__"
            statsList = dict(statsArray)
            for person in statsList.keys():
                newMessage = newMessage + "\n" + person + ": " + str(statsList[person])
            await message.channel.send(newMessage)
        else:
            try:
                
                await message.channel.send("<@" + str(finder) + "> has " + str(currentStats[finder][characterName]) + " of " + characterName)
            except:
                mhaCharacterFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')
                mhaCharacters = mhaCharacterFile.read().split("\n")
                mhaCharacterFile.close()
                if characterName in mhaCharacters:
                    await message.channel.send("<@" + str(finder) + "> has 0 of " + characterName)
                else:
                    await message.channel.send(characterName + " doesn't exist!")
    #Checks the quantity of a character owned.
    if message.content.startswith("*contestant"):
        coin = random.randint(0,1)
        human = "[Error]"
        if coin == 0:
            person = generatePerson()
            human = person[0]
        else:
            peopleFile = open("mhaBracket.txt", "r", encoding='utf-8-sig')

            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            peopleFile.close()
            RNG = random.randint(0, len(peopleArray))
            human = peopleArray[RNG]
        adjective = generateAdjective().capitalize()
        weapon = generateWeapon()

        await message.channel.send(adjective + human + " with " + weapon)
    #Generates an adjective, person, and weapon.
    if message.content.startswith("*powerUp"):
        newMessage = message.content[9::]
        if newMessage == "":
            adjective = generateAdjective().strip()
            weapon = generateWeapon().strip()
            await message.channel.send("You are " + adjective + " and you have " + weapon)
        else:
            adjective = generateAdjective().capitalize()
            weapon = generateWeapon()
            await message.channel.send(adjective + message.content[9::] + " with " + weapon)
    #Gives a weapon and an adjective to someone.
    if message.content.startswith("*help"):
                me = message.guild.get_member(int(557273350414794772))
                color = me.color
                embed = discord.Embed(title="Help", description="", color=0xFF9900)
                embed.add_field(name="*newPeopleInfo", value="Get the scoop on the newest additions to Death Match Bot!", inline=False)
                embed.add_field(name="*lincoln", value="Get a photo of the 16th president of the USA. There's now 15 different photos!", inline=False)
                embed.add_field(name="*roosevelt", value="Also gives you photos of Abraham Lincoln, the 16th president of the USA.", inline=False)
                embed.add_field(name="*<PRESIDENTLASTNAME>", value="Also also gives you photos of Abraham Lincoln, the 16th president of the USA. *JFK also works.", inline=False)
                embed.add_field(name="*placeMe", value="Get a random place!", inline=False)
                embed.add_field(name="*weaponMe", value="Get a random weapon!", inline=False)
                embed.add_field(name="*personMe", value="Get a random person!", inline=False) 
                embed.add_field(name="*adjectiveMe", value="Get a random adjective!", inline=False) 
                embed.add_field(name="*match", value="Created your very own death match, with two combatants, each armed and adjectived, and a location!", inline=False)
                embed.add_field(name="*react", value="React with people emojis! The syntax is '*react MESSAGEID CHANNELID EMOJIFIRSTNAME EMOJILASTNAME`.", inline=False)
                embed.add_field(name="*register/suggest", value="Suggest new people for the bot!", inline=False)
                embed.add_field(name="*info", value="Get an info card about a person, weapon, place, or adjective.", inline=False)
                embed.add_field(name="*about", value="Get some info on the bot.", inline=False)
                embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
                await message.channel.send(embed=embed)
    #The help command
    if message.content.startswith("*match"):
                person1 = generatePerson()
                person2 = generatePerson()
                weapons = generateWeaponPair()
                adjectives = generateAdjectivePair()
                place = generatePlace()
                match = adjectives[0].capitalize()[:1:] + adjectives[0][1::] + person1[0] + " with " + weapons[0] + " vs " + adjectives[1] + person2[0] + " with " + weapons[1] + " " + place + "!"
                matchMessage = await message.channel.send(match)
                emoji1 = getEmoji(person1[0])
                emoji2 = getEmoji(person2[0])
                await matchMessage.add_reaction(emoji1)
                await matchMessage.add_reaction(emoji2)
    #Single match for everyone to use. Currently only runs classic HDM matches. 
    if message.content.startswith("*react"):
                messageArray = message.content.split(" ")
                if len(messageArray) >= 3:
                    messageArray.pop(0)
                    mixedMessageChannel = messageArray[0]
                    idArray = mixedMessageChannel.split("-")
                    print("Message ID: " + str(idArray[1]))
                    print("Channel ID: " + str(idArray[0]))
                    channelID = message.guild.get_channel(int(idArray[0]))
                    msg = await channelID.fetch_message(idArray[1])
                    messageArray.pop(0)
                    name = ""
                    for item in messageArray:
                        name = name + item + " "
                    name = name.strip()
                    emoji = getEmoji(name)
                    print("Person: " + name)
                    await message.delete()
                    await msg.add_reaction(emoji)
    #React with an emoji; uses the syntax `*react [channelID]-[messageID] [Emoji Name]`
    if message.content.startswith("*purgeDeathMatch"):
                async for message in message.channel.history(limit=100):
                    messageArray = message.content.split(" ")
                    commandPossible = messageArray[0]
                    commandList = ["*ranked", "*sendLastMatchInfo", "*weapons", "*places", "*newPeopleInfo", "*SuleimanSpecial", "*SuperBowlSpecial", "*resetBracket", "*resetBracket", "*peoplePics", "*lincoln", "*placeMe", "*weaponMe", "*personMe", "*help", "*react"]
                    if commandPossible in commandList:
                        await message.delete()
                await message.delete()
    #Purges all death match commands.      
    if message.content.startswith("*register") or message.content.startswith("*suggest"):
                peopleFile = open("peer.txt", "r", encoding='utf-8-sig')
                peopleFull = peopleFile.read()
                peopleID = peopleFull.split("\n")
                suggestionFile = open("suggestions.txt", "r", encoding='utf-8-sig')
                suggestions = suggestionFile.read()
                suggestionFile.close()
                suggestionsArray = suggestions.split("\n")
                people = []
                for index in range(len(peopleID)):
                    if index % 2 == 0 and (peopleID[index] != "A" and peopleID[index] != "B"):
                        people.append(peopleID[index])

                person = message.content[9:len(message.content)]
                print("Person: " + person)
                if person in people:
                    response = await message.channel.send(person + " is already in Historical Death Match! (ID " + peopleID[peopleID.index(person) + 1] + ")")
                else:
                    if person in suggestionsArray:
                        response = await message.channel.send(person + " has already been suggested (but not yet added!).")
                    else:
                        suggestionFile = open("suggestions.txt", "w", encoding='utf-8-sig')
                        suggestionFile.write(suggestions)
                        suggestionFile.write("\n" + person)
                        suggestionFile.close()
                        response = await message.channel.send("Added " + person + " to suggestions.")
                await message.delete()
                time.sleep(2)
                await response.delete()
                
    #Command to suggest new people!  
    if message.content.startswith("*about"):
                embed = discord.Embed(title="About HDM!", description='"though I would' + "'ve bribed people to get stephen hawking to win that one match" + '"\n-Harrison Truscott\nHistorical Death Match (found here https://github.com/fixmeseb/DeathMatchBot) is a Discord bot that started out when I thought, "Hey, you know what' + "'s funny?" + ' Historical figures fighting each other. I could do something with this!" And then I did. Abbreviated to HDM a lot, HDM is currently running it' + "'s third iteration of the bot (with adjectives!) on the CA Discord Server, and otherwise is soon ready to be added to other server- just reach out to me at the below Discord address or at sauronclaus@gmail.com to see if we can work something out!", color=0xFF9900)
                embed.add_field(name="Lines of Code in Main File", value=2000)
                embed.add_field(name="People", value=574)
                embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
                await message.channel.send(embed=embed)
    #Gives some info about the bot!

client.run(botToken)