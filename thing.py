import discord
from discord.utils import get

import random
import wikipedia
import os.path

from generateNumbers import generateNumRep
from generateNumbers import newGenerateNum

from embeds import createPlaceEmbed
from embeds import createWeaponEmbed
from embeds import createPlaceLongEmbed
from embeds import createAdjectiveEmbed
from embeds import summaryShort
from embeds import checkLinks

from generation import generatePerson
from generation import generateWeapon
from generation import generatePlace
from generation import generatePlaceAdverb
from generation import generateAdjective
from generation import generateWeaponPair
from generation import generateAdjectivePair

presidentalNamesFile = open("Pictures\\Lincoln\\presidentLastNames.txt", "r")
presidentalNamesFull = presidentalNamesFile.read()
presidentalNames = presidentalNamesFull.split("\n")
numberOfLincolnPics = 0

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

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    numberOfLincolnPics = 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("*ranked") and message.author.id == userID:
        numberOfMatches = 5
        matchesVariables = []
        guildID = message.guild.id
        numberOfMatchesFile = open("matchNum.txt", "r")
        numberOfMatchesTotal = int(numberOfMatchesFile.read())

        peopleFile = open("CABracket.txt", "r")
        weaponTierFile = open("Armory\\Tiers\\weaponTiers.txt", "r")
        placesFile = open("Atlas\\places.txt", "r")
        adjectiveTierFile = open("Adjectives\\adjectiveTiers.txt")

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

        lastInfo = open("lastInfo.txt", "w")
        stringsList = [people[0], people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], weapons[0], weapons[1], weapons[2], weapons[3], weapons[4], weapons[5], weapons[6], weapons[7], weapons[8], weapons[9], places[0], places[1], places[2], places[3], places[4], adjectives[0], adjectives[1], adjectives[2], adjectives[3], adjectives[4], adjectives[5], adjectives[6], adjectives[7], adjectives[8], adjectives[9]]
        for i in stringsList:
            lastInfo.write(i + "\n")
        
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
            print("[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker], places[matchNum], placeLinks[matchNum]))
            embed = discord.Embed(title="Match #" + str(numberOfMatchesTotal + matchNum), description="[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker], places[matchNum], placeLinks[matchNum]), color=0xFF9900)
            matchMessage = await pollChannel.send(embed=embed)
            matchMessages.append(matchMessage)
            weaponPersonAdjectiveTicker+=2

        numberOfMatchesFile.close()
        numberOfMatchesFile = open("matchNum.txt", "w")
        numberOfMatchesFile.write(str(numberOfMatchesTotal + 5))
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
    if message.content.startswith("*sendLastMatchInfo") and message.author.id == userID:
        infoWrite = open("lastInfo.txt", "r")
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
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[1])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[2])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[3])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[4])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[5])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[6])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[7])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[8])
        await peopleInfo.send(embed=embed)
        embed = createPersonEmbed(info[9])
        await peopleInfo.send(embed=embed)
        embed = createWeaponEmbed(info[10])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[11])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[12])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[13])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[14])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[15])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[16])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[17])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[18])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[19])
        await weaponsInfo.send(embed=embed)
        embed = createPlaceLongEmbed(info[20])
        await placeInfo.send(embed=embed)
        embed = createPlaceLongEmbed(info[21])
        await placeInfo.send(embed=embed)
        embed = createPlaceLongEmbed(info[22])
        await placeInfo.send(embed=embed)
        embed = createPlaceLongEmbed(info[23])
        await placeInfo.send(embed=embed)
        embed = createPlaceLongEmbed(info[24])
        await placeInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[25])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[26])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[27])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[28])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[29])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[30])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[31])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[32])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[33])
        await adjectivesInfo.send(embed=embed)
        embed = createAdjectiveEmbed(info[34])
        await adjectivesInfo.send(embed=embed)
        #embed = createPlaceEmbed(info[12])
        #await placeInfo.send(embed=embed)
        #embed = createPlaceEmbed(info[13])
        #await placeInfo.send(embed=embed)
        #mbed = createPlaceEmbed(info[14])
        #await placeInfo.send(embed=embed)
    #Send the info in the file "lastInfo.txt"
    if message.content.startswith("*newPeopleInfo"):
        weaponTierFile = open("newPeople.txt", "r")
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
    if message.content.startswith("*SuleimanSpecial") and message.author.id == userID:
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
        await sentMessage.add_reaction(emoji=SuleimanMoji)
        await sentMessage.add_reaction(emoji=crowdMoji)
    #Suleiman Special!
    if message.content.startswith("*SuperBowlSpecial") and message.author.id == userID:
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
        await sentMessage.add_reaction(emoji=crowdMoji)
        await sentMessage.add_reaction(emoji=SuleimanMoji)
    #Super Bowl Special!
    if message.content.startswith("*resetBracket") and message.author.id == userID:
        logFile = open("Log The CA Discord.txt", "r")
        logFull = logFile.read()
        log = logFull.split("\n")
        logFile.close()
        reepFull = ""
        for matchInfo in log:
            match = matchInfo.split("|")
            if match[1] == "Tie":
                match[1] = match[0]
            reepFull = reepFull + match[1] + ";"
        reepFull = reepFull[:len(reepFull)]
        reepFile = open("reep VThe CA Discord.txt", "w")
        reepFile.write(reepFull)
        reepFile.close()
    #Resets the bracket with the matches in "Log The CA Discord.txt"           
    if message.content.startswith("*peoplePics") and message.author.id == userID:
        peopleFile = open("people.txt", "r")
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
    #Generate a person. 
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
        match = adjectives[0].capitalize()[:1:] + adjectives[0][1::] + person1[0] + " with " + weapons[0] + " vs " + adjectives[1] + person2[0] + " with " + weapons[0] + " " + place + "!"
        matchMessage = await message.channel.send(match)
        emoji1 = getEmoji(person1[0])
        emoji2 = getEmoji(person2[0])
        await matchMessage.add_reaction(emoji1)
        await matchMessage.add_reaction(emoji2)
    #Single match for everyone to use.
    if message.content.startswith("*react"):
        messageArray = message.content.split(" ")
        if len(messageArray) >= 3:
            messageArray.pop(0)
            print("Message ID: " + str(messageArray[0]))
            print("Channel ID: " + str(messageArray[1]))
            channelID = message.guild.get_channel(int(messageArray[1]))
            msg = await channelID.fetch_message(messageArray[0])
            messageArray.pop(0)
            messageArray.pop(0)
            name = ""
            for item in messageArray:
                name = name + item + " "
            name = name.strip()
            emoji = getEmoji(name)
            print("Person: " + name)
            await message.delete()
            await msg.add_reaction(emoji)
    #React with an emoji; uses the syntax `*react [messageID] [channelID] [Emoji Name]`
    if message.content.startswith("*purgeDeathMatch"):
        async for message in message.channel.history(limit=100):
            messageArray = message.content.split(" ")
            commandPossible = messageArray[0]
            commandList = ["*ranked", "*sendLastMatchInfo", "*weapons", "*places", "*newPeopleInfo", "*SuleimanSpecial", "*SuperBowlSpecial", "*resetBracket", "*resetBracket", "*peoplePics", "*lincoln", "*placeMe", "*weaponMe", "*personMe", "*help", "*react"]
            if commandPossible in commandList:
                await message.delete()
        await message.delete()
    #Purges all death match commands.      
    if message.content.startswith("*beginCADiscordMatches") and message.author.id == userID:
        peopleFile = open("peer.txt", "r")
        peopleFull = peopleFile.read()
        people = peopleFull.split("\n")

        CABracketFile = open("CABracket.txt", "r")
        CABracketFull = CABracketFile.read()
        BackUp = open("CABracketBackUp.txt", "w")
        BackUp.write(CABracketFull)
        CABracketFile.close()
        BackUp.close()

        CABracket = []
        for i in range(len(people)):
            if i % 2 == 0 and (people[i] != "A" and people[i] != "B"):
                CABracket.append(people[i])
                print(str(people[i]) + " added.")
        CABracketFile = open("CABracket.txt", "w")
        for person in CABracket:
            CABracketFile.write("\n" + person)
        CABracketFile.close()
        peopleFile.close()
        await message.channel.send("Completed.")
    #Resets the bracket for the CA Discord. 
    if message.content.startswith("*everyInfoEver") and message.author.id == userID:
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

        #peopleFile = open("peer.txt", "r")
        #peopleFull = peopleFile.read()
        #people = peopleFull.split("\n")
        #peopleFile.close()
        #for i in range(len(people)):
            #if i % 2 == 0 and (people[i] != "A" and people[i] != "B"):
                #embed = createPersonEmbed(people[i])
                #await peopleInfo.send(embed=embed)


        weaponTiersFiles = open("weaponTiers.txt", "r")
        adjectiveTiersFull = weaponTiersFiles.read()
        weaponTiers = adjectiveTiersFull.split("\n")
        weaponTiersFiles.close()
        for weaponTier in weaponTiers:
            weaponFile = open(weaponTier + ".txt", "r")
            weaponFull = weaponFile.read()
            weapons = weaponFull.split("\n")
            weaponFile.close()
            for weapon in weapons: 
                embed = createWeaponEmbed(weapon)
                await weaponsInfo.send(embed=embed)

        placesFile = open("places.txt", "r")
        placesFull = placesFile.read()
        places = placesFull.split("\n")
        for place in places:
            embed = createPlaceEmbed(place)
            await placeInfo.send(embed=embed)
    #sends all of the info for all people, weapons, and places. 
    if message.content.startswith("*register") or message.content.startswith("*suggest"):
        peopleFile = open("peer.txt", "r")
        peopleFull = peopleFile.read()
        peopleID = peopleFull.split("\n")
        suggestionFile = open("suggestions.txt", "r")
        suggestions = suggestionFile.read()
        suggestionFile.close()
        suggestionsArray = suggestions.split("\n")
        people = []
        for index in range(len(peopleID)):
            if index % 2 == 0 and (peopleID[index] != "A" and peopleID[index] != "B"):
                people.append(peopleID[index])

        person = message.content[10:len(message.content)]
        print("Person: " + person)
        if person in people:
            await message.channel.send(person + " is already in Historical Death Match! (ID " + peopleID[peopleID.index(person) + 1] + ")")
        else:
            if person in suggestionsArray:
                await message.channel.send(person + " has already been suggested (but not yet added!).")
            else:
                suggestionFile = open("suggestions.txt", "w")
                suggestionFile.write(suggestions)
                suggestionFile.write("\n" + person)
                suggestionFile.close()
                await message.channel.send("Added " + person + " to suggestions.")
        await message.delete()
    #Command to suggest new people!  
    if message.content.startswith("*checkEmoji") and message.author.id == userID:
        for emoji in message.guild.emojis:
            await message.channel.send(emoji.name + "; " + str(emoji.id))
    #Sends all the emojis with ids in the server. Useful for large emoji batches. 
    if (message.content.startswith("*customMatch") or message.content.startswith("*presidentialBracket")) and message.author.id == userID:
        peopleMatch3 = ["George Washington", "John Adams"]

        peopleMatches = [peopleMatch3]

        numberOfMatches = len(peopleMatches)
        matchesVariables = []
        guildID = message.guild.id

        numofMatches = 0

        weaponTierFile = open("Armory\\Tiers\\weaponTiers.txt", "r")
        placesFile = open("Atlas\\places.txt", "r")
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

        lastInfo = open("lastInfo.txt", "w")
        stringsList = [people[0], people[1], people[2], people[3], people[4], people[5], people[6], people[7], people[8], people[9], weapons[0], weapons[1], weapons[2], weapons[3], weapons[4], weapons[5], weapons[6], weapons[7], weapons[8], weapons[9], places[0], places[1], places[2], places[3], places[4], adjectives[0], adjectives[1], adjectives[2], adjectives[3], adjectives[4], adjectives[5], adjectives[6], adjectives[7], adjectives[8], adjectives[9]]
        for i in stringsList:
            lastInfo.write(i + "\n")
        
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
            print("[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker], places[matchNum], placeLinks[matchNum]))
            embed = discord.Embed(title="Match #" + str(numofMatches + matchNum), description="[%s](%s) [%s](%s) with [%s](%s) vs [%s](%s) [%s](%s) with [%s](%s) [%s](%s)!" % (adjectiveFirst, adjectiveLinks[weaponPersonAdjectiveTicker], people[weaponPersonAdjectiveTicker], peopleLinks[weaponPersonAdjectiveTicker], weapons[weaponPersonAdjectiveTicker], weaponLinks[weaponPersonAdjectiveTicker], adjectives[weaponPersonAdjectiveTicker+1], adjectiveLinks[weaponPersonAdjectiveTicker+1], people[weaponPersonAdjectiveTicker+1], peopleLinks[weaponPersonAdjectiveTicker+1], weapons[weaponPersonAdjectiveTicker+1], weaponLinks[weaponPersonAdjectiveTicker], places[matchNum], placeLinks[matchNum]), color=0xFF9900)
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
            await match.add_reaction(emoji=personEmojiList[emojiTicker])
            await match.add_reaction(emoji=personEmojiList[emojiTicker + 1])
            emojiTicker+=2
        print("Completed!")
    #Quick set up for custom matches and brackets- in this case, the presidential bracket. Just throw the people into the code manually and you're good to go!
    if message.content.startswith("*WIT") and message.author.id == userID:
        print("WeaponInfoTesting!")
        adjectiveTiersFile = open("Armory\\Tiers\\weaponTiers.txt", "r")
        adjectiveTiersFull = adjectiveTiersFile.read()
        adjectiveTiersArray = adjectiveTiersFull.split("\n")
        for tier in adjectiveTiersArray:
            print("Tier: " + tier)
            tierFile = open("Armory\\Tiers\\" + tier + ".txt", "r")
            tierFull = tierFile.read()
            tierArray = tierFull.split("\n")
            for weapon in tierArray:
                print(weapon)
                weaponEmbed = createWeaponEmbed(weapon)
                await message.channel.send(embed=weaponEmbed)
    #Sends all the info for each and every weapon.
    if message.content.startswith("*AIT") and message.author.id == userID:
        print("adjectivesInfoTesting!")
        adjectivesQuant = 16
        for numTier in range(adjectivesQuant):
            print("Tier: Tier" + str(numTier+1))
            tierFile = open("Adjectives\\Tier" + str(numTier+1) + ".txt", "r")
            tierFull = tierFile.read()
            tierArray = tierFull.split("\n")
            for adjective in tierArray:
                print(adjective)
                adjectiveEmbed = createAdjectiveEmbed(adjective)
                await message.channel.send(embed=adjectiveEmbed)
    #Sends all the info for each and every adjective.
    if message.content.startswith("*ATLAS") and message.author.id == userID:
        print("Places Info Testing!")
        placeFile = open("Atlas\\placesName.txt", "r")
        placeFull = placeFile.read()
        placeArray = placeFull.split("\n")
        for place in placeArray:
            embed = createPlaceEmbed(place)
            await message.channel.send(embed=embed)
    #Sends all the info for each and every place.
    if message.content.startswith("*info"):
        messageContent = message.content[6::]
        
        peopleFile = open("people.txt", "r")
        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")

        weaponTierFile = open("Armory\\Tiers\\weaponTierList.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split("\n")
        weaponArray = []
        weaponMinusFirstWord = []
        for weaponTier in weaponTierArray:
            weaponFile = open("Armory\\Tiers\\" + weaponTier + ".txt", "r")
            weaponFull = weaponFile.read()
            weaponArrayTemp = weaponFull.split("\n")
            for weapon in weaponArrayTemp:
                weaponArray.append(weapon)
                
        placesFile = open("Atlas\\placesName.txt", "r")
        placesFull = placesFile.read()
        placesArray = placesFull.split("\n")

        adjectiveTierFile = open("Adjectives\\TierList.txt", "r")
        adjectiveTierFull = adjectiveTierFile.read()
        adjectiveTierArray = adjectiveTierFull.split("\n")

        adjectiveArray = []
        for adjectiveTier in adjectiveTierArray:
            adjectiveFile = open("Adjectives\\" + adjectiveTier + ".txt", "r")
            adjectiveFull = adjectiveFile.read()
            adjectiveArrayTemp = adjectiveFull.split("\n")
            for adjective in adjectiveArrayTemp:
                adjectiveArray.append(adjective)
        
        
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
                        await message.channel.send(messageContent + " was not found.")
    #Grab info on a person, weapon, adjective, or place!
    if message.content.startswith("*about"):
        embed = discord.Embed(title="About HDM!", description='"though I would' + "'ve bribed people to get stephen hawking to win that one match" + '"\n-Harrison Truscott\nHistorical Death Match (found here https://github.com/fixmeseb/DeathMatchBot) is a Discord bot that started out when I thought, "Hey, you know what' + "'s funny?" + ' Historical figures fighting each other. I could do something with this!" And then I did. Abbreviated to HDM a lot, HDM is currently running it' + "'s third iteration of the bot (with adjectives!) on the CA Discord Server, and otherwise is soon ready to be added to other server- just reach out to me at the below Discord address or at sauronclaus@gmail.com to see if we can work something out!", color=0xFF9900)
        embed.add_field(name="Lines of Code in Main File", value=1056)
        embed.add_field(name="People", value=372)
        embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
        await message.channel.send(embed=embed)
    #Gives some info about the bot!
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
client.run(testToken)