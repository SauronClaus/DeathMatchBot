adjectivesQuant = 16
for numTier in range(adjectivesQuant):
    print("Tier: Tier" + str(numTier+1))
    tierFile = open("Adjectives\\Tier" + str(numTier+1) + ".txt", "r")
    tierFull = tierFile.read()
    tierArray = tierFull.split("\n")
    tierFile.close()
    overWriteFile = open("Adjectives\\Tier" + str(numTier+1) + ".txt", "w")
    for adjective in tierArray:
        print(adjective)
        overWriteFile.write("\n" + adjective)
    overWriteFile.close()