import requests
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv('TOKEN')

# def get_data():
#     response = requests.get(f'https://api.countrylayer.com/v2/all?access_key={token}')
#     print(response)
#     return response.json()

# def get_flag():
#     data = get_data()
#     # print(data)
#     # print(f'{country["name"]} - {country["flag"]}')

# get_flag()
# print(get_data())

response = requests.get(f'https://api.countrylayer.com/v2/all?access_key={token}').json()

def get_flag():
    for country in response:
        print(f'{country["name"]} - {country["flag"]}')

def get_country():
    for country in response:
        print(f'{country["name"]}')

get_flag()
get_country()