from dotenv import load_dotenv
import requests
import os

load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv("JWL_TOKEN")}"
}

def collect_user_data(user_name):
    response = requests.get(f'https://www.duolingo.com/users/{user_name}', headers=headers)
    if response.status_code != 200:
        return None
    
    return response.json()

def collect_user_id(user_name):
    response = requests.get(f"https://www.duolingo.com/users/{user_name}", headers=headers).json()
    user_id = response['avatar'][36:46]

    return user_id

def collect_user_friends(user_id):
    response = requests.get(f"https://www.duolingo.com/2017-06-30/friends/users/{user_id}/followers?pageSize=500&viewerId={user_id}&_={os.getenv("TLS_TOKEN")}", headers=headers).json()
    return response 

def include_competitor_local():
    ...

def get_competitors_local():
    competitors = []
    with open('rank_competidores.csv', 'r') as arquivo:
        for linha in arquivo:
            competitors.append(linha)
    return competitors
# def rank_competitors(competitors):
    
#     return sorted(competitors.items(), key=lambda x: x[1][1], reverse=True)