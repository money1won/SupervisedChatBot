
import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from command_requests.math.do_math import SimpleMathRequest
from command_requests.info_search.weather.retrieve_weather import SimpleWeatherRequest
from command_requests.info_search.google.basic_google import SimpleGoogleRequest
from text_to_speech import speak
from playsound import playsound
from gtts import gTTS
from stored.bot_info import name
from output.log_output import console_output
from stored.bot_info import response_keywords
from speech_to_text import speech_input
from formulate_output import formulate_output

def input_interpretation(model, tags, all_words, voice):
    input_method_voice = voice
    if input_method_voice == True:
        sentence = speech_input()
        print(f"You: {sentence}")  # Voice based input
    else:
        sentence = input('You: ')  # Text based input
    if sentence == 'quit':
        pass

    original_sentence = sentence

    # must first tokenize and get a bag of words
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    return [prob, tag, original_sentence]