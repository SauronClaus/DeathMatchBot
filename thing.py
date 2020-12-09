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
    print("Test: \"" + person + "\"")
    article = wikipedia.page(person, auto_suggest=False)
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
    numberOfLincolnPics = 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("*ranked") and message.author.id == userID:
        peopleFile = open("CABracket.txt", "r")
        weaponTierFile = open("weaponTiers.txt", "r")
        placesFile = open("places.txt", "r")
        adjectiveTierFile = open("Adjectives\\adjectiveTiers.txt")

        peopleFull = peopleFile.read()
        people = peopleFull.split("\n")
        peopleFile.close()
        peopleList = []
        fileNumber = len(people) - 1

        while (len(peopleList) < 10):
            peopleList = newGenerateNum(fileNumber, peopleList)
  
        person1 = people[peopleList[0]]
        person2 = people[peopleList[1]]
        person3 = people[peopleList[2]]
        person4 = people[peopleList[3]]
        person5 = people[peopleList[4]]
        person6 = people[peopleList[5]]
        person7 = people[peopleList[6]]
        person8 = people[peopleList[7]]
        person9 = people[peopleList[8]]
        person10 = people[peopleList[9]]


        print("People: ")
        print (person1)
        print (person2)
        print (person3)
        print (person4)
        print (person5)
        print (person6)
        print (person7)
        print (person8)
        print (person9)
        print (person10)

        peopleCurrent = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10]
        
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')

        weaponTier1Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier2Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier3Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier4Num = random.randint(1, len(weaponTierArray) - 1)
        weaponTier5Num = random.randint(1, len(weaponTierArray) - 1)


        weaponTier1Name = weaponTierArray[weaponTier1Num] + ".txt"
        weaponTier2Name = weaponTierArray[weaponTier2Num] + ".txt"
        weaponTier3Name = weaponTierArray[weaponTier3Num] + ".txt"
        weaponTier4Name = weaponTierArray[weaponTier4Num] + ".txt"
        weaponTier5Name = weaponTierArray[weaponTier5Num] + ".txt"


        weaponFile1 = open(weaponTier1Name, "r")
        weaponFile2 = open(weaponTier2Name, "r")
        weaponFile3 = open(weaponTier3Name, "r")
        weaponFile4 = open(weaponTier4Name, "r")
        weaponFile5 = open(weaponTier5Name, "r")


        weaponSet1 = weaponFile1.read().split('\n')
        weaponSet2 = weaponFile2.read().split('\n')
        weaponSet3 = weaponFile3.read().split('\n')
        weaponSet4 = weaponFile4.read().split('\n')
        weaponSet5 = weaponFile5.read().split('\n')


        weaponArray1 = []
        weaponArray2 = []
        weaponArray3 = []
        weaponArray4 = []
        weaponArray5 = []



        
        while (len(weaponArray1) < 2):
            weaponArray1 = generateNumRep(len(weaponSet1) - 1, weaponArray1)
        while (len(weaponArray2) < 2):
            weaponArray2 = generateNumRep(len(weaponSet2) - 1, weaponArray2)
        while (len(weaponArray3) < 2):
            weaponArray3 = generateNumRep(len(weaponSet3) - 1, weaponArray3)
        while (len(weaponArray4) < 2):
            weaponArray4= generateNumRep(len(weaponSet4) - 1, weaponArray4)
        while (len(weaponArray5) < 2):
            weaponArray5 = generateNumRep(len(weaponSet5) - 1, weaponArray5)
            


        weapon1 = weaponSet1[weaponArray1[0]]
        weapon2 = weaponSet1[weaponArray1[1]]
        weapon3 = weaponSet2[weaponArray2[0]]
        weapon4 = weaponSet2[weaponArray2[1]]
        weapon5 = weaponSet3[weaponArray3[0]]
        weapon6 = weaponSet3[weaponArray3[1]]
        weapon7 = weaponSet4[weaponArray4[0]]
        weapon8 = weaponSet4[weaponArray4[1]]
        weapon9 = weaponSet5[weaponArray5[0]]
        weapon10 = weaponSet5[weaponArray5[1]]


        
        print("Weapons: ")
        print(weapon1)
        print(weapon2)
        print(weapon3)
        print(weapon4)
        print(weapon5)
        print(weapon6)
        print(weapon7)
        print(weapon8)
        print(weapon9)
        print(weapon10)

        weapons = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10]

        places = placesFile.read().split('\n')
        placeArray = []

        while (len(placeArray) < 5):
            placeArray = generateNumRep(len(places) - 1, placeArray)

        place1Num = placeArray[0]    
        place2Num = placeArray[1]
        place3Num = placeArray[2]
        place4Num = placeArray[3]
        place5Num = placeArray[4]


        place1 = places[place1Num]   
        place2 = places[place2Num]       
        place3 = places[place3Num]
        place4 = places[place4Num]
        place5 = places[place5Num]


        print("Places: ")
        print(place1)      
        print(place2)       
        print(place3)
        print(place4)
        print(place5)

        places = [place1, place2, place3, place4, place5]

        adjectiveTiersFull = adjectiveTierFile.read()
        adjectiveTierArray = adjectiveTiersFull.split('\n')

        adjectiveTier1Num = random.randint(1, len(adjectiveTierArray) - 1)
        adjectiveTier2Num = random.randint(1, len(adjectiveTierArray) - 1)
        adjectiveTier3Num = random.randint(1, len(adjectiveTierArray) - 1)
        adjectiveTier4Num = random.randint(1, len(adjectiveTierArray) - 1)
        adjectiveTier5Num = random.randint(1, len(adjectiveTierArray) - 1)


        adjectiveTier1Name = adjectiveTierArray[adjectiveTier1Num] + ".txt"
        adjectiveTier2Name = adjectiveTierArray[adjectiveTier2Num] + ".txt"
        adjectiveTier3Name = adjectiveTierArray[adjectiveTier3Num] + ".txt"
        adjectiveTier4Name = adjectiveTierArray[adjectiveTier4Num] + ".txt"
        adjectiveTier5Name = adjectiveTierArray[adjectiveTier5Num] + ".txt"


        adjectiveFile1 = open("Adjectives\\" + adjectiveTier1Name, "r")
        adjectiveFile2 = open("Adjectives\\" + adjectiveTier2Name, "r")
        adjectiveFile3 = open("Adjectives\\" + adjectiveTier3Name, "r")
        adjectiveFile4 = open("Adjectives\\" + adjectiveTier4Name, "r")
        adjectiveFile5 = open("Adjectives\\" + adjectiveTier5Name, "r")


        adjectiveSet1 = adjectiveFile1.read().split('\n')
        adjectiveSet2 = adjectiveFile2.read().split('\n')
        adjectiveSet3 = adjectiveFile3.read().split('\n')
        adjectiveSet4 = adjectiveFile4.read().split('\n')
        adjectiveSet5 = adjectiveFile5.read().split('\n')


        adjectiveArray1 = []
        adjectiveArray2 = []
        adjectiveArray3 = []
        adjectiveArray4 = []
        adjectiveArray5 = []



        
        while (len(adjectiveArray1) < 2):
            adjectiveArray1 = generateNumRep(len(adjectiveSet1) - 1, adjectiveArray1)
        while (len(adjectiveArray2) < 2):
            adjectiveArray2 = generateNumRep(len(adjectiveSet2) - 1, adjectiveArray2)
        while (len(adjectiveArray3) < 2):
            adjectiveArray3 = generateNumRep(len(adjectiveSet3) - 1, adjectiveArray3)
        while (len(adjectiveArray4) < 2):
            adjectiveArray4 = generateNumRep(len(adjectiveSet4) - 1, adjectiveArray4)
        while (len(adjectiveArray5) < 2):
            adjectiveArray5 = generateNumRep(len(adjectiveSet5) - 1, adjectiveArray5)
            


        adjective1 = adjectiveSet1[adjectiveArray1[0]]
        adjective2 = adjectiveSet1[adjectiveArray1[1]]
        adjective3 = adjectiveSet2[adjectiveArray2[0]]
        adjective4 = adjectiveSet2[adjectiveArray2[1]]
        adjective5 = adjectiveSet3[adjectiveArray3[0]]
        adjective6 = adjectiveSet3[adjectiveArray3[1]]
        adjective7 = adjectiveSet4[adjectiveArray4[0]]
        adjective8 = adjectiveSet4[adjectiveArray4[1]]
        adjective9 = adjectiveSet5[adjectiveArray5[0]]
        adjective10= adjectiveSet5[adjectiveArray5[1]]


        
        print("Adjectives: ")
        print(adjective1)
        print(adjective2)
        print(adjective3)
        print(adjective4)
        print(adjective5)
        print(adjective6)
        print(adjective7)
        print(adjective8)
        print(adjective9)
        print(adjective10)

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
        match1 = adjective1.capitalize() + " " + person1 + " with " + weapon1 + " vs " + adjective2.capitalize() + " " + person2 + " with " + weapon2 + " " + place1 + "!"
        match2 = adjective3.capitalize() + " " + person3 + " with " + weapon3 + " vs " + adjective4.capitalize() + " " + person4 + " with " + weapon4 + " " + place2 + "!"
        match3 = adjective5.capitalize() + " " + person5 + " with " + weapon5 + " vs " + adjective6.capitalize() + " " + person6 + " with " + weapon6 + " " + place3 + "!"
        match4 = adjective7.capitalize() + " " + person7 + " with " + weapon7 + " vs " + adjective8.capitalize() + " " + person8 + " with " + weapon8 + " " + place4 + "!"
        match5 = adjective9.capitalize() + " " + person9 + " with " + weapon9 + " vs " + adjective10.capitalize() + " " + person10 + " with " + weapon10 + " " + place5 + "!"

        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)
        match4ID = await pollChannel.send(match4)
        match5ID = await pollChannel.send(match5)

        await pollChannel.send("<@&613144506757283974>")
        
        personIDList = []
        for i in peopleCurrent:
            personID = findEmojiID(i)
            personIDList.append(personID)

        person1ID = personIDList[0]
        person2ID = personIDList[1]
        person3ID = personIDList[2]
        person4ID = personIDList[3]
        person5ID = personIDList[4]
        person6ID = personIDList[5]
        person7ID = personIDList[6]
        person8ID = personIDList[7]
        person9ID = personIDList[8]
        person10ID = personIDList[9]

        

        person1Emoji = checkForEmoji(person1ID)
        person2Emoji = checkForEmoji(person2ID)
        person3Emoji = checkForEmoji(person3ID)
        person4Emoji = checkForEmoji(person4ID)
        person5Emoji = checkForEmoji(person5ID)
        person6Emoji = checkForEmoji(person6ID)
        person7Emoji = checkForEmoji(person7ID)
        person8Emoji = checkForEmoji(person8ID)
        person9Emoji = checkForEmoji(person9ID)
        person10Emoji = checkForEmoji(person10ID)


        lastInfo = open("lastInfo.txt", "w")
        stringsList = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10, place1, place2, place3, place4, place5, adjective1, adjective2, adjective3, adjective4, adjective5, adjective6, adjective7, adjective8, adjective9, adjective10]
        for i in stringsList:
            lastInfo.write(i + "\n")
        
        people.remove(person1)
        people.remove(person2)
        people.remove(person3)
        people.remove(person4)
        people.remove(person5)
        people.remove(person6)
        people.remove(person7)
        people.remove(person8)
        people.remove(person9)
        people.remove(person10)


        peopleFile.close()
        peopleFile = open("CABracket.txt", "w")
        peerString = ""
        for name in people:
            peerString = peerString + "\n" + name
        stringPeer = peerString[1:len(peerString)]
        print("Peer String: " + stringPeer)
        peopleFile.write(stringPeer)
        peopleFile.close()


        await match1ID.add_reaction(emoji=person1Emoji)
        await match1ID.add_reaction(emoji=person2Emoji)
        await match2ID.add_reaction(emoji=person3Emoji)
        await match2ID.add_reaction(emoji=person4Emoji)
        await match3ID.add_reaction(emoji=person5Emoji) 
        await match3ID.add_reaction(emoji=person6Emoji)
        await match4ID.add_reaction(emoji=person7Emoji)
        await match4ID.add_reaction(emoji=person8Emoji)
        await match5ID.add_reaction(emoji=person9Emoji)
        await match5ID.add_reaction(emoji=person10Emoji)


        for person in peopleCurrent:
            embed = createPersonEmbed(person)
            await peopleInfo.send(embed=embed)
        #for weapon in weapons:
            #embed = createWeaponEmbed(weapon)
            #await weaponsInfo.send(embed=embed)
        #for place in places:
            #embed = createPlaceEmbed(place)
            #await placeInfo.send(embed=embed)
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
        #embed = createWeaponEmbed(info[6])
        #await weaponsInfo.send(embed=embed)
        #embed = createWeaponEmbed(info[7])
        #await weaponsInfo.send(embed=embed)
        #embed = createWeaponEmbed(info[8])
        #await weaponsInfo.send(embed=embed)
        #embed = createWeaponEmbed(info[9])
        #await weaponsInfo.send(embed=embed)
        #embed = createWeaponEmbed(info[10])
        #await weaponsInfo.send(embed=embed)
        #embed = createWeaponEmbed(info[11])
        #await weaponsInfo.send(embed=embed)
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
        embed = discord.Embed(title="Help", description="", color=color)
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
        embed.add_field(name="*register", value="Suggest new people for the bot!", inline=False)
        embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/5861378fa49209b3929119cc0b49eee8.png?size=128")
        await message.channel.send(embed=embed)
    #The help command
    if message.content.startswith("*match"):
        person1 = generatePerson()
        person2 = generatePerson()
        weapons = generateWeaponPair()
        adjectives = generateAdjectivePair()

        place = generatePlace()
        match = adjectives[0].capitalize() + " " + person1[0] + " with " + weapons[0] + " vs " + adjectives[1].capitalize() + " " + person2[0] + " with " + weapons[0] + " " + place + "!"
        matchID = await message.channel.send(match)
        emoji1 = getEmoji(person1[0])
        emoji2 = getEmoji(person2[0])
        await matchID.add_reaction(emoji1)
        await matchID.add_reaction(emoji2)
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
        weaponTiersFull = weaponTiersFiles.read()
        weaponTiers = weaponTiersFull.split("\n")
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
    if message.content.startswith("*register"):
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
    if (message.content.startswith("*presidentialBracket") or message.content.startswith("*customMatch")) and message.author.id == userID:
        peopleMatch1 = ["John Quincy Adams", "Herbert Hoover"]
        peopleMatch2 = ["Grover Cleveland", "John Tyler"]
        peopleMatch3 = ["Henry Ford", "Millard Fillmore"]

        print("People:")
        print(peopleMatch1[0])
        print(peopleMatch1[1])
        print(peopleMatch2[0])
        print(peopleMatch2[1])
        print(peopleMatch3[0])
        print(peopleMatch3[1])

        peopleCurrent = [peopleMatch1[0], peopleMatch1[1], peopleMatch2[0], peopleMatch2[1], peopleMatch3[0], peopleMatch3[1]]
        
        weaponsMatch1 = generateWeaponPair()
        weaponsMatch2 = generateWeaponPair()
        weaponsMatch3 = generateWeaponPair()

        print("Weapons:")
        print(weaponsMatch1[0])
        print(weaponsMatch1[1])
        print(weaponsMatch2[0])
        print(weaponsMatch2[1])
        print(weaponsMatch3[0])
        print(weaponsMatch3[1])

        adjectivesMatch1 = generateAdjectivePair()
        adjectivesMatch2 = generateAdjectivePair()
        adjectivesMatch3 = generateAdjectivePair()

        print("Adjectives:")
        print(adjectivesMatch1[0])
        print(adjectivesMatch1[1])
        print(adjectivesMatch2[0])
        print(adjectivesMatch2[1])
        print(adjectivesMatch3[0])
        print(adjectivesMatch3[1])

        placeMatch1 = generatePlace()
        placeMatch2 = generatePlace()
        placeMatch3 = generatePlace()

        print("Places:")
        print(placeMatch1)
        print(placeMatch2)
        print(placeMatch3)

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
        match1 = adjectivesMatch1[0].capitalize() + " " + peopleMatch1[0] + " with " + weaponsMatch1[0] + " vs " + adjectivesMatch1[1].capitalize() + " " + peopleMatch1[1] + " with " + weaponsMatch1[1] + " " + placeMatch1 + "!"
        match2 = adjectivesMatch2[0].capitalize() + " " + peopleMatch2[0] + " with " + weaponsMatch2[0] + " vs " + adjectivesMatch2[1].capitalize() + " " + peopleMatch2[1] + " with " + weaponsMatch2[1] + " " + placeMatch2 + "!"
        match3 = adjectivesMatch3[0].capitalize() + " " + peopleMatch3[0] + " with " + weaponsMatch3[0] + " vs " + adjectivesMatch3[1].capitalize() + " " + peopleMatch3[1] + " with " + weaponsMatch3[1] + " " + placeMatch3 + "!"
        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)

        if message.channel.guild.id == 620758472451162142:
            await pollChannel.send("<@&783468826997555261>")
        else:
            if message.channel.guild.id == 620964009247768586:
                await pollChannel.send("Notified!")

        personIDList = []
        for i in peopleCurrent:
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
        stringsList = [peopleMatch1[0], peopleMatch1[1], peopleMatch2[0], peopleMatch2[1], peopleMatch3[0], peopleMatch3[1], weaponsMatch1[0], weaponsMatch1[1], weaponsMatch2[0], weaponsMatch2[1], weaponsMatch3[0], weaponsMatch3[1], placeMatch1, placeMatch2, placeMatch3, adjectivesMatch1[0], adjectivesMatch1[1], adjectivesMatch2[0], adjectivesMatch2[1], adjectivesMatch3[0], adjectivesMatch3[1]]
        for i in stringsList:
            lastInfo.write(i + "\n")

        await match1ID.add_reaction(emoji=person1Emoji)
        await match1ID.add_reaction(emoji=person2Emoji)
        await match2ID.add_reaction(emoji=person3Emoji)
        await match2ID.add_reaction(emoji=person4Emoji)
        await match3ID.add_reaction(emoji=person5Emoji) 
        await match3ID.add_reaction(emoji=person6Emoji)

        for person in peopleCurrent:
            embed = createPersonEmbed(person)
            await peopleInfo.send(embed=embed)
    #Quick set up for custom matches and brackets- in this case, the presidential bracket. Just throw the people into the code manually and you're good to go!

client.run(botToken)