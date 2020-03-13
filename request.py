"""
Author: Martin Karlsson
Email: mrtn.karlsson@gmail.com
"""
# This file handles requests

import os
import sys

# Todo Move .env file into db
try:
    import requests
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as import_error:
    print(import_error)


# Class for handling weather API calls
# Todo connect with selection of current location
class Weather:
    def __init__(self):
        super().__init__()
        # 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}'
        self.appid = os.getenv('WEATHER_API')
        self.q = 'Stockholm'
        self.api_call = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(
            self.q, self.appid)
        print(self.api_call)

    def get_weather(self):

        try:
            response = requests.get(self.api_call)
        except Exception as e:
            print('Exception:', e)
        finally:
            if response.ok:
                print('Status: {}\nResponse:\n{}'.format(
                    response.status_code, response.text))


if __name__ == '__main__':
    print(__name__)
    weather = Weather()
    weather.get_weather()
