import discord
import requests
import json

client = discord.Client()

def get_pic():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    dog = json_data["message"]
    return(dog)

def get_breed(breed):
    response = requests.get("https://dog.ceo/api/breed/{0}".format(breed)+"/images/random")
    json_data = json.loads(response.text)
    pic = json_data["message"]
    return(pic)

def get_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    json_data = json.loads(response.text)
    dog_list=[]
    for key in json_data["message"]:
        dog_list.append(key)
    return(dog_list)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dog = get_pic()
    dog_list = get_list()
    if message.content.startswith("pls dog"):
        await message.add_reaction("🐕")
        await message.channel.send(dog)

    if message.content.startswith("pls list"):
        await message.channel.send(dog_list)

    if any( breed in message.content for breed in dog_list):
        breed = message.content
        breed_pic = get_breed(breed)
        await message.channel.send(breed_pic)

client.run("token")

