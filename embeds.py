import discord
from discord.utils import get

import random
import wikipedia
import os.path
 
def createWeaponEmbed(weapon):
    print("Weapon: ~" + weapon + "~")
    weaponTiersFile = open("Armory\\Tiers\\weaponTierList.txt", "r")
    weaponTiersFull = weaponTiersFile.read()
    weaponTiersArray = weaponTiersFull.split("\n")
    tierName = ""
    tiers = []
    for tier in weaponTiersArray:
        tierFile = open("Armory\\Tiers\\" + tier + ".txt", "r")
        tierFull = tierFile.read()
        tierArray = tierFull.split("\n")
        for weaponSearch in tierArray:
            if weaponSearch == weapon:
                print("Found weapon! " + tier)
                tierName = tier
                tiers.append(tier)
    contentFile = open("Armory\\Descriptions\\" + tierName + "\\" + weapon + ".txt", "r")
    contentFull = contentFile.read()
    content = contentFull.split("\n")
    if weapon.split(" ")[0] == "a":
        weapon = weapon[2::]
    else:
        if weapon.split(" ")[0] == "an":
            weapon = weapon[3::]
    
    embed = discord.Embed(title=weapon[:1:].capitalize() + weapon[1::], description=content[0], color=0xFF9900)
    tierR = tiers[0]
    if len(tiers) <= 1:
        embed.add_field(name="Tier",value=tierName, inline=False)
    else:
        for tier in tiers:
            if tier != tiers[0]:
                tierR = tierR + "/" + tier
        embed.add_field(name="Tiers",value=tierR, inline=False)
    if len(content) >= 3:
        embed.add_field(name="Link", value=content[2], inline=False)
    if len(content) >= 2:
        imagePath = content[1]
        embed.set_image(url=imagePath)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object from the weapon inputed. 
def createPlaceLongEmbed(placeLong):
    print("Place: " + placeLong)
    propositions = ["on", "in", "above", "inside", "on", "top", "of"]
    placeLongArray = placeLong.split(" ")
    if placeLongArray[0] in propositions:
        print("removing " + placeLongArray[0])
        placeLongArray.remove(placeLongArray[0])
    if placeLongArray[0] in propositions:
        print("removing " + placeLongArray[0])
        placeLongArray.remove(placeLongArray[0])
    if placeLongArray[0] in propositions:
        print("removing " + placeLongArray[0])
        placeLongArray.remove(placeLongArray[0])
    placeLong = ""
    for item in placeLongArray:
        placeLong = placeLong + item + " "
    contentFile = open("Atlas\\Descriptions\\" + placeLong + ".txt", "r")
    contentFull = contentFile.read()
    content = contentFull.split("\n")
    imagePath = content[1]

    embed = discord.Embed(title=placeLong.capitalize()[0:1:] + placeLong[1:len(placeLong)-1:], description=content[0], color=0xFF9900)
    if len(content) >= 3:
        embed.add_field(name="Link", value=content[2], inline=False)
    embed.set_image(url=imagePath)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed with the place (with proposition) inputed. 
def createPlaceEmbed(place):
    print("Place: " + place)
    contentFile = open("Atlas\\Descriptions\\" + place + ".txt", "r")
    contentFull = contentFile.read()
    content = contentFull.split("\n")
    imagePath = content[1]
    
    embed = discord.Embed(title=place.capitalize()[0:1:] + place[1:len(place)-1:], description=content[0], color=0xFF9900)
    if len(content) >= 3:
        embed.add_field(name="Link", value=content[2], inline=False)
    embed.set_image(url=imagePath)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
def summaryShort(summary):
    summaryPersonal = ""
    if len(list(summary)) > 2040:
        summaryPersonal = str(summary[0:2000]) + "..."
    else:
        summaryPersonal = summary
    return summaryPersonal
