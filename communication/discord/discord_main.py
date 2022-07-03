import discord
import random
from input.input_interpretation import input_interpretation
from output.formulate_output import formulate_output

TOKEN = "OTkzMjE2Mjk0NTI4NzUzNjg1.GvaXri.sbgoCDRpNTlujH_Gwq8e4damDVRdG0OPPHR9Lc"

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # Choose which channels the bot can respond to
    if message.channel.name == 'general':
        if user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == "how are you":
            await message.channel.send(f'Hello {username}, I\'m doing well!')
        else:
            await message.channel.send(f'See you later {username}!')
            return


client.run(TOKEN)

