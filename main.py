import requests
import random

countries = requests.get('https://flagcdn.com/en/codes.json').json()
country_names = list(countries.values())
country_codes = list(countries.keys())
country_name = random.choice(country_names)
country_code = random.choice(country_codes)
print(country_code)

# flag
flag  = requests.get(f'https://flagcdn.com/256x192/{country_code}.png')
# print(flag.status_code)
with open(f'flag.png', 'wb') as f:
    f.write(flag.content)

# guess the country
print("Guess the country")
guess = input("Enter the country: ")
if guess == country_name:
    print("Correct!")
else:
    print(f"Incorrect! The country was {country_name}")