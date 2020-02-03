import discord
from discord.utils import get
import random
import wikipedia

client = discord.Client()
discordEmojiList = ["1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer"]

def generateNum(fileNumber, peopleList):
    #print("Generating things: " + "fileNumber = " + str(fileNumber))
    rando = random.randint(1, fileNumber)
    #print("Rando = " + str(rando))
    #print("Length: " + str(len(peopleList)))
    if rando in peopleList or rando % 2 == 0:
       print("Generation Failed: " + str(rando) + " already in list or even.")
       return peopleList
    else:
        #print (str(rando) + " added to list!")
        peopleList.append(rando)
        return peopleList
def newGenerateNum(fileNumber, peopleList):
    rando = random.randint(1, fileNumber)
    if rando in peopleList:
        print("Generation Failed: " + str(rando) + " already in list")
        for i in peopleList:
           print("List: " + str(i))
        return peopleList
    else:
        #print (str(rando) + " added to list!")
        peopleList.append(rando)
        return peopleList
def generateNumRep(fileNumber, peopleList):
    #print("Generating things: " + "fileNumber = " + str(fileNumber))
    rando = random.randint(1, fileNumber)
    #print("Rando = " + str(rando))
    #print("Length: " + str(len(peopleList)))
    if rando % 2 != 0:
       #print("Generation Failed: " + str(rando) + " odd.")
       return peopleList
    else:
        #print (str(rando) + " added to list!")
        peopleList.append(rando)
        return peopleList
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
def checkLinks(personName):
    
    largeDictionary = {
        "Drake": "Drake (musician)",
        "Elon Musk": "Elon Musk",
        "Archduke Franz Ferdinand": "Archduke Franz Ferdinand of Austria",
        "Attila the Hun": "Atilla",
        "August Ferdinand Mobius": "August Ferdinand Möbius",
        "Augustus Caeser": "Augustus",
        "Brutus": "Brutus the Younger",
        "Carl Gauss": "Carl Friedrich Gauss",
        "Charles Cornwallis": "Charles Cornwallis, 1st Marquess Cornwallis",
        "Charles V of Austria": "Charles V, Holy Roman Emperor",
        "Charles X of Sweden": "Charles X Gustav of Sweden",
        "Chris Evans": "Chris Evans (actor)",
        "Dwight Eisenhower": "Dwight D. Eisenhower",
        "Erwin Schrodinger": "Erwin Schrödinger",
        "Fluffy (Gabriel Iglesias)": "Gabriel Iglesias",
        "Hanibal (general)": "Hanibal",
        "Henri Poincare": "Henri Poincaré",
        "Homer (The Odyssey)": "Homer",
        "Bon Jovi": "Jon Bon Jovi",
        "James Garfield": "James A. Garfield",
        "John Rockefeller": "John D. Rockefeller",
        "King Tutankhamun": "Tutankhamun",
        "Kaiser_Wilhelm": "Wilhelm II, German Emperor",
        "Napoleon Bonaparte": "Napoleon",
        "Montezuma": "Moctezuma I",
        "Sir Francis Drake": "Francis Drake",
        "Prince Charles": "Charles, Prince of Wales",
        "Sir Walter Raleigh": "Walter Raleigh",
        "Richard the Lionheart": "Richard I of England",
        "Sir Robert Wadlow": "Robert Wadlow",
        "Rene Descartes": "René Descartes",
        "Stefan Karl Stefansson": "Stefán Karl Stefánsson",
        "Evariste Galois": "Évariste Galois",
        "Tom Holland": "Tom Holland (actor)",
        "inside a moving train": "Train",
        "a yardstick": "Meterstick",
        "Iron Man's right glove": "Iron Man",
        "5x shurikens": "Shuriken",
        "disco ball and chain": "Ball and Chain",
        "a baby": "Infant",
        "the Master Sword": "Universe of The Legend of Zelda",
        "Darth Maul's Dual Saber": "Lightsaber",
        "Aquaman's Trident": "Arthur Curry",
        "a Halo Energy Sword": "Halo (franchise)",
        "a Needler": "Halo (franchise)",
        "a M6 Spartan Laser": "Halo (franchise)",
        "in Valhalla (from Halo)": "Halo (franchise)",
        "Sunraiser": "The Stormlight Archive",
        "Cthulhu's left thumb (currently attached to the wielder in place of the wielder's left thumb)": "Cthulhu",
        "Cthulhu's left thumb (severed)": "Cthulhu",
        "Frostmourne": "Arthas Menethil",
        "Stormbreaker": "Avengers: Infinity War",
        "a Phaser (Star Trek)": "Weapons in Star Trek",
        "a Nerf Gun but all projectiles from the nerf gun are set on fire upon leaving the barrel of the nerf gun": "Tech Target",
        "R.Y.N.O.": "Ratchet & Clank",
        "Widowmaker's Sniper Rifle": "List of Overwatch Characters",
        "Mei's freeze gun": "List of Overwatch Characters",
        'a thermal detonator': "List of Star Wars Weapons",
        "a DT-29 heavy blaster pistol": "List of Star Wars Weapons",
        "a TL-50 heavy repeater": "List of Star Wars Weapons",
        "in The Death Star Main Hanger Bay": "Death Star",
        "in The Death Star Throne Room": "Death Star",
        "a pair of WESTAR-34 blasters": "Boba Fett",
        "Mac’s shotgun with axe from Agents of SHIELD": "Combination weapons",
        "Ronan's Hammer (no power stone)": "Ronan the Accuser",
        "in The Senate Chamber (Star Wars)": "Galatic Republic",
        "in The Geonosis Arena": "List of Star Wars planets and moons",
        "on Mustafar (site of Obi-Wan Kenobi and Anakin Skywalker's Duel)": "List of Star Wars planets and moons",
        "in The Senate Chamber (Real World)": "United States Capitol",
        "in The Sanctum Sanctorum": "Sanctum Sanctorum",
        "in the USS Enterprise": "USS Enterprise (NCC-1701)",
        "in an arcade": "Amusement arcade",
        "in New York City (Marvel Universe)": "New York City",
        "in an airplane": "Airplane",
        "on an airplane": "Airplane", 
        "in the Voice auditorium": "The Voice (American TV series)",
        "in an IKEA food court": "IKEA",
        "above the Sarlacc Pit on Jabba's sail barges": "List of Star Wars air, aquatic, and ground vehicles",
        "in Defy Gravity's trampoline pit": "CircusTrix",
        "in the Dueling Area of Wakanda": "Wakanda",
        "in a giant 53,820 mile^2 field": "Meadow",
        "San's Gaster Blaster": "Undertale",
        "a morningstar": "Morning star (weapon)",
        "a warhammer": "War hammer",
        "Steve's Diamond Sword": "Minecraft",
        "Freddy Kruger's Glove": "Freddy Krueger",
        "their bear hands (replacing original hands)": "Bears",
        "Spider-Man's Right Webshooter": "Spider-Man",
        "a candlestick": "Candlestick",
        "an oversized Whac-A-Mole mallet": "Whac-A-Mole",
        "a mace": "Mace (weapon)", 
        "an immovable rod": "Magic item (Dungeons & Dragons)", 
        "a disco ball and chain": "Ball and chain",
        "a crusader's shield": "Crusades",
        "Mark Ruffalo": "Mark Alan Ruffalo",
        "their bare hands (duplicated)": "Hand",
        "Brandon Uri's guitar": "Guitar",
        "a Fortnite Pickaxe": "Fornite",
        "a pike (fish)": "Northern Pike",
        "a Delorean's Car Door": "DeLorean Motor Company",
        "Napoleon Bonaparte's Petrified Body": "Napoleon",
        "a large non-personal Laser Cutter": "Laser cutting",
        "a handheld telescope": "Telescope",
        "a dead raven": "Raven",
        'the book "Give Me Liberty" by Eric Forner': "Eric Foner",
        "a very large rock": "Rock (geology)",
        "a shrunken Costco": "Costco",
        "Elon Musk": "Elon Reeve Musk",
        "a pair of nunchucks": "Nunchaku",
        "the toy knife from Undertale": "knife",
        "Sun Tzu": "Sun Wu",
        "John Cena": "John Felix Anthony Cena",
    }
    correct = personName
    if personName in largeDictionary:
        correct = largeDictionary[personName]
    print("Correct: " + correct)
    return correct
