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


client = discord.Client()
discordEmojiList = ["1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer"]
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
    article = wikipedia.page(person)
    summary = article.summary.split('\n')
    summaryPersonal = summaryShort(str(summary[0]))
    embed = discord.Embed(title=article.title, description=summaryPersonal, color=0xFF9900)
    print("Emoji Name: " + personEmoji.name)
    print(summary[0])
    personURL = str(personEmoji.url)
    embed.set_image(url=personURL)
    embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/01cb7c2c7f2007d8b060e084ea4eb6fd.png?size=512")
    return embed
#Returns an embed object created from the inputed person.

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("*ranked") and message.author.id == userID:
        peerFile = open("reep VThe CA Discord.txt", "r")
        weaponTierFile = open("weaponTiers.txt", "r")
        placesFile = open("places.txt", "r")
        peerFull = peerFile.read()
        peer = peerFull.split(";")
        peerFile.close()
        peopleList = []
        fileNumber = len(peer) - 1

        while (len(peopleList) < 6):
            peopleList = newGenerateNum(fileNumber, peopleList)
  
        person1 = peer[peopleList[0]]
        person2 = peer[peopleList[1]]
        person3 = peer[peopleList[2]]
        person4 = peer[peopleList[3]]
        person5 = peer[peopleList[4]]
        person6 = peer[peopleList[5]]

        print("People: ")
        print (person1)
        print (person2)
        print (person3)
        print (person4)
        print (person5)
        print (person6)
        people = [person1, person2, person3, person4, person5, person6]
        
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')

        weaponTier1Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier2Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier3Num = random.randint(1, len(weaponTierArray) - 1)

        weaponTier1Name = weaponTierArray[weaponTier1Num] + ".txt"
        weaponTier2Name = weaponTierArray[weaponTier2Num] + ".txt"
        weaponTier3Name = weaponTierArray[weaponTier3Num] + ".txt"

        weaponFile1 = open(weaponTier1Name, "r")
        weaponFile2 = open(weaponTier2Name, "r")
        weaponFile3 = open(weaponTier3Name, "r")

        weaponSet1 = weaponFile1.read().split('\n')
        weaponSet2 = weaponFile2.read().split('\n')
        weaponSet3 = weaponFile3.read().split('\n')

        weaponArray1 = []
        weaponArray2 = []
        weaponArray3 = []


        
        while (len(weaponArray1) < 2):
            weaponArray1 = generateNumRep(len(weaponSet1) - 1, weaponArray1)
        while (len(weaponArray2) < 2):
            weaponArray2 = generateNumRep(len(weaponSet2) - 1, weaponArray2)
        while (len(weaponArray3) < 2):
            weaponArray3 = generateNumRep(len(weaponSet3) - 1, weaponArray3)
            


        weapon1 = weaponSet1[weaponArray1[0]]
        weapon2 = weaponSet1[weaponArray1[1]]
        weapon3 = weaponSet2[weaponArray2[0]]
        weapon4 = weaponSet2[weaponArray2[1]]
        weapon5 = weaponSet3[weaponArray3[0]]
        weapon6 = weaponSet3[weaponArray3[1]]

        
        print("Weapons: ")
        print(weapon1)
        print(weapon2)
        print(weapon3)
        print(weapon4)
        print(weapon5)
        print(weapon6)
        weapons = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6]

        places = placesFile.read().split('\n')
        placeArray = []

        while (len(placeArray) < 3):
            placeArray = generateNumRep(len(places) - 1, placeArray)

        place1Num = placeArray[0]    
        place2Num = placeArray[1]
        place3Num = placeArray[2]

        place1 = places[place1Num]   
        place2 = places[place2Num]       
        place3 = places[place3Num]

        print("Places: ")
        print(place1)      
        print(place2)       
        print(place3)
        places = [place1, place2, place3]

        pollChannel = message.channel
        peopleInfo = message.channel
        placeInfo = message.channel
        weaponsInfo = message.channel

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
        
        print("Poll Channel: #" + pollChannel.name)
        match1 = person1 + " with " + weapon1 + " vs " + person2 + " with " + weapon2 + " " + place1 + "!"
        match2 = person3 + " with " + weapon3 + " vs " + person4 + " with " + weapon4 + " " + place2 + "!"
        match3 = person5 + " with " + weapon5 + " vs " + person6 + " with " + weapon6 + " " + place3 + "!"
        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)
        await pollChannel.send("<@&613144506757283974>")
        
        personIDList = []
        for i in people:
            personID = findEmojiID(i)
            personIDList.append(personID)

        person1ID = personIDList[0]
        person2ID = personIDList[1]
        person3ID = personIDList[2]
        person4ID = personIDList[3]
        person5ID = personIDList[4]
        person6ID = personIDList[5]
        

        person1Emoji = checkForEmoji(person1ID)
        person2Emoji = checkForEmoji(person2ID)
        person3Emoji = checkForEmoji(person3ID)
        person4Emoji = checkForEmoji(person4ID)
        person5Emoji = checkForEmoji(person5ID)
        person6Emoji = checkForEmoji(person6ID)

        lastInfo = open("lastInfo.txt", "w")
        stringsList = [person1, person2, person3, person4, person5, person6, weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, place1, place2, place3]
        for i in stringsList:
            lastInfo.write(i + "\n")
        
        peer.remove(person1)
        peer.remove(person2)
        peer.remove(person3)
        peer.remove(person4)
        peer.remove(person5)
        peer.remove(person6)

        peerFile.close()
        peerFile = open("reep VThe CA Discord.txt", "w")
        peerString = ""
        for name in peer:
            peerString = peerString + name + ";"
        stringPeer = peerString[:len(peerString)-1]
        peerFile.write(stringPeer)
        peerFile.close()


        await match1ID.add_reaction(emoji=person1Emoji)
        await match1ID.add_reaction(emoji=person2Emoji)
        await match2ID.add_reaction(emoji=person3Emoji)
        await match2ID.add_reaction(emoji=person4Emoji)
        await match3ID.add_reaction(emoji=person5Emoji) 
        await match3ID.add_reaction(emoji=person6Emoji)

        for person in people:
            embed = createPersonEmbed(person)
            await peopleInfo.send(embed=embed)
        for weapon in weapons:
            embed = createWeaponEmbed(weapon)
            await weaponsInfo.send(embed=embed)
        for place in places:
            embed = createPlaceEmbed(place)
            await placeInfo.send(embed=embed)
    #Ranked matches for the CA Discord. 
    if message.content.startswith("*sendLastMatchInfo") and message.author.id == userID:
        infoWrite = open("lastInfo.txt", "r")
        infoFull = infoWrite.read()
        info = infoFull.split("\n")

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
        embed = createWeaponEmbed(info[6])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[7])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[8])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[9])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[10])
        await weaponsInfo.send(embed=embed)
        embed = createWeaponEmbed(info[11])
        await weaponsInfo.send(embed=embed)
        embed = createPlaceEmbed(info[12])
        await placeInfo.send(embed=embed)
        embed = createPlaceEmbed(info[13])
        await placeInfo.send(embed=embed)
        embed = createPlaceEmbed(info[14])
        await placeInfo.send(embed=embed)
    #Send the info in the file "lastInfo.txt"
    if message.content.startswith("*weapons") and message.author.id == userID:
        weaponTierFile = open("itemsAndLinks.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')
        for channel in message.guild.text_channels:
            if channel.name == "historical-weapons-info":
                print("found #" + channel.name)
                weaponsInfo = channel
        for weaponFileName in weaponTierArray:
            weaponFile = open(weaponFileName + ".txt", "r")
            weaponSet = weaponFile.read().split('\n')
            for v in range(len(weaponSet)):
                if v % 2 == 0:
                    embed = createWeaponEmbed(weaponSet[v])
                    await weaponsInfo.send(embed=embed)
    #Send the info on all weapons. 
    if message.content.startswith("*places") and message.author.id == userID:
        weaponTierFile = open("places.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')
        weaponsInfo = message.channel
        for channel in message.guild.text_channels:
            if channel.name == "historical-places-info":
                print("found #" + channel.name)
                weaponsInfo = channel
        for v in range(len(weaponTierArray)):
            if v % 2 == 0:
                embed = createPlaceEmbed(weaponTierArray[v])
                await weaponsInfo.send(embed=embed)
    #Send the info on all places. 
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
    if message.content.startswith("*lincoln"):
        person = "Abraham Lincoln"
        jpg = "Pictures\\" + person + ".jpg"
        png = person + ".png"
        if os.path.exists(jpg):
            await message.channel.send(file=discord.File(jpg))
        else:
            await message.channel.send("Not found. '" + str(jpg) + "'.")
    #Get a picture of Abraham Lincoln. Not sure why you want this, but it's good to have options.
    if message.content.startswith("*placeMe"):
        place = generatePlace()
        await message.channel.send(place.strip() + "!")
    #Generate a place.
    if message.content.startswith("*weaponMe"):
        weapon = generateWeapon()
        await message.channel.send(weapon.strip() + "!")
    #Generate a weapon. 
    if message.content.startswith("*personMe"):
        person = generatePerson()
        await message.channel.send(person[0] + "!")
    #Generate a person. 
    if message.content.startswith("*help"):
        me = message.guild.get_member(557273350414794772)
        color = me.color
        embed = discord.Embed(title="Help", description="", color=color)
        embed.add_field(name="*newPeopleInfo", value="Get the scoop on the newest additions to Death Match Bot!", inline=False)
        embed.add_field(name="*lincoln", value="Get a photo of the 16th president of the USA. There's only one photo for him though.", inline=False)
        embed.add_field(name="*placeMe", value="Get a random place!", inline=False)
        embed.add_field(name="*weaponMe", value="Get a random weapon!", inline=False)
        embed.add_field(name="*personMe", value="Get a random person!", inline=False) 
        embed.add_field(name="*match", value="Created your very own death match, with two combatants, each armed, and a location!", inline=False)
        embed.add_field(name="*react", value="React with people emojis! The syntax is '*react MESSAGEID CHANNELID EMOJIFIRSTNAME EMOJILASTNAME`.", inline=False)
        embed.add_field(name="*purgeDeathMatch", value="Purge Death Match: Clear all commands used by Death Match bot in this channel!", inline=False)
        embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/01cb7c2c7f2007d8b060e084ea4eb6fd.png?size=512")
        await message.channel.send(embed=embed)
    #The help command
    if message.content.startswith("*match"):
        person1 = generatePerson()
        person2 = generatePerson()
        weapon1 = generateWeapon()
        weapon2 = generateWeapon()
        place = generatePlace()
        match = person1[0] + " with " + weapon1 + " vs " + person2[0] + " with " + weapon2 + " " + place
        matchID = await message.channel.send(match)
        await matchID.add_reaction(emoji=person1[1])
        await matchID.add_reaction(emoji=person2[1])
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

client.run(botToken)