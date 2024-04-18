if message.content.startswith("*info"):
                messageContent = message.content[6::]
                
                peopleFile = open("people.txt", "r", encoding='utf-8-sig')
                peopleFull = peopleFile.read()
                peopleArray = peopleFull.split("\n")

                weaponTierFile = open("Armory\\Tiers\\weaponTierList.txt", "r", encoding='utf-8-sig')
                weaponTierFull = weaponTierFile.read()
                weaponTierArray = weaponTierFull.split("\n")
                weaponArray = []
                weaponMinusFirstWord = []
                for weaponTier in weaponTierArray:
                    weaponFile = open("Armory\\Tiers\\" + weaponTier + ".txt", "r", encoding='utf-8-sig')
                    weaponFull = weaponFile.read()
                    weaponArrayTemp = weaponFull.split("\n")
                    for weapon in weaponArrayTemp:
                        weaponArray.append(weapon)
                        
                placesFile = open("Atlas\\placesName.txt", "r", encoding='utf-8-sig')
                placesFull = placesFile.read()
                placesArray = placesFull.split("\n")

                adjectiveTierFile = open("Adjectives\\TierList.txt", "r", encoding='utf-8-sig')
                adjectiveTierFull = adjectiveTierFile.read()
                adjectiveTierArray = adjectiveTierFull.split("\n")

                adjectiveArray = []
                for adjectiveTier in adjectiveTierArray:
                    adjectiveFile = open("Adjectives\\" + adjectiveTier + ".txt", "r", encoding='utf-8-sig')
                    adjectiveFull = adjectiveFile.read()
                    adjectiveArrayTemp = adjectiveFull.split("\n")
                    for adjective in adjectiveArrayTemp:
                        adjectiveArray.append(adjective)
                
                
                songsFile = open("Competition Exclusive Info\\Songs\\songs.txt", "r", encoding='utf-8-sig')
                songsFull = songsFile.read()
                songsArray = songsFull.split("\n")

                minigamesFile = open("Competition Exclusive Info\\Mario Party 10 Minigames\\minigames.txt", "r", encoding='utf-8-sig')
                minigamesFull = minigamesFile.read()
                minigamesArray = minigamesFull.split("\n")

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
                                if messageContent in songsArray:
                                    print("Query is Song")
                                    embed = createSongEmbed(messageContent)
                                    await message.channel.send(embed=embed)
                                else:
                                    if messageContent in minigamesArray:
                                        print("Query is Mario Party 10 Minigame")
                                        embed = createMarioMinigameEmbed(messageContent)
                                        await message.channel.send(embed=embed)
                                    else:
                                        await message.channel.send(messageContent + " was not found.")
    #Grab info on a person, weapon, adjective, or place!
    if message.content.startswith("*newPeopleInfo"):
                weaponTierFile = open("newPeople.txt", "r", encoding='utf-8-sig')
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
    #Generate a random historical figure.
    if message.content.startswith("*mhaMe"):
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()
        RNG = random.randint(0, len(peopleArray)-1)
        await message.channel.send(peopleArray[RNG] + "!")
    #Generate a random MHA character.
    if message.content.startswith("*declare"):
        declaredPerson = message.content[9::].strip()
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()

        
        if declaredPerson in peopleArray:
            pityChart[message.author.id] = declaredPerson
            declaredFile = open("declaredGacha.txt", "w", encoding='utf-8-sig')
            #print(str(pityChart))
            for personID in pityChart.keys():
                declaredFile.write(str(personID) + "|" + pityChart[personID] + "\n")
            declaredFile.close()
            await message.channel.send("<@" + str(message.author.id) + "> has declared " + declaredPerson + "!")
        else:
            if declaredPerson == "":
                test = ""
                try:
                    test = pityChart[message.author.id]
                    await message.channel.send("<@" + str(message.author.id) + "> has " + pityChart[message.author.id] + " declared!")
                except:
                    await message.channel.send("<@" + str(message.author.id) + "> has nobody declared!")

            #print("|" + declaredPerson + "|")
            #print(str(peopleArray))
            else:
                await message.channel.send(declaredPerson + " doesn't exist!")
    #Declare a MHA character for the gacha system.
    if message.content.startswith("*roll"):
        peopleFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')

        peopleFull = peopleFile.read()
        peopleArray = peopleFull.split("\n")
        peopleFile.close()

        RNG = random.randint(0, len(peopleArray))

        chosen = peopleArray[RNG]

        pityFile = open("pityCount.txt", "w", encoding='utf-8-sig')
        pityCurrent = 0
        try:
            pityCurrent = pityCount[message.author.id]
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
        except:
            pityCount[message.author.id] = 0
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")

        immutablePity = pityCurrent
        if pityCurrent >= pityNum:
            pityCurrent = pityNum
        pityCheck = random.randint(pityCurrent, 100)

        test = ""
        try:
            test = pityChart[message.author.id]
        
            if pityCheck == 100 or chosen == pityChart[message.author.id]:
                chosen = pityChart[message.author.id]
                pityCount[message.author.id] = 0
                for personID in pityCount.keys():
                    pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
                try:
                    currentStats[message.author.id][chosen]+=1
                except:
                    try: 
                        currentStats[message.author.id][chosen] = 1
                    except:
                        currentStats[message.author.id] = {chosen: 1}
                writeFile = open("Gacha Storage Characters\\" + str(message.author.id) + ".txt", "w", encoding='utf-8-sig')
                for person in currentStats[message.author.id].keys():
                    writeFile.write(person + "|" + str(currentStats[message.author.id][person]) + "\n")
                writeFile.close()
                #print(str(currentStats))
                await message.channel.send("<@" + str(message.author.id) + ">, you got " + chosen + "! (pity count: " + str(immutablePity) + ")")
            else:
                pityCount[message.author.id] += 1
                for personID in pityCount.keys():
                    pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
                try:
                    currentStats[message.author.id][chosen]+=1
                except:
                    try: 
                        currentStats[message.author.id][chosen] = 1
                    except:
                        currentStats[message.author.id] = {chosen: 1}
                #print(str(currentStats))
                writeFile = open("Gacha Storage Characters\\" + str(message.author.id) + ".txt", "w", encoding='utf-8-sig')
                for person in currentStats[message.author.id].keys():
                    writeFile.write(person + "|" + str(currentStats[message.author.id][person]) + "\n")
                writeFile.close()
                await message.channel.send(chosen + "!")
            pityFile.close()
        except:
            pityCount[message.author.id] += 1
            for personID in pityCount.keys():
                pityFile.write(str(personID) + "|" + str(pityCount[personID]) + "\n")
            try:
                currentStats[message.author.id][chosen]+=1
            except:
                try: 
                    currentStats[message.author.id][chosen] = 1
                except:
                    currentStats[message.author.id] = {chosen: 1}
            #print(str(currentStats))
            writeFile = open("Gacha Storage Characters\\" + str(message.author.id) + ".txt", "w", encoding='utf-8-sig')
            for person in currentStats[message.author.id].keys():
                writeFile.write(person + "|" + str(currentStats[message.author.id][person]) + "\n")
            writeFile.close()
            await message.channel.send(chosen + "!")
        pityFile.close()
    #Roll on the gacha wheel.
    if message.content.startswith("*currentStats"):
        print(str(currentStats))

        finder = message.content[16:len(message.content)-1:]
        if finder == "":
            finder = message.author.id
        test = []
        try:
            test = currentStats[int(finder)]
        except:
            currentStats[int(finder)] = {}
        print(currentStats[int(finder)])
        statsArray = sorted(currentStats[int(finder)].items(), key=lambda x:x[1], reverse=True)
        newMessage = "__<@" + str(finder) + "> stats:__"
        statsList = dict(statsArray)

        totalNum = 0
        for person in statsList.keys():
            totalNum+=statsList[person]
        for person in statsList.keys():
            if statsList[person] > totalNum * 0.02:
                newMessage = newMessage + "\n" + person + ": " + str(statsList[person])
        newMessage = newMessage + "\n" + "**Total Rolls: ** " + str(totalNum)
        newMessage = newMessage + "\n" + "**Characters Obtained: **" + str(len(statsList.keys())) + "/220"
        
        mhaFile = open("mhaCharacters.txt", "r", encoding="utf-8-sig")
        mhaArray = mhaFile.read().split("\n")
        if len(statsList.keys()) >= 200 and len(statsList.keys()) < 220:
            newMessage = newMessage + "\n" + "**Characters Remaining: **"
            for character in mhaArray:
                if not character in statsList.keys():
                    newMessage = newMessage + character + ", "
            newMessage = newMessage[0:len(newMessage)-2:]
        await message.channel.send(newMessage)
    #Check your current stats with the gacha.      
    if message.content.startswith("*pity"):
        pityCurrent = 0
        finder = message.content[8:len(message.content)-1:]
        if finder == "":
            finder = message.author.id

        try:
            pityCurrent = pityCount[int(finder)]
        except:
            pityCount[int(finder)] = 0
        await message.channel.send("<@" + str(finder) + "> has a current pity count of " + str(pityCurrent))
    #Checks your current pity.  
    if message.content.startswith("*checkCharacter"):
        characterName = message.content[16::]
        finder = message.author.id
        print(str(len(message.content)))
        if characterName == "" or len(message.content) == 15:
            try:
                test = currentStats[int(finder)]
            except:
                currentStats[int(finder)] = {}
            print(currentStats[int(finder)])
            statsArray = sorted(currentStats[int(finder)].items(), key=lambda x:x[1], reverse=True)
            newMessage = "__<@" + str(finder) + "> Characters:__"
            await message.channel.send(newMessage)
            statsList = dict(statsArray)
            for person in statsList.keys():
                await message.channel.send(person + ": " + str(statsList[person]))
        else:
            try:
                
                await message.channel.send("<@" + str(finder) + "> has " + str(currentStats[finder][characterName]) + " of " + characterName)
            except:
                mhaCharacterFile = open("mhaCharacters.txt", "r", encoding='utf-8-sig')
                mhaCharacters = mhaCharacterFile.read().split("\n")
                mhaCharacterFile.close()
                if characterName in mhaCharacters:
                    await message.channel.send("<@" + str(finder) + "> has 0 of " + characterName)
                else:
                    await message.channel.send(characterName + " doesn't exist!")
    #Checks the quantity of a character owned.
    if message.content.startswith("*missingMHA"):
        finder = message.author.id
        try:
            test = currentStats[int(finder)]
        except:
            currentStats[int(finder)] = {}
        print(currentStats[int(finder)])
        statsArray = sorted(currentStats[int(finder)].items(), key=lambda x:x[1], reverse=True)
        newMessage = "<@" + str(finder) + "> **Missing Characters: **"
        statsList = dict(statsArray)
        mhaFile = open("mhaCharacters.txt", "r", encoding="utf-8-sig")
        mhaArray = mhaFile.read().split("\n")
        mhaFile.close()
        for character in mhaArray:
            if not character in statsList.keys():
                newMessage = newMessage + character + ", "
        
        
        if len(newMessage) <= 1990:
            await message.channel.send(newMessage[0:len(newMessage)-2:])
        else:
            chunks = [newMessage[i:i+1990] for i in range(0, len(newMessage), 1990)]
            for i, chunk in enumerate(chunks, 1):
                await message.channel.send(chunk)
    #Prints a list of the user's missing characters
    if message.content.startswith("*contestant"):
        coin = random.randint(0,1)
        human = "[Error]"
        if coin == 0:
            person = generatePerson()
            human = person[0]
        else:
            peopleFile = open("mhaBracket.txt", "r", encoding='utf-8-sig')

            peopleFull = peopleFile.read()
            peopleArray = peopleFull.split("\n")
            peopleFile.close()
            RNG = random.randint(0, len(peopleArray))
            human = peopleArray[RNG]
        adjective = generateAdjective().capitalize()
        weapon = generateWeapon()

        await message.channel.send(adjective + human + " with " + weapon)
    #Generates an adjective, person, and weapon.
    if message.content.startswith("*powerUp"):
        newMessage = message.content[9::]
        if newMessage == "":
            adjective = generateAdjective().strip()
            weapon = generateWeapon().strip()
            await message.channel.send("You are " + adjective + " and you have " + weapon)
        else:
            adjective = generateAdjective().capitalize()
            weapon = generateWeapon()
            await message.channel.send(adjective + message.content[9::] + " with " + weapon)
    #Gives a weapon and an adjective to someone.
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
                match = adjectives[0].capitalize()[:1:] + adjectives[0][1::] + person1[0] + " with " + weapons[0] + " vs " + adjectives[1] + person2[0] + " with " + weapons[1] + " " + place + "!"
                matchMessage = await message.channel.send(match)
                emoji1 = getEmoji(person1[0])
                emoji2 = getEmoji(person2[0])
                await matchMessage.add_reaction(emoji1)
                await matchMessage.add_reaction(emoji2)
    #Single match for everyone to use. Currently only runs classic HDM matches. 
    if message.content.startswith("*react"):
                messageArray = message.content.split(" ")
                if len(messageArray) >= 3:
                    messageArray.pop(0)
                    mixedMessageChannel = messageArray[0]
                    idArray = mixedMessageChannel.split("-")
                    print("Message ID: " + str(idArray[1]))
                    print("Channel ID: " + str(idArray[0]))
                    channelID = message.guild.get_channel(int(idArray[0]))
                    msg = await channelID.fetch_message(idArray[1])
                    messageArray.pop(0)
                    name = ""
                    for item in messageArray:
                        name = name + item + " "
                    name = name.strip()
                    emoji = getEmoji(name)
                    print("Person: " + name)
                    await message.delete()
                    await msg.add_reaction(emoji)
    #React with an emoji; uses the syntax `*react [channelID]-[messageID] [Emoji Name]`
    if message.content.startswith("*register") or message.content.startswith("*suggest"):
                peopleFile = open("peer.txt", "r", encoding='utf-8-sig')
                peopleFull = peopleFile.read()
                peopleID = peopleFull.split("\n")
                suggestionFile = open("suggestions.txt", "r", encoding='utf-8-sig')
                suggestions = suggestionFile.read()
                suggestionFile.close()
                suggestionsArray = suggestions.split("\n")
                people = []
                for index in range(len(peopleID)):
                    if index % 2 == 0 and (peopleID[index] != "A" and peopleID[index] != "B"):
                        people.append(peopleID[index])

                person = message.content[9:len(message.content)]
                print("Person: " + person)
                if person in people:
                    response = await message.channel.send(person + " is already in Historical Death Match! (ID " + peopleID[peopleID.index(person) + 1] + ")")
                else:
                    if person in suggestionsArray:
                        response = await message.channel.send(person + " has already been suggested (but not yet added!).")
                    else:
                        suggestionFile = open("suggestions.txt", "w", encoding='utf-8-sig')
                        suggestionFile.write(suggestions)
                        suggestionFile.write("\n" + person)
                        suggestionFile.close()
                        response = await message.channel.send("Added " + person + " to suggestions.")
                await message.delete()
                time.sleep(2)
                await response.delete()
    #Command to suggest new people!  
    if message.content.startswith("*about"):
                embed = discord.Embed(title="About HDM!", description='"though I would' + "'ve bribed people to get stephen hawking to win that one match" + '"\n-Harrison Truscott\nHistorical Death Match (found here https://github.com/fixmeseb/DeathMatchBot) is a Discord bot that started out when I thought, "Hey, you know what' + "'s funny?" + ' Historical figures fighting each other. I could do something with this!" And then I did. Abbreviated to HDM a lot, HDM is currently running it' + "'s third iteration of the bot (with adjectives!) on the CA Discord Server, and otherwise is soon ready to be added to other server- just reach out to me at the below Discord address or at sauronclaus@gmail.com to see if we can work something out!", color=0xFF9900)
                embed.add_field(name="Lines of Code in Main File", value=2000)
                embed.add_field(name="People", value=574)
                embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
                await message.channel.send(embed=embed)
    #Gives some info about the bot!
