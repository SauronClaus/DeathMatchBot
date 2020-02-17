tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])

import discord
import asyncio
import random
import wikipedia

from embeds import createPlaceEmbed
from embeds import summaryShort
from embeds import checkLinks
from embeds import createWeaponEmbed
from generateNumbers import generateNumRep
from generateNumbers import newGenerateNum

discordEmojiList = ["1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer"]

client = discord.Client()
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
async def my_background_task():
    await client.wait_until_ready()
    print("ready!")
    counter = 0
    channel = client.get_channel(620964009679650847)
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

    channelList = [624231124154974225, 624230957284851713, 624231093758984193, 624231027845627914]
    #CA Discord channel ID list
    pollChannel = client.get_channel(channelList[0])
    peopleInfo = client.get_channel(channelList[1])
    placeInfo = client.get_channel(channelList[2])
    weaponsInfo = client.get_channel(channelList[3])
        
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
async def my_background_taskTest():
    await client.wait_until_ready()
    print("ready!")
    counter = 0
    channel = client.get_channel(620964009679650847)
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

    channelList = [620964009679650847, 644530970741047306, 665200620818661376, 665200586400202752]
    #Test Server channel ID list
    pollChannel = client.get_channel(channelList[0])
    peopleInfo = client.get_channel(channelList[1])
    placeInfo = client.get_channel(channelList[2])
    weaponsInfo = client.get_channel(channelList[3])
        
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

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    mode = input("What mode? (test/ranked)")
    if mode == "test":
        client.loop.create_task(my_background_taskTest())
    if mode == "ranked":
        client.loop.create_task(my_background_task())

client.run(botToken)