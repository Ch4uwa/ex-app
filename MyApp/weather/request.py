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

except ImportError as import_error:
    # Expected
    print(import_error.__class__.__name__ + ': {}'.format(import_error))
except Exception as imp_exception:
    # Unexpected
    print(imp_exception, False)
    print(imp_exception.__class__.__name__ + ': {}'.format(imp_exception))
else:
    load_dotenv()


# Class for handling weather API calls
# Todo connect with select current location
class Weather:
    def __init__(self, city='Stockholm'):
        self.api_key = os.getenv('WEATHER_API')
        self.city = city

        # 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}'
        self.api_call = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(
            self.city, self.api_key)

    def get_weather(self):
        # Current weather Stockholm
        try:
            response = requests.get(self.api_call)
        except requests.exceptions as req_error:
            print('Exception:', req_error)
        else:
            print('Status Code: {}\nResponse:\n{}'.format(response.status_code, response.json()))


def run():
    pass


if __name__ == '__main__':
    print('Executing as main')
    print('__name__ ==', __name__)
    run()
else:
    print('Executing module: ', __name__)
