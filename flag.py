import requests
import random


def get_countries():
    countries_json = requests.get('https://flagcdn.com/en/codes.json').json()
    all_country_codes = list(countries_json.keys())
    # all_country_names = list(countries_json.values())
    country_codes = random.choices(all_country_codes, k=4)
    # country_names = random.choices(all_country_names, k=4)
    country_names = []
    for code in country_codes:
        country_names.append(countries_json[code])
    # print(country_names)

    return country_names, country_codes

# print(get_countries())
