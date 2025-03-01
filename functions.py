from dotenv import load_dotenv
import requests
from database import connect_db
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

def include_competitor_db(user_name, language):
    
    data = collect_user_data(user_name)

    if data == None:
        print(f'Usuário {user_name} não encontrado')
        return False

    display_name = data['fullname']
    avatar_url = 'https:' + data['avatar'] + '/xlarge'
    xp = '0'

    for i in data['languages']:
        if i['learning'] == False:
            continue
        if i['language_string'] == language:
            xp = i['points']
            break

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO competitors (username, avatar_url, display_name, language, xp)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (username) DO UPDATE SET xp = EXCLUDED.xp;
    """, (user_name, avatar_url, display_name, language, xp))

    conn.commit()
    conn.close()

    print(f'Usuário {user_name} salvo com sucesso')
    return True

def get_competitors_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT username, avatar_url, display_name, language, xp FROM competitors ORDER BY xp DESC")
    competitors = cursor.fetchall()

    conn.close()
    return competitors
    

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