def createPersonEmbed(person):
    print(person)
    person = checkLinks(person)
    print("Person: " + person)
    article = wikipedia.page(person)
    #for i in article.images:
        #await peopleInfo.send(str(i))
    summary = article.summary.split('\n')
    print(summary[0])
    summaryPersonal = summaryShort(str(summary[0]))
    embed = discord.Embed(title=article.title, description=summaryPersonal, color=0xFF9900)
    if len(article.images) > 0:
        embed.set_image(url=article.images[0])
    embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/01cb7c2c7f2007d8b060e084ea4eb6fd.png?size=512")
    return embed
def createWeaponEmbed(weapon):
    print(weapon)
    weapon = checkLinks(weapon)
    article = wikipedia.page(weapon)
    #for i in article.images:
        #await weaponInfo.send(str(i))
    summary = article.summary.split('\n')
    summaryPersonal = summaryShort(str(summary[0]))
    embed = discord.Embed(title=article.title, description=summaryPersonal, color=0xFF9900)
    if len(article.images) > 0:
        embed.set_image(url=article.images[0])
    embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/01cb7c2c7f2007d8b060e084ea4eb6fd.png?size=512")
    return embed
def createPlaceEmbed(place):
    print(place)
    place = checkLinks(place)
    article = wikipedia.page(place)
    #for i in article.images:
        #await placeInfo.send(str(i))
    summary = article.summary.split('\n')
    summaryOne = summary[0]
    summaryPersonal = summaryShort(summaryOne)
    embed = discord.Embed(title=article.title, description=summaryPersonal, color=0xFF9900)
    if len(article.images) > 0:
        embed.set_image(url=article.images[0])
    embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://cdn.discordapp.com/avatars/366709133195476992/01cb7c2c7f2007d8b060e084ea4eb6fd.png?size=512")
    return embed
