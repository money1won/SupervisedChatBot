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

def formulate_output(prob, intents, tag, original_sentence, guess_threshold = 0.75):
    if prob.item() > guess_threshold:
        for intent in intents['intents']:
            if tag == intent['tag']:
                # This portion is specifically for conversational purposes

                response = random.choice(intent['responses'])

                # todo: use {VARIABLE_NAME} in the corpus to identify changeable variables. Must update in bot info too
                if any(character in response for character in ["{", "}"]):
                    response_keyword = response[response.find("{") + 1: response.find("}")]
                    response_keyword = response_keyword.lower()
                    response = response.replace(response[response.find("{"): response.find("}") + 1],
                                                response_keywords[response_keyword])

                console_output(f"{response}")

                speak(response)

                # Any data involved commands can go down here

                if tag == "introduction":
                    output = f"My name is {bot_name}"
                    console_output(output)
                    speak(output)

                if tag == "request":
                    print("request has been made")

                if tag == "math":
                    # output = do_math(original_sentence)
                    # print(output)
                    # speak(output)
                    output = simple_math_request.execute(original_sentence)
                    console_output(output)
                    speak(output)

                if tag == "stock_check":
                    pass

                if tag == "weather":
                    console_output(simple_weather_request.execute("Belton"))

                if tag == "query":
                    response = simple_google_request.execute(original_sentence)
                    console_output(response)
                    speak(response)

    else:
        print(f'{bot_name}: I do not understand...')
        speak("I do not understand...")