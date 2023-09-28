# api.py
import requests
from config import APP_ID

BASE_URL = 'https://dummyapi.io/data/v1/'

def fetch_users_data():
    headers = {'app-id': APP_ID}
    response = requests.get(BASE_URL + 'user', headers=headers)
    return response.json()['data']

def fetch_posts_data(user_id):
    headers = {'app-id': APP_ID}
    response = requests.get(BASE_URL + f'user/{user_id}/post', headers=headers)
    return response.json()['data']
