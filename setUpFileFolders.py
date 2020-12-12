adjectiveTiersFile = open("Adjectives\\adjectiveTiers.txt", "r")
adjectiveTiersFull = adjectiveTiersFile.read()
adjectiveTiersArray = ["Tier1", "Tier2", "Tier3", "Tier4", "Tier5", "Tier6", "Tier7", "Tier8", "Tier9", "Tier10", "Tier11", "Tier12", "Tier13", "Tier14", "Tier15"]
for adjectiveTier in adjectiveTiersArray:
    adjectiveFile = open("Adjectives\\" + adjectiveTier + ".txt", "r")
    adjectiveFull = adjectiveFile.read()
    adjectiveArray = adjectiveFull.split("\n")
    for adjective in adjectiveArray:
        print("Adjective: " + adjective)
        addFile = open("Adjectives\\Descriptions\\" + adjectiveTier + "\\" + adjective + ".txt", "w")
        addFile.close()