import discord
import os
intents = discord.Intents.all()
client = discord.Client(intents=intents)

discordEmojiList = ["test server", "1DiscordEmoji", "2DiscordEmojis", "3DiscordEmojis", "4DiscordEmojis", "5DiscordEmojis", "6EmojiServer", "7EmojiServer", "8EmojiServer", "9EmojiServer", "CA Teacher Emojis", "2CA Teacher Emojis"]
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

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "*go":
        faculty = open("Faculty Death Match2.txt", "r", encoding='utf8').read().split("\n")
        for person in faculty:
            messag2e = await message.channel.send(person.split("|")[0])
            await messag2e.add_reaction(emoji=checkForEmoji(person.split("|")[1]))
        print("Completed!")
client.run(botToken)