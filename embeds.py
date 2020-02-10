import discord
from discord.utils import get

import random
import wikipedia
import os.path
 
def createWeaponEmbed(weapon):
    print("Weapon: " + weapon)
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
#Returns an embed object from the weapon inputed. 
def createPlaceEmbed(place):
    print("Place: " + place)
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
#Returns an embed with the place inputed. 
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
        "Steve's Diamond Sword": "Minecraft",
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
    correct = objectName
    if objectName in largeDictionary:
        correct = largeDictionary[objectName]
    print("Correct Name: " + correct)
    return correct
#Replaces the passed in object with the correct object if it's an irregular wikipedia article. 