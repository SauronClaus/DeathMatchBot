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


from wikidata.client import Client
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)

wikiClient = Client()

tokenFile = open("token.txt", "r", encoding='utf-8-sig')
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[0]
testToken = tokens[1]
userID = int(tokens[2])


def createPersonEmbed(person, teacherBracket=False):
    title = person
    person = checkLinks(person)
    article = wikipedia.page(person, auto_suggest=False)
    summary = article.summary.split('\n')
    summaryPersonal = summaryShort(str(summary[0]))
    embed = discord.Embed(title=title, description=summaryPersonal, color=0xFF9900)
    #print(summary[0])
    personURL = str("EMPTY EMOJI URL")
    if teacherBracket == False:
        embed.add_field(name="Link",value=article.url)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed
#Returns an embed object created from the inputed person.
url = 'https://wikidata.org/w/rest.php/wikibase/v0/entities/items/Q42'

headers = {
  'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4NDAyMDg2ZGM5MTVlMDMxNDBlMjBhMGVlZWUwNjlkNiIsImp0aSI6ImQ0MWM1ZTU2NWIzMWQ1ZTkzMmE5ZDhhMjY1ZjY4ODVlYzU3ZGM4YWYyZDM5OTk5MGYyNmU0MDU3NTA4NmE5YWUwMjAyZWIyMWMzOGI5MDI4IiwiaWF0IjoxNzEzMjMyNDU5LjkyMzgwMiwibmJmIjoxNzEzMjMyNDU5LjkyMzgwOCwiZXhwIjozMzI3MDE0MTI1OS45MjE3MzgsInN1YiI6Ijc1NDM5NTgwIiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.UqfOvVLy5dY4XQuE-fBii0llJTnRqxbD9VstJaQomboQrlbUd8ICBCvbaNAEDV74buauxDz10bpYDYUY5sgZsuFjngRnpQbtdwBVSIjo6xhDNtVjmJ_8kz29-zB0jannaKq5Kx1x10UFTOR_gmJEWJRBwTt5atGTr4i_f2-Z2XG3wGtIjuIrEc-_zjeiSr3VeBaS0rd2KykG8BrVm5ySIKVnoGmQa5U6eyKfmsvtARynM0YuLGhapT74Z60s9BSRPTfjaPPEzAsRYzTXBy4-j7sZjTMtKdAAf5eS6U6XpOmG3xQ6z19zwdwePim7rsRUR3Qxb17qS0VvxOezhT4Qi3rXq9mMj5wmnGz4ZbzQTcRAjwHqkZgN63uCQ-0R1kUulk5aXpFehpMEnuSIHT7qMZefBknWIns4zpQOvnkTnPIHtvsutHOgd_MstpaOeuMzRdbbOaQ9n8LmAh5Mna0AGxGrJwgIXO-KSA1SMFyV2QUZsko5YC1ZnGZddq5gNNJKRBUTp3MtHlOQqg0CIho6ru6KhzvgU0FfpiEDjU_99DHorVrf9bQudgR2M99TBHhNdj-OglXGEYtj2lOSgnV8ejIUAaHqUqz7w2-42d7AFWjkZm2e2-PHEYmVoDjzzwHDcnJ0CuaJkq15xWte3HQ7bI3CCnJ8Li2fHxqLlHN9MOE',
  'User-Agent': 'HDM Infinite'
}