def summaryShort(summary):
    summaryPersonal = ""
    if len(list(summary)) > 2040:
        summaryPersonal = str(summary[0:2000]) + "..."
    else:
        summaryPersonal = summary
    return summaryPersonal
@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("*match") and message.author.id == 366709133195476992:
        peerFile = open("peer.txt", "r")
        weaponTierFile = open("itemsAndLinks.txt", "r")
        placesFile = open("randomListPlaces.txt", "r")
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        peopleList = []
        print("Peer: ")
        for item in peer:
            print(item)
        fileNumber = len(peer) - 1

        while (len(peopleList) < 6):
            peopleList = generateNum(fileNumber, peopleList)
            
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
        
        pollChannel = message.channel
        peopleInfo = message.channel
        placeInfo = message.channel
        weaponsInfo = message.channel

        for channel in message.guild.text_channels:
            print(channel.name)
            if channel.name == "historical-death-match-polls":
                print("found #channel " + channel.name)
                pollChannel = channel
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
            if channel.name == "historical-places-info":
                print("found #channel " + channel.name)
                placeInfo = channel
        
        print("Poll Channel: #" + pollChannel.name)
        match1 = person1 + " with " + weapon1 + " vs " + person2 + " with " + weapon2 + " " + place1 + "!"
        match2 = person3 + " with " + weapon3 + " vs " + person4 + " with " + weapon4 + " " + place2 + "!"
        match3 = person5 + " with " + weapon5 + " vs " + person6 + " with " + weapon6 + " " + place3 + "!"
        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)

        person1ID = peer[peopleList[0] + 1]
        person2ID = peer[peopleList[1] + 1]
        person3ID = peer[peopleList[2] + 1]
        person4ID = peer[peopleList[3] + 1]
        person5ID = peer[peopleList[4] + 1]
        person6ID = peer[peopleList[5] + 1]        

        person1Emoji = checkForEmoji(person1ID)
        person2Emoji = checkForEmoji(person2ID)
        person3Emoji = checkForEmoji(person3ID)
        person4Emoji = checkForEmoji(person4ID)
        person5Emoji = checkForEmoji(person5ID)
        person6Emoji = checkForEmoji(person6ID)

        


        await match1ID.add_reaction(emoji=person1Emoji)
        await match1ID.add_reaction(emoji=person2Emoji)
        await match2ID.add_reaction(emoji=person3Emoji)
        await match2ID.add_reaction(emoji=person4Emoji)
        await match3ID.add_reaction(emoji=person5Emoji) 
        await match3ID.add_reaction(emoji=person6Emoji)

        people = [person1, person2, person3, person4, person5, person6]
        weapons = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6]
        places = [place1, place2, place3]

        for person in people:
            embed = createPersonEmbed(person)
            await peopleInfo.send(embed=embed)
        for weapon in weapons:
            embed = createWeaponEmbed(weapon)
            await weaponsInfo.send(embed=embed)
        for place in places:
            embed = createPlaceEmbed(place)
            await placeInfo.send(embed=embed)
    if message.content.startswith("*ranked") and message.author.id == 366709133195476992:
        peerFile = open("reep VThe CA Discord.txt", "r")
        weaponTierFile = open("itemsAndLinks.txt", "r")
        placesFile = open("randomListPlaces.txt", "r")
        peerFull = peerFile.read()
        peer = peerFull.split(";")
        peerFile.close()
        peopleList = []
        print("Peer: ")
        for item in peer:
            print(item)
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
            print(channel.name)
            if channel.name == "historical-death-match-polls":
                print("found #channel " + channel.name)
                pollChannel = channel
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
            if channel.name == "historical-places-info":
                print("found #channel " + channel.name)
                placeInfo = channel
        
        print("Poll Channel: #" + pollChannel.name)
        match1 = person1 + " with " + weapon1 + " vs " + person2 + " with " + weapon2 + " " + place1 + "!"
        match2 = person3 + " with " + weapon3 + " vs " + person4 + " with " + weapon4 + " " + place2 + "!"
        match3 = person5 + " with " + weapon5 + " vs " + person6 + " with " + weapon6 + " " + place3 + "!"
        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)

        peerFile = open("peer.txt", "r")
        
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        peoplePeerIndex = []
        for person in people:
            personIndex = peer.index(person)
            peoplePeerIndex.append(personIndex)

        person1ID = peer[peoplePeerIndex[0] + 1]
        person2ID = peer[peoplePeerIndex[1] + 1]
        person3ID = peer[peoplePeerIndex[2] + 1]
        person4ID = peer[peoplePeerIndex[3] + 1]
        person5ID = peer[peoplePeerIndex[4] + 1]
        person6ID = peer[peoplePeerIndex[5] + 1]
        

        person1Emoji = checkForEmoji(person1ID)
        person2Emoji = checkForEmoji(person2ID)
        person3Emoji = checkForEmoji(person3ID)
        person4Emoji = checkForEmoji(person4ID)
        person5Emoji = checkForEmoji(person5ID)
        person6Emoji = checkForEmoji(person6ID)

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
    if message.content.startswith("*sendLastMatchInfo"):
        infoWrite = open("lastInfo.txt", "r")
        infoFull = infoWrite.read()
        info = infoFull.split("\n")

        for channel in message.guild.text_channels:
            print(channel.name)
            if channel.name == "historical-death-match-polls":
                print("found #channel " + channel.name)
                pollChannel = channel
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
            if channel.name == "historical-places-info":
                print("found #channel " + channel.name)
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
    if message.content.startswith("*weapons"):
        weaponTierFile = open("itemsAndLinks.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')
        for channel in message.guild.text_channels:
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
        for weaponFileName in weaponTierArray:
            weaponFile = open(weaponFileName + ".txt", "r")
            weaponSet = weaponFile.read().split('\n')
            for v in range(len(weaponSet)):
                if v % 2 == 0:
                    embed = createWeaponEmbed(weaponSet[v])
                    await weaponsInfo.send(embed=embed)
    if message.content.startswith("*places"):
        weaponTierFile = open("randomListPlaces.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')
        weaponsInfo = message.channel
        for channel in message.guild.text_channels:
            if channel.name == "historical-places-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
        for v in range(len(weaponTierArray)):
            if v % 2 == 0:
                embed = createPlaceEmbed(weaponTierArray[v])
                await weaponsInfo.send(embed=embed)
    if message.content.startswith("*newPeopleInfo"):
        weaponTierFile = open("newPeople.txt", "r")
        weaponTierFull = weaponTierFile.read()
        weaponTierArray = weaponTierFull.split('\n')
        weaponsInfo = message.channel
        for channel in message.guild.text_channels:
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
        for v in range(len(weaponTierArray)):
            if v % 2 == 0:
                embed = createPersonEmbed(weaponTierArray[v])
                await weaponsInfo.send(embed=embed)
    if message.content.startswith("*SuleimanSpecial"):
        sentMessage = await message.channel.send("An equal number of Suleiman to the people in this tier list with scimitars vs everyone else in this tier list with longswords at the gates of Vienna!")
        embed = createPersonEmbed("Suleiman the Magnificent")
        peopleInfo = message.channel
        for channel in message.guild.text_channels:
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
        await peopleInfo.send(embed=embed)
        crowdMoji = checkForEmoji(str(670378517585723443))
        SuleimanMoji = checkForEmoji(str(670368394180296744))
        await sentMessage.add_reaction(emoji=SuleimanMoji)
        await sentMessage.add_reaction(emoji=crowdMoji)
    if message.content.startswith("*SuperBowlSpecial"):
        sentMessage = await message.channel.send("The Kansas City Chiefs with bows vs the San Francisco 49ers with MAT-49s in a pottery contest!")
        #embed = createWeaponEmbed("MAT-49")
        peopleInfo = message.channel
        for channel in message.guild.text_channels:
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
        #await peopleInfo.send(embed=embed)
        crowdMoji = checkForEmoji(str(673616029485891612))
        SuleimanMoji = checkForEmoji(str(673616029850664991))
        await sentMessage.add_reaction(emoji=crowdMoji)
        await sentMessage.add_reaction(emoji=SuleimanMoji)
    if message.content.startswith("*lastMatch"):
        peerFile = open("reep VThe CA Discord.txt", "r")
        weaponTierFile = open("itemsAndLinks.txt", "r")
        placesFile = open("randomListPlaces.txt", "r")
        peerFull = peerFile.read()
        peer = peerFull.split(";")
        peerFile.close()
        peopleList = []
        print("Peer: ")
        for item in peer:
            print(item)
        fileNumber = len(peer) - 1

        peopleList.append(0)
        peopleList.append(1)
        peopleList.append(2)
        peopleList.append(3)
        peopleList.append(4)
        peopleList.append(5)
  
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
            print(channel.name)
            if channel.name == "historical-death-match-polls":
                print("found #channel " + channel.name)
                pollChannel = channel
            if channel.name == "historical-people-info":
                print("found #channel " + channel.name)
                peopleInfo = channel
            if channel.name == "historical-weapons-info":
                print("found #channel " + channel.name)
                weaponsInfo = channel
            if channel.name == "historical-places-info":
                print("found #channel " + channel.name)
                placeInfo = channel
        
        print("Poll Channel: #" + pollChannel.name)
        match1 = person1 + " with " + weapon1 + " vs " + person2 + " with " + weapon2 + " " + place1 + "!"
        match2 = person3 + " with " + weapon3 + " vs " + person4 + " with " + weapon4 + " " + place2 + "!"
        match3 = person5 + " with " + weapon5 + " vs " + person6 + " with " + weapon6 + " " + place3 + "!"
        
        match1ID = await pollChannel.send(match1)
        match2ID = await pollChannel.send(match2)
        match3ID = await pollChannel.send(match3)

        peerFile = open("peer.txt", "r")
        
        peerFull = peerFile.read()
        peer = peerFull.split("\n")
        peoplePeerIndex = []
        for person in people:
            personIndex = peer.index(person)
            peoplePeerIndex.append(personIndex)

        person1ID = peer[peoplePeerIndex[0] + 1]
        person2ID = peer[peoplePeerIndex[1] + 1]
        person3ID = peer[peoplePeerIndex[2] + 1]
        person4ID = peer[peoplePeerIndex[3] + 1]
        person5ID = peer[peoplePeerIndex[4] + 1]
        person6ID = peer[peoplePeerIndex[5] + 1]
        

        person1Emoji = checkForEmoji(person1ID)
        person2Emoji = checkForEmoji(person2ID)
        person3Emoji = checkForEmoji(person3ID)
        person4Emoji = checkForEmoji(person4ID)
        person5Emoji = checkForEmoji(person5ID)
        person6Emoji = checkForEmoji(person6ID)

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
    if message.content.startswith("*resetBracket"):
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
                    
tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
client.run(botToken)