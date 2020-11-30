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


intents = discord.Intents.all()
client = discord.Client(intents=intents)

discordEmojiList = ["1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer"]
#List of servers with the Discord Emojis. 

tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])


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
    peopleFile = open("CABracket.txt", "r")
    weaponTierFile = open("weaponTiers.txt", "r")
    placesFile = open("places.txt", "r")

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
        weaponArray4 = generateNumRep(len(weaponSet4) - 1, weaponArray4)
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

    guild = client.get_guild(620964009247768586)
    pollChannel = client.get_channel(620964009679650847)
    peopleInfo = client.get_channel(620964009679650847)
    weaponsInfo = client.get_channel(620964009679650847)
    placeInfo = client.get_channel(620964009679650847)

    for channel in guild.text_channels:
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
    match4 = person7 + " with " + weapon7 + " vs " + person8 + " with " + weapon8 + " " + place4 + "!"
    match5 = person9 + " with " + weapon9 + " vs " + person10 + " with " + weapon10 + " " + place5 + "!"


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
    stringsList = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, weapon1, weapon2, weapon3, weapon4, weapon5, weapon6, weapon7, weapon8, weapon9, weapon10, place1, place2, place3, place4, place5]
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


        

client.run(testToken)