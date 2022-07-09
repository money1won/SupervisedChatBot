# Import the necessary modules!
from command_requests.request_base import RequestBase
import pywttr
import requests

def retrieve_weather(city):
    try:
        # Input the city name
        # city = input('Enter City name: ')

        # Or you can also hard-code the value
        # city = 'Irkutsk'

        # Display the message
        print('Displaying Weater report for: ' + city)

        # Fetch the weater details
        url = 'https://wttr.in/{}'.format(city) # Use of format to pass city as a parameter here
        res = requests.get(url)                 # Make use of the requests module

        # Display the result
        # Resultant data is stored in res.
        # Use of the text method to extract our desired weather details to display the result
        print(res.text)
    except:
        print("Cannot obtain weather")


class SimpleWeatherRequest(RequestBase):
    def __init__(self):
        super().__init__()

    def execute(self, string=""):
        try:
            city = string
            # Input the city name
            # city = input('Enter City name: ')

            # Or you can also hard-code the value
            # city = 'Irkutsk'

            # Display the message
            print('Displaying Weater report for: ' + city)

            # Fetch the weater details
            url = 'https://wttr.in/{}'.format(city)  # Use of format to pass city as a parameter here
            res = requests.get(url)  # Make use of the requests module

            # res.text.translate({ord(i): None for i in 'Follow @igor_chubin for wttr.in updates'})

            # Display the result
            # Resultant data is stored in res.
            # Use of the text method to extract our desired weather details to display the result
            print(res.text)
        except:
            print("Unable to obtain weather report")
