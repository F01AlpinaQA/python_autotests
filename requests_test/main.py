import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a8ff9ff643aeb205b46bf979030f9ca'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "7318"

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Python",
    "photo_id": "1"
    }

body_rename = {
    "pokemon_id": "116528",
    "name": "Python 2024",
    "photo_id": 1
}

body_add = {
    "pokemon_id": "116528"
}


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


'''response_create = requests.post(url = f'{URL}/pokemons', headers =  HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_rename)
print(response.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_add)
print(response_add.text)