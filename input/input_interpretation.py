import torch
from nltk_utils import bag_of_words, tokenize
from speech_to_text import speech_input


def input_interpretation(model, tags, all_words, discord_message="", voice='voice'):
    input_method_voice = voice
    sentence = ""
    if input_method_voice == 'voice':
        sentence = speech_input()
        print(f"You: {sentence}")  # Voice based input
    elif voice == 'discord':
        sentence = discord_message
    elif voice == 'type':
        sentence = input('You: ')  # Text based input
    elif sentence == 'quit':
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