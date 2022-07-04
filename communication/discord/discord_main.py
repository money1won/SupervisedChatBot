import discord
import random
from input.input_interpretation import input_interpretation
from output.formulate_output import formulate_output
import asyncio
import json
import torch
import sys
import aiohttp
import time
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from itertools import cycle




TOKEN = "OTkzMjE2Mjk0NTI4NzUzNjg1.GvaXri.sbgoCDRpNTlujH_Gwq8e4damDVRdG0OPPHR9Lc"

client = discord.Client()
client_command = commands.Bot(command_prefix = '!')




device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]

all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']
from model import NeuralNet


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

@client.event
async def on_message(message):
    # username = str(message.author).split('#')[0]
    user_message = str(message.content)
    # channel = str(message.channel.name)
    # print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    # Choose which channels the bot can respond to
    if message.channel.name == 'general':
        [prob, tag, original_sentence] = input_interpretation(model, tags, all_words, user_message.lower(), voice='discord')
        response = formulate_output(prob, intents, tag, original_sentence, discord_message=True)

        await message.channel.send(str(response))


def bot_discord_init():
    client.run(TOKEN)

# client.run(TOKEN)

# def driver(coroutine):
#     try:
#         coroutine.send(None)
#         coroutine.close()
#     except:
#         return

bot_discord_init()

