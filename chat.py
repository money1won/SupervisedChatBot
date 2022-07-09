import json
import torch
# import discord


from model import NeuralNet
from command_requests.math.do_math import SimpleMathRequest
from command_requests.info_search.weather.retrieve_weather import SimpleWeatherRequest
from command_requests.info_search.google.basic_google import SimpleGoogleRequest
from stored.bot_info import Bot
from output.formulate_output import formulate_output
from input.input_interpretation import input_interpretation

# from communication.discord.discord_main import bot_discord_init
# import asyncio
# from discord.ext import commands

import multiprocessing
import threading
import time
import sys
import subprocess







simple_math_request = SimpleMathRequest()
simple_weather_request = SimpleWeatherRequest()
simple_google_request = SimpleGoogleRequest()

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



model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot = Bot()
bot_name = bot.name

print("Let's chat! Type 'quit' to exit")

guess_threshold = 0.75


def type_chat():
    # Interprets the used input and provides the probable word, the tag associated, and the original sentence
    [prob, tag, original_sentence] = input_interpretation(model, tags, all_words, voice='type')

    # Creates an appropriate output for the input from the user
    formulate_output(prob, intents, tag, original_sentence, guess_threshold)


# DON'T CHANGE THIS! Finally figured it out
s1 = subprocess.Popen("python communication\\discord\\discord_main.py")
time.sleep(2)

while True:
    type_chat()
