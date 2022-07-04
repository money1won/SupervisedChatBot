import random

from command_requests.math.do_math import SimpleMathRequest
from command_requests.info_search.weather.retrieve_weather import SimpleWeatherRequest
from command_requests.info_search.google.basic_google import SimpleGoogleRequest
from text_to_speech import speak

from output.log_output import console_output
from stored.bot_info import response_keywords

from stored.bot_info import name

simple_math_request = SimpleMathRequest()
simple_weather_request = SimpleWeatherRequest()
simple_google_request = SimpleGoogleRequest()

bot_name = name


def formulate_output(prob, intents, tag, original_sentence, guess_threshold=0.75, discord_message=False):
    response = ''
    voice_response_req = True
    console_output_req = True
    if prob.item() > guess_threshold:
        for intent in intents['intents']:
            if tag == intent['tag']:
                if discord_message:
                    voice_response_req = False
                    console_output_req = False
                else:
                    pass
                # This portion is specifically for conversational purposes

                response = random.choice(intent['responses'])

                # todo: use {VARIABLE_NAME} in the corpus to identify changeable variables. Must update in bot info too
                if any(character in response for character in ["{", "}"]):
                    response_keyword = response[response.find("{") + 1: response.find("}")]
                    response_keyword = response_keyword.lower()
                    response = response.replace(response[response.find("{"): response.find("}") + 1],
                                                response_keywords[response_keyword])

                # Any data involved commands can go down here

                if tag == "introduction":
                    response = f"My name is {bot_name}"

                if tag == "request":
                    print("request has been made")

                if tag == "math":
                    # output = do_math(original_sentence)
                    # print(output)
                    # speak(output)
                    response = simple_math_request.execute(original_sentence)

                if tag == "stock_check":
                    pass

                if tag == "weather":
                    console_output(simple_weather_request.execute("Belton"))

                if tag == "query":
                    response = simple_google_request.execute(original_sentence)

    else:
        response = "I do not understand"

    if not discord_message:
        console_output(response)
        speak(response)

    return response
