tierFile = open("Adjectives\\TierList.txt", "r")
tierFull = tierFile.read()
tiers = tierFull.split("\n")
for tier in tiers:
    if tier != "Tier1" and tier != "Tier2":
        tier2File = open("Adjectives\\" + tier + ".txt", "r")
        tier2Full = tier2File.read()
        tiers2 = tier2Full.split("\n")
        for adjective in tiers2:
            if adjective[len(adjective)-1:len(adjective):] == " ":
                adjectiveFile = open("Adjectives\\Descriptions\\" + tier + "\\" + adjective[:len(adjective)-1:] + ".txt", "r")
                adjectivesFull = adjectiveFile.read()
                adjectivesSplit = adjectivesFull.split("\n")
                adjectiveFile.close()
                adjectiveFile = open("Adjectives\\Descriptions\\" + tier + "\\" + adjective[:len(adjective)-1:] + ".txt", "w")
                adjectiveFile.write(adjectivesSplit[0] + "\n" + "https://www.dictionary.com/browse/" + adjective[:len(adjective)-1:])
            else:
                adjectiveFile = open("Adjectives\\Descriptions\\" + tier + "\\" + adjective + ".txt", "r")
                adjectivesFull = adjectiveFile.read()
                adjectivesSplit = adjectivesFull.split("\n")
                adjectiveFile.close()
                adjectiveFile = open("Adjectives\\Descriptions\\" + tier + "\\" + adjective + ".txt", "w")
                adjectiveFile.write(adjectivesSplit[0] + "\n" + "https://www.dictionary.com/browse/" + adjective[:len(adjective)-1:])