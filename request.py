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
    # Expected
    print(import_error.__class__.__name__ + ': {}'.format(import_error))
except Exception as imp_exception:
    # Unexpected
    print(imp_exception, False)
    print(imp_exception.__class__.__name__ + ': {}'.format(imp_exception))


# Class for handling weather API calls
# Todo connect with select current location
class Weather:
    def __init__(self):
        super().__init__()
        # 'api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}'
        self.api_key = os.getenv('WEATHER_API')
        self.city = 'Stockholm'
        self.api_call = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(
            self.city, self.api_key)
        print(self.api_call)

    def get_weather(self):
        # Current weather Stockholm
        try:
            response = requests.get(self.api_call)
            if response.ok:
                print('Status Code: {}\nResponse:\n{}'.format(response.status_code, response.json()))
        except requests.exceptions as req_error:
            print('Exception:', req_error)


def main():
    print(sys.version)
    print('File is: {}'.format(__name__))


if __name__ == '__main__':
    main()
