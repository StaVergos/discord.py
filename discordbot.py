import discord
import random
import sys


client = discord.Client()
random_greeting = ["Hello", "Hi", "YO!", "Sup!"]
random_answer = ["Maybe", "Try again later", "Sure", "Definitely", "I doubt that", "Yes", "No", "No chance for that to happen"]



@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    '''
    Use this if you want to find the id of a custom emoji so you can use it as an reaction
    for emoji in client.emojis:
        print(emoji.id)
        print(emoji.name)'''



@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    
    if message.author == client.user:
        return
    
    if "hello" in message.content.lower():
        await message.channel.send(random.choice(random_greeting))

    if "happy birthday" in message.content.lower():
        await message.channel.send("Happy Birthday!")

    if "!byebot" in message.content.lower():
        await client.close()
        sys.exit()

    if "!tellmebot" in message.content.lower():
        await message.channel.send(random.choice(random_answer))

    '''if "trigger" in message.content.lower():
        emoji = client.get_emoji(emojiid)
        await message.add_reaction(emoji)'''

    

client.run("your token goes here")