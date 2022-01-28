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

from generation import generatePerson
from generation import generateWeapon
from generation import generatePlace
from generation import generatePlaceAdverb
from generation import generateAdjective
from generation import generateWeaponPair
from generation import generateAdjectivePair

from contestGeneration import generateContest
from contestGeneration import generateMatchMessage

from tradingCards import createCard
from tradingCards import grantCard
from tradingCards import generateStats

from tradingCardPerson import TradingCard
import time
    
presidentalNamesFile = open("Pictures\\Lincoln\\presidentLastNames.txt", "r")
presidentalNamesFull = presidentalNamesFile.read()
presidentalNames = presidentalNamesFull.split("\n")

numberOfLincolnPics = 0
roundNumber = int(open("matchNum.txt", "r").read().split("\n")[2])

intents = discord.Intents.all()
client = discord.Client(intents=intents)

discordEmojiList = ["test server", "1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer", "8EmojiServer"]
#List of servers with the Discord Emojis. 


tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])
CADiscord = client.get_guild(int(tokens[3]))

def findPersonPic(person):
    if os.path.exists("Pictures\\" + person.strip() + ".png"):
        return discord.File("Pictures\\" + person + '.png')
    else:
        if os.path.exists("Pictures\\" + person.strip() + ".jpg"):
            return discord.File("Pictures\\" + person + '.jpg')
#Finds the picture of a person
def findPeerIndex(personName):
    peerFile = open("peer.txt", "r")
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
def findEmojiID(personName):
    peerFile = open("peer.txt", "r")
    peerFull = peerFile.read()
    peer = peerFull.split("\n")
    peoplePeerIndex = []
    if personName == "Abraham Lincoln": 
        personName = "ï»¿Abraham Lincoln"
    print("Person Name: " + personName)
    personIndex = peer.index(personName)
    emojiID = peer[personIndex + 1]
    return emojiID
#Return the emoji ID from the person's name
def reverseEmojiID(ID):
    peerFile = open("peer.txt", "r")
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
def getEmoji(personName):
    emojiID = findEmojiID(personName)
    print(personName + " (" + str(emojiID) + ")")
    emoji = checkForEmoji(emojiID)
    return emoji
#Combines checkForEmoji() and findEmojiID()
def createPersonEmbed(person):
    personEmoji = getEmoji(person)
    personUnEdit = person
    person = checkLinks(person)
    article = wikipedia.page(person, auto_suggest=False)
    summary = article.summary.split('\n')
    summaryPersonal = summaryShort(str(summary[0]))
    embed = discord.Embed(title=article.title, description=summaryPersonal, color=0xFF9900)
    print("Emoji Name: " + personEmoji.name)
    print(summary[0])
    personURL = str(personEmoji.url)
    embed.set_image(url=personURL)
    embed.add_field(name="Link",value=article.url)
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
    

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    numberOfLincolnPics = 0
    print("Round Number: " + str(roundNumber))
    if True == True:
        if False == False:
            roundNumber = int(open("matchNum.txt", "r").read().split("\n")[2])
            channel = client.get_channel(773719674927972424)
            quantMessages = 0
            numberOfMatches = 5
            messageResults = []
            async for matchMessage in channel.history(limit=numberOfMatches+5):
                if quantMessages < 5:
                    for embeds in matchMessage.embeds:
                        if "Round #" + str(roundNumber) in matchMessage.embeds[0].title:
                                messageResults.append(returnResult(matchMessage))
                                quantMessages+=1

            bracketFile = open("LogCADiscordRound" + str(roundNumber) + ".txt", "a")
            bracketFile.write("\n")
            messageResults.reverse()
            for result in messageResults:
                bracketFile.write(result)
                bracketFile.write("\n")
            bracketFile.close()
            print("Completed!")
            
            guildID = CADiscord.id
            numberOfMatchesFile = open("matchNum.txt", "r")
            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleFile = open("CABracket.txt", "r")

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

            matchesInfo = []
            
            ticker = 0
            for matchNum in range(numberOfMatches):
                matchInfo = []
                condenser = {
                    people[ticker]: "",
                    people[ticker+1]: ""
                }
                matchInfo.append(condenser)
                ticker+=2
                matchesInfo.append(matchInfo)
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
            pollChannel = channel
            peopleInfo = channel
            placeInfo = channel
            weaponsInfo = channel
            adjectivesInfo = channel
            contestInfo = channel
            contestItemsInfo = channel

            for channel in CADiscord.text_channels:
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
            
            print("Poll Channel: #" + pollChannel.name)

            lastInfo = open("lastInfo.txt", "w")
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

            for match in matchesInfo:
                for person in match[0]:
                    embed = createPersonEmbed(person)
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
            for match in matchesInfo:
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
            for match in matchesInfo:
                matchMessage = generateMatchMessage(match, True)
                embed = discord.Embed(title="Round #" + str(numberOfRounds) + " Match #" + str(numberOfMatchesRound + matchNum) + " (Total Match #" + str(numberOfMatchesTotal + matchNum) + ")", description=matchMessage, color=0xFF9900)
                matchMessage = await pollChannel.send(embed=embed)
                matchMessages.append(matchMessage)
                matchNum+=1

            numberOfMatchesFile.close()
            numberOfMatchesFile = open("matchNum.txt", "w")
            numberOfMatchesFile.write(str(numberOfMatchesTotal + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfMatchesRound + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfRounds))
            numberOfMatchesFile.close()

            await pollChannel.send("<@&613144506757283974>")
            
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
            peopleFile = open("CABracket.txt", "w")
            peerString = ""
            for name in peopleArray:
                peerString = peerString + "\n" + name
            stringPeer = peerString[1:len(peerString)]
            peopleFile.write(stringPeer)
            peopleFile.close()
            
            emojiTicker = 0
            for match in matchMessages:
                await match.add_reaction(emoji=personEmojiList[emojiTicker])
                await match.add_reaction(emoji=personEmojiList[emojiTicker + 1])
                emojiTicker+=2
            print("Completed!")
        #Ranked matches for the CA Discord.  

client.run(botToken)