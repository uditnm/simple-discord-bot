import discord
from discord.ext import commands
import requests
import json

client = commands.Bot(command_prefix='.')


def get_pic():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    dog = json_data["message"]
    return dog

def get_breed(breed):
    response = requests.get("https://dog.ceo/api/breed/{0}".format(breed)+"/images/random")
    json_data = json.loads(response.text)
    pic = json_data["message"]
    return(pic)

def get_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    json_data = json.loads(response.text)
    dog_list = []
    for key in json_data["message"]:
        dog_list.append(key)
    return(dog_list)

dog_list = get_list()
dogs = ""
for x in dog_list:
    dogs = dogs + x + "\n"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dog = get_pic()

    if message.content.startswith("pls dog"):
        await message.add_reaction("🐕")
        await message.channel.send(dog)

    if message.content.startswith("pls list"):
        await message.channel.send(dog_list)

    if any( breed in message.content for breed in dog_list):
        breed = message.content
        breed_pic = get_breed(breed)
        await message.channel.send(breed_pic)

    await client.process_commands(message)

@client.command()
async def doglist(ctx):
    embed = discord.Embed(
        title="DOG LIST",
        description=dogs,
        colour=discord.Colour.blue()
    )

    await ctx.send(embed=embed)

client.run(TOKEN)