def is_human(wikidata_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        
        claims = data['entities'][wikidata_id].get('claims', {})
        if 'P31' in claims:  # Check if the 'instance of' property exists
            for claim in claims['P31']:
                if 'datavalue' in claim['mainsnak'] and claim['mainsnak']['datavalue']['value']['id'] == 'Q5':
                    return True  # The item is an instance of human
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return False

def get_random_wikidata_item():
    url = "https://query.wikidata.org/sparql"
    query = """
    SELECT ?item ?itemLabel WHERE {
      ?item ?label ?value
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    ORDER BY RAND()
    LIMIT 1
    """
    headers = {
        "User-Agent": "ExampleBot/0.1 (https://yourwebsite.org/; mailto:your-email@example.com)",
        "Accept": "application/sparql-results+json"
    }
    response = requests.get(url, headers=headers, params={'query': query, 'format': 'json'})
    data = response.json()
    
    results = data['results']['bindings']
    if results:
        item = results[0]
        item_id = item['item']['value'].split('/')[-1]
        item_label = item['itemLabel']['value']
        return item_id, item_label
    return None, None

def get_random_wikipedia_article():
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,  # Namespace 0 indicates articles
        "rnlimit": 1       # Fetch one random article
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if data['query']['random']:
        title = data['query']['random'][0]['title']
        article_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
        return title, article_url
    else:
        return None, None

def get_wikidata_item_id(wikipedia_title, wikipedia_language='en'):
    url = f"https://{wikipedia_language}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": wikipedia_title,
        "prop": "pageprops",  # This property includes Wikidata item IDs
        "redirects": 1         # Automatically resolve redirects
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    pages = data.get("query", {}).get("pages", {})
    if pages:
        for page_id, page in pages.items():
            return page.get("pageprops", {}).get("wikibase_item", None)
    
    return None

def count_languages(wikidata_id):
    """Count the number of language versions for a Wikidata item."""
    url = f"https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "format": "json",
        "ids": wikidata_id,
        "props": "sitelinks"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'entities' in data and wikidata_id in data['entities']:
        sitelinks = data['entities'][wikidata_id].get('sitelinks', {})
        return len(sitelinks)
    return 0


@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("*infinitePower"):
            validRankedServers = {1173402242989166702: []}
            #validRankedServers = {620964009247768586: []}
            #Other server: 
            #Second one is the testing servers

            channel = message.channel
            quantMessages = 0
            numberOfMatches = 5
            messageResults = []

          
            
            guildID = message.guild.id
            numberOfMatchesFile = open("matchNumInfinite.txt", "r", encoding='utf-8-sig')
            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleList = []
            for match in range(numberOfMatches):
                person1 = [False, "[EMPTY]"]
                person2 = [False, "[EMPTY]"]

                while person1[0] == False or person2[0] == False:
                    # Example usage
                    title, url = get_random_wikipedia_article()
                    if title:
                        print(f"Random Wikipedia article: {title}\nURL: {url}")
                    else:
                        print("Failed to fetch a random article.")

                    wikidata_item_id = get_wikidata_item_id(title)
                    if wikidata_item_id:
                        print(f"Wikidata item ID for {title}: {wikidata_item_id}")
                    else:
                        print("No Wikidata item found for this article.")

                    # Example usage:
                    wikidata_id = wikidata_item_id  # Douglas Adams, for example
                    check = is_human(wikidata_id)
                    if check:
                        print(f"{wikidata_id} is a human.")
                    else:
                        print(f"{wikidata_id} is not a human.")
                    if check == True:
                        if person1[0] == True:
                            person2[0] = True
                            person2[1] = title
                        else:
                            person1[0] = True
                            person1[1] = title
                peopleList.append(person1[1])
                peopleList.append(person2[1])
            
            people = []
            for personIndex in peopleList:
                people.append(personIndex)

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
                        
            
            matchNumber = 0
            for match in matchMessages[0]:
                for matchSet in matchMessages:
                    await matchSet[matchNumber].add_reaction("1️⃣")
                    await matchSet[matchNumber].add_reaction("2️⃣")
                matchNumber+=1
            print("Completed!")
    if message.content.startswith("*completeRandom"):

            channel = message.channel
            quantMessages = 0
            numberOfMatches = 1
            messageResults = []
            
          
            
            guildID = message.guild.id
            validRankedServers = {guildID: []}

            numberOfMatchesFile = open("matchNumInfinite.txt", "r", encoding='utf-8-sig')
            numberOfMatchesFull = numberOfMatchesFile.read()
            numberOfMatchesInfos = numberOfMatchesFull.split("\n")
            numberOfMatchesTotal = int(numberOfMatchesInfos[0])
            numberOfRounds = int(numberOfMatchesInfos[2])
            numberOfMatchesRound = int(numberOfMatchesInfos[1])

            peopleList = []
            totalPeople = numberOfMatches * 2
            sorted = 0
            checked = 0

            print("Starting complete random!")
            for match in range(numberOfMatches):
                person1 = [False, "[EMPTY]"]
                person2 = [False, "[EMPTY]"]

                while person1[0] == False or person2[0] == False:
                    # Example usage
                    title, url = get_random_wikipedia_article()
                    #if title:
                        #print(f"Random Wikipedia article: {title}\nURL: {url}")
                    #else:
                        #print("Failed to fetch a random article.")

                    wikidata_item_id = get_wikidata_item_id(title)
                    #if wikidata_item_id:
                        #print(f"Wikidata item ID for {title}: {wikidata_item_id}")
                    #else:
                       #print("No Wikidata item found for this article.")

                    # Example usage:
                    wikidata_id = wikidata_item_id  # Douglas Adams, for example
                    check = is_human(wikidata_id)
                    #if check:
                        #print(f"{wikidata_id} is a human.")
                    #else:
                        #print(f"{wikidata_id} is not a human. [" + str(sorted) + "/" + str(totalPeople) + "]")
                
                    languages = count_languages(wikidata_id)
                    if languages >= 50 and check:
                        sorted+=1
                        print(title + " is famous enough! [" + str(sorted) + "/" + str(totalPeople) + "]")
                        print("\t" + str(languages))
                        if check == True:
                            if person1[0] == True:
                                person2[0] = True
                                person2[1] = title
                            else:
                                person1[0] = True
                                person1[1] = title
                    #else:
                        #print(title + " isn't famous enough. [" + str(sorted) + "/" + str(totalPeople) + "]")
                    checked+=1
                    if checked % 50 == 0:
                        print("\tChecked " + str(checked) + " articles.")  
                peopleList.append(person1[1])
                peopleList.append(person2[1])
            
            people = []
            for personIndex in peopleList:
                people.append(personIndex)

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
                    if serverID == 1173402242989166702:
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
                    else:
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
            numberOfMatchesFile = open("matchNumInfinite.txt", "w", encoding='utf-8-sig')
            numberOfMatchesFile.write(str(numberOfMatchesTotal + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfMatchesRound + numberOfMatches)+"\n")
            numberOfMatchesFile.write(str(numberOfRounds))
            numberOfMatchesFile.close()
                        
            
            matchNumber = 0
            for match in matchMessages[0]:
                for matchSet in matchMessages:
                    await matchSet[matchNumber].add_reaction("1️⃣")
                    await matchSet[matchNumber].add_reaction("2️⃣")
                matchNumber+=1
            print("Completed!")
    
    

client.run(botToken)