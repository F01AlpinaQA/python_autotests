import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a8ff9ff643aeb205b46bf979030f9ca'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "7318"

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params = {"trainer_id": TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Stan Lee'