#Shortens the summary to 2040 characters if needed. 
def checkLinks(objectName):
    largeDictionary = {
        "Malcolm X": "Malcolm Little",
        "petriefied Knuckles the Echidna": "Sonic the Hedgehog",
        "Harrison Ford": "Harrison J. Ford",
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
        "Tom Holland": "Thomas Stanley Holland",
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
        "Steve's Diamond Sword": "Min4craft",
        "Freddy Kruger's Glove": "Freddy Krueger",
        "their bear hands (replacing original hands)": "Bears",
        "Spider-Man's Right Webshooter": "Spider-Man",
        "a candlestick": "chamberstick",
        "an oversized Whac-A-Mole mallet": "Whac-A-Mole",
        "a mace": "Mace (weapon)", 
        "an immovable rod": "Magic item (Dungeons & Dragons)", 
        "a disco ball and chain": "Ball and chain",
        "a crusader's shield": "Crusades",
        "Mark Ruffalo": "Mark Alan Ruffalo",
        "their bare hands (duplicated)": "Hand",
        "Brandon Uri's guitar": "Guitar",
        "a Fortnite Pickaxe": "Fornite",
        "a pike (fish)": "Northern Pike Fish",
        "a Delorean's Car Door": "DeLorean Motor Company",
        "Napoleon Bonaparte's Petrified Body": "Napoleon",
        "a large non-personal Laser Cutter": "Laser cutting",
        "a handheld telescope": "Telescope",
        "a dead raven": "Raven",
        'the book "Give Me Liberty" by Eric Forner': "Eric Foner",
        "a very large rock": "Rock (geology)",
        "a shrunken Costco": "Costco Corporation",
        "Elon Musk": "Elon Reeve Musk",
        "a pair of nunchucks": "Nunchaku",
        "the toy knife from Undertale": "knife",
        "Sun Tzu": "Sun Wu",
        "John Cena": "John Felix Anthony Cena",
        "ï»¿Abraham Lincoln": "Abraham Lincoln",
        "Kaiser Wilhelm": "Kaiser Wilhelm II",
        "Charles Long (1st Baron Farnborough)": "Charles Long, 1st Baron Farnborough",
        "a greataxe": "Battle axe",
        "a Yellow-Finned Tuna": "Yellow Finned Tuna Fish", 
        "their bear hands (severed)": "Grizzlie Bears", 
        "Mr. RM's Glasses": "eyeglasses"
    }
    correct = objectName
    if objectName in largeDictionary:
        correct = largeDictionary[objectName]
    print("Correct Name: \"" + correct + "\"")
    return correct
#Replaces the passed in object with the correct object if it's an irregular wikipedia article. 
def createAdjectiveEmbed(adjective):
    print("Adjective: " + adjective)
    adjectiveTiersFile = open("Adjectives\\TierList.txt", "r")
    adjectiveTiersFull = adjectiveTiersFile.read()
    adjectiveTiersArray = adjectiveTiersFull.split("\n")

    adjectiveTierDescriptionsFile = open("Adjectives\\TierDescriptions.txt", "r")
    adjectiveTierDescriptionsFull = adjectiveTierDescriptionsFile.read()
    adjectiveTierDescriptionsArray = adjectiveTierDescriptionsFull.split("\n")

    tierName = ""
    for tier in adjectiveTiersArray:
        tierFile = open("Adjectives\\" + tier + ".txt", "r")
        tierFull = tierFile.read()
        tierArray = tierFull.split("\n")
        for adjectiveSearch in tierArray:
            if adjectiveSearch == adjective:
                print("Found adjective! " + tier)
                tierName = tier
    tierDescriptionNum = int(tierName[4::]) - 1
    tierDescription = adjectiveTierDescriptionsArray[tierDescriptionNum]
    if adjective[len(adjective)-1::] != "-":
        contentFile = open("Adjectives\\Descriptions\\" + tierName + "\\" + adjective[:len(adjective)-1:] + ".txt", "r")
    else:
        contentFile = open("Adjectives\\Descriptions\\" + tierName + "\\" + adjective + ".txt", "r")
    contentFull = contentFile.read()
    content = contentFull.split("\n")
    embed = discord.Embed(title=adjective[:1:].capitalize() + adjective[1::], description=content[0].capitalize()[:1:] + content[0][1::], color=0xFF9900)
    tierName = "Tier " + tierName[4::]
    embed.add_field(name="Tier",value=tierName + " (" + tierDescription + ")", inline=False)
    if not(content[1].startswith("https://www.dictionary.com/")):
        embed.add_field(name="Link",value=content[1], inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create an adjective embed
def createSongEmbed(songName):
    print("Song Title: " + songName)

    songFile = open("Competition Exclusive Info\\Songs\\" + songName + ".txt", "r")
    songFull = songFile.read()
    song = songFull.split("\n")

    embed = discord.Embed(title=songName, description="[Link](%s)" % (song[0]), color=0xFF9900)
    embed.add_field(name="Artist",value=song[1], inline=True)
    embed.add_field(name="Album",value=song[2], inline=True)
    embed.add_field(name="Length",value=song[3], inline=True)
    embed.set_image(url=song[4])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create a song embed
def createMarioMinigameEmbed(minigame):
    print("Minigame: " + minigame)
    
    minigameFile = open("Competition Exclusive Info\\Mario Party 10 Minigames\\" + minigame + ".txt", "r")
    minigameFull = minigameFile.read()
    minigameInfo = minigameFull.split("\n")

    embed = discord.Embed(title=minigame, description=minigameInfo[0], color=0xFF9900)
    embed.add_field(name="Type",value=minigameInfo[1], inline=True)
    embed.set_image(url=minigameInfo[2])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create a Mario Party 10 Minigame embed
def createSpaceShipEmbed(spaceship):
    print("Spaceship: " + spaceship)

    spaceShipFile = open("Competition Exclusive Info\\Spaceships\\" + spaceship + ".txt", "r")
    spaceShipFull = spaceShipFile.read()
    spaceShipInfo = spaceShipFull.split("\n")

    embed = discord.Embed(title=spaceship, description=spaceShipInfo[0], color=0xFF9900)
    embed.add_field(name="Link",value=spaceShipInfo[1], inline=True)
    embed.set_image(url=spaceShipInfo[2])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for Spaceships! (Which is currently only the X-wing)
def createJudgeEmbedCooking(judge, typeContest):
    print("Judge: " + judge + "\nType: " + typeContest)

    judgeFile = open("Competition Exclusive Info\\Judges\\Cooking Contest\\" + judge + ".txt", "r")
    judgeFull = judgeFile.read()
    judgeInfo = judgeFull.split("\n")
    if judge == "the Swedish Chef":
        embed = discord.Embed(title="The Swedish Chef", description=judgeInfo[0], color=0xFF9900)
    else:
        embed = discord.Embed(title=judge, description=judgeInfo[0], color=0xFF9900)
    embed.add_field(name="Link",value=judgeInfo[1], inline=False)
    embed.add_field(name="Competition Type",value=typeContest, inline=False)
    embed.set_image(url=judgeInfo[2])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for a Judge for a cooking contest!
def createJudgeEmbedCleaning(judge, typeContest, judgeTrio):
    print("Judge: " + judge + "\nType: " + typeContest)

    locationFile = open("Competition Exclusive Info\\Judges\\Cleaning Competition\\locations.txt", "r")
    locationFull = locationFile.read()
    locations = locationFull.split("\n")

    judgesFile = open("Competition Exclusive Info\\Judges\\Cleaning Competition\\judges.txt", "r")
    judgesFull = judgesFile.read()
    judgesInfo = judgesFull.split("\n")

    indexNumber = judgesInfo.index(judgeTrio)
    location = locations[indexNumber]

    judgeFile = open("Competition Exclusive Info\\Judges\\Cleaning Competition\\" + judge + ".txt", "r")
    judgeFull = judgeFile.read()
    judgeInfo = judgeFull.split("\n")

    embed = discord.Embed(title=judge, description=judgeInfo[0], color=0xFF9900)
    embed.add_field(name="Link",value=judgeInfo[1], inline=False)
    embed.add_field(name="Competition Type",value=typeContest, inline=False)
    embed.add_field(name="Location",value=location, inline=False)
    embed.set_image(url=judgeInfo[2])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for a Judge for a cleaning competition!
def createJudgeThreeSet(judgeTrio, typeContest):
    judgeSplit = judgeTrio.split(", ")
    judgeEmbeds = {}
    for judge in judgeSplit:
        if typeContest == "Cleaning Competition":
            judgeEmbeds[judge] = createJudgeEmbedCleaning(judge, typeContest, judgeTrio)
        else:
            judgeEmbeds[judge] = createJudgeEmbedCooking(judge, typeContest)
    return judgeEmbeds
#Returns the embeds for a judge trio
def createFranchiseEmbed(franchise):
    print("Franchise: " + franchise)

    franchiseFile = open("Competition Exclusive Info\\Franchise\\" + franchise + ".txt", "r")
    franchiseFull = franchiseFile.read()
    franchiseInfo = franchiseFull.split("\n")

    embed = discord.Embed(title=franchise, description=franchiseInfo[0], color=0xFF9900)
    embed.add_field(name="Link",value=franchiseInfo[1], inline=True)
    embed.set_image(url=franchiseInfo[2])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for a Franchise!
def createFoodEmbed(food):
    print("Food: |" + food + "|")

    foodFile = open("Competition Exclusive Info\\Food\\Food\\" + food + ".txt", "r")
    foodFull = foodFile.read()
    foodInfo = foodFull.split("\n")
    
    embed = discord.Embed(title=food, description="%s [Link](%s)" % (foodInfo[0], foodInfo[1]), color=0xFF9900)
    if foodInfo[1] == "":
        embed = discord.Embed(title=food, description="%s" % (foodInfo[0]), color=0xFF9900)
    ingredients = foodInfo[2].split("|")
    ingredientBlock = ""
    for ingredient in ingredients:
        ingredientBlock = ingredientBlock + "\n" + ingredient
    if ingredientBlock != "" and ingredientBlock != "\n":
        embed.add_field(name="Ingredients",value=ingredientBlock[1::], inline=False)
    time = foodInfo[3].split("|")
    if time[0] != "":
        embed.add_field(name="Prep Time",value=time[0], inline=True)
    if time[1] != "":
        embed.add_field(name="Cooking Time",value=time[1], inline=True)
    if time[2] != "":
        embed.add_field(name="Total Time",value=time[2], inline=True)
    embed.set_image(url=foodInfo[4])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Creates an embed for a dish!
def createPieEmbed(pie):
    print("Pie: " + pie)

    pieFile = open("Competition Exclusive Info\\Food\\Pies\\" + pie + ".txt", "r")
    pieFull = pieFile.read()
    pieInfo = pieFull.split("\n")

    embed = discord.Embed(title=pie[:1:].capitalize() + pie[1::], description="%s [Link](%s)" % (pieInfo[0], pieInfo[1]), color=0xFF9900)
    embed.add_field(name="Calories",value=pieInfo[2], inline=True)
    embed.set_image(url=pieInfo[3])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create a pie embed!
def createDrinkEmbed(drink):
    print("Drink: " + drink)

    drinkFile = open("Competition Exclusive Info\\Drinks\\" + drink + ".txt", "r")
    drinkFull = drinkFile.read()
    drinkInfo = drinkFull.split("\n")

    embed = discord.Embed(title=drink, description=drinkInfo[0], color=0xFF9900)
    embed.add_field(name="ABV",value=drinkInfo[1], inline=True)
    embed.add_field(name="Proof",value=drinkInfo[2], inline=True)

    embed.set_image(url=drinkInfo[3])
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Create a drink embed!
def createContestEmbed(contest, ruleset):
    print("Contest: " + contest)

    contestFile = open("Contests\\" + contest + "\\description.txt", "r")
    contestFull = contestFile.read()
    contestInfo = contestFull.split("\n")

    rulesFile = open("Contests\\" + contest + "\\" + ruleset + "rules.txt", "r")
    rulesFull = rulesFile.read()
    rulesInfo = rulesFull.split("\n")
    
    embed = discord.Embed(title=contest, description="%s [Link](%s)" % (contestInfo[0], contestInfo[1]), color=0xFF9900)
    embed.add_field(name="Ruleset",value=ruleset, inline=False)

    rulesBlock = ""
    for rule in rulesInfo:
        rulesBlock = rulesBlock + "\n-" + rule
    if rulesBlock != "" and rulesBlock != "\n":
        embed.add_field(name="Rules",value=rulesBlock[1::], inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Generate Info for a contest!
def createHDMClassicEmbed():
    print("HDM Classic")
    
    embed = discord.Embed(title="Deathmatch Classic", description="The Deathmatch Classic is the classic 1v1 death match of HDM.", color=0xFF9900)
    embed.add_field(name="Rules",value="- Both competitors know how to activate their weapons.", inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Generate Info for an hDM Classic Death Match!