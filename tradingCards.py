import wikipedia
import discord

import os
import random

def createCard(owner, person, rarity, emojiID):
    rarityColors = {
        "Common":0xa2acc5,
        "Uncommon":0x58bb6b,
        "Rare":0x37b8ef,
        "Epic":0x7a4097,
        "Legendary":0xf4a24c
    }
    AbeLincoln = ["★★☆☆☆", "★★☆☆☆", "★★★☆☆", "★★★☆☆", 15, "Dreamer", "Abraham Lincoln was an American statesman and lawyer who served as the 16th president of the United States from 1861 until his assassination in 1865."]
    HeinrichHertz = ["★★★☆☆", "★★★☆☆", "★★★★☆", "★★☆☆☆", 10, "Artist", "Heinrich Rudolf Hertz was a German physicist who first conclusively proved the existence of the electromagnetic waves predicted by James Clerk Maxwell's equations of electromagnetism."]
    RichardNixon = ["★★★☆☆", "★★★☆☆", "★★★★★", "★★★☆☆", 15, "Soldier", "Richard Milhous Nixon was the 37th president of the United States, serving from 1969 until 1974, and is the only president to resign from office following the Watergate Scandal."]
    JRobertOppenheimer = ["★★★★☆", "★★★★☆", "★★★★★", "★★★☆☆", 15, "Dreamer", "J. Robert Oppenheimer was an American theoretical physicist and professor of physics at the University of California, Berkeley, and the wartime head of the Los Alamos Laboratory, which developed the Manhatten Project and the Atomic Bomb."]
    OdaNobunaga = ["★★★★★", "★★★★★", "★★★★☆", "★★★★☆", 20, "Soldier", "Oda Nobunaga was a Japanese daimyō and one of the leading figures of the Sengoku period."]
    article = wikipedia.page(person, auto_suggest=False)
    dictionaryDefs = {
        "Abraham Lincoln":AbeLincoln,
        "Heinrich Hertz":HeinrichHertz,
        "J. Robert Oppenheimer":JRobertOppenheimer,
        "Richard Nixon":RichardNixon,
        "Oda Nobunaga":OdaNobunaga
    }
    embed = discord.Embed(title=person, description=dictionaryDefs[person][6], color=rarityColors[rarity])
    embed.add_field(name="Name",value=owner.name)
    embed.add_field(name="Stats",value="**Strength**: " + dictionaryDefs[person][0] + "\n**Speed**: " + dictionaryDefs[person][1] + "\n**Intelligence**: " + dictionaryDefs[person][2] + "\n**Constitution**: " + dictionaryDefs[person][3], inline=False)
    embed.add_field(name="Health",value=dictionaryDefs[person][4])
    embed.add_field(name="Equipment",value=dictionaryDefs[person][5])

    personEmoji = str(emojiID)
    personURL = str(personEmoji.url)

    embed.add_field(name="Further Information",value="[Here](" + article.url + ")")
    embed.set_image(url=personURL)

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed
#Creates a trading card with the inputed person and rarity. 
def grantCard(owner, person, rarity):
    filePath = 'C:\\Users\\Sebastian_Polge\\OneDrive-CaryAcademy\Documents\\meNewBot\\ProjectDeathMatch\\Players\\%s\\%s' % (owner.id, rarity)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    tradingCard = []
#Gives the wielder a card with the specific info. 
def generateStats(rarity):
    rarityStatNums = {
        "Common": 13, 
        "Uncommon": 15, 
        "Rare": 17, 
        "Epic": 19, 
        "Legendary": 21}
    totalNum = rarityStatNums[rarity]
    stats = []
    for stat in range(5):
        randomNum = random.randint(0, 5)
        totalNum-=randomNum
        if totalNum < 0:
            valueOverflow = abs(0-totalNum)
            while valueOverflow > 0: 
                randomStatNum = random.randint(0, len(stats)-1)
                randomStat = stats[randomStatNum]
                newRandomStat = randomStat-valueOverflow
                if newRandomStat < 0:
                    newRandomStat = 0
                    valueOverflow = valueOverflow - randomStat
                stats[randomStatNum] = newRandomStat
                print("Set stat (decrease) to " + str(randomStat))
        stats.append(randomNum)
    print("Total Num: " + str(totalNum))
    while totalNum > 0:
        randomStatNum = random.randint(0, len(stats)-1)
        randomStat = stats[randomStatNum]
        increaseAmount = random.randint(1, 3)
        if totalNum-increaseAmount < 0:
            increaseAmount = abs(0-totalNum)
        newRandomStat = randomStat+increaseAmount
        if newRandomStat > 5:
            newRandomStat = 5
            increaseAmount = newRandomStat-randomStat
        totalNum = totalNum - increaseAmount
        print("Set stat (" + str(randomStat) + ") (increase) to " + str(newRandomStat) + "; total num is " + str(totalNum))
        stats[randomStatNum] = newRandomStat
    random.shuffle(stats)
    return stats
#Generates 5 random stats.

