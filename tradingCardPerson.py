import discord
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import os

class TradingCard:
    def __init__(self, name, imageURL, infoLink, stats, equipment, rarity, summary):
        self.name = name
        self.image = imageURL
        self.infoLink = infoLink
        self.stats = []
        for stat in stats:
            stars = ""
            for i in range(int(stat)):
                stars = stars + "★"
            for i in range(5-len(stars)):
                stars= stars + "☆"
            self.stats.append(stars)
        #Strength, Speed, Intelligence, Constitution, Charisma
        self.health = stats[3] * 5
        if self.health <= 0:
            self.health = 1
        self.equipment = equipment
        self.rarity = rarity
        self.summary = summary
        rarityColors = {
        "Common":0xa2acc5,
        "Uncommon":0x58bb6b,
        "Rare":0x37b8ef,
        "Epic":0x7a4097,
        "Legendary":0xf4a24c
        }
        self.color = rarityColors[rarity]

    def sendCard(self):
        embed = discord.Embed(title=self.name, description=self.summary, color=self.color)
        
        
        embed.add_field(name="Stats",value="**Strength**: " + self.stats[0] + "\n**Speed**: " + self.stats[1] + "\n**Intelligence**: " + self.stats[2] + "\n**Constitution**: " + self.stats[3] + "\n**Charisma**: " + self.stats[4], inline=False)
        embed.add_field(name="Health",value=self.health)
        embed.add_field(name="Equipment",value=self.equipment)

        embed.add_field(name="Further Information",value="[Here](" + self.infoLink + ")")
        embed.set_image(url=self.image)

        embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

        return embed
    #Creates a trading card with the inputed person and rarity. 
    def sendGraph(self):
        os.remove("file.png")
        # Set data
        df = pd.DataFrame({
            'group': ['A'],
            'Strength': [self.stats[0]],
            'Speed': [self.stats[1]],
            'Intelligence': [self.stats[2]],
            'Constitution': [self.stats[3]],
            'Charisma': [self.stats[4]]
        })
        
        # number of variable
        categories=list(df)[1:]
        N = len(categories)
                
        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values=df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        values
                
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
                
        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)
                
        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories, color='grey', size=8)
            
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
        plt.ylim(0,5)
                
        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')
            
        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)

        # Show the graph

        plt.savefig("file.png")