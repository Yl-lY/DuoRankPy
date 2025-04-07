from dotenv import load_dotenv
import requests
import os
import database as db

load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Authorization": f"Bearer {os.getenv("JWL_TOKEN")}"
}

bandeiras = {
        'Spanish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/59a90a2cedd48b751a8fd22014768fd7.svg',
        'French': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/482fda142ee4abd728ebf4ccce5d3307.svg',
        'Japanese': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/edea4fa18ff3e7d8c0282de3f102aaed.svg',
        'German': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/c71db846ffab7e0a74bc6971e34ad82e.svg',
        'Korean': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/ec5835ac9f465ff3dad4b1b8725d4314.svg',
        'Italian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/635a09df9323279d39934a991edd4510.svg',
        'Chinese': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/9905aa3a86fcb9e351b0b3bfaf04d8b9.svg',
        'Hindi': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/73837fa39dbf1bcc4c95a17a58ed0ffb.svg',
        'Russian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/eadd7804652170c33814a89482f1f353.svg',
        'Arabic': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/9ab6930a263c981b57f9d578ac97cae7.svg',
        'Portuguese': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/27d253ae1272917fc9f4a79459aacd53.svg',
        'English': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/bbe17e16aa4a106032d8e3521eaed13e.svg',
        'Turkish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/bc80a9518cd6d5af6ae14e8b22b8a1f4.svg',
        'Dutch': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/de945d789e249dcd74333a6996472ef8.svg',
        'Greek': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/8db373482261397a3159d3f370eed2f3.svg',
        'Vietnamese': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/2b077d42185bc45d4896ed55f15c4fea.svg',
        'Polish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/f095084e6ec400e631d62c3d95fefaa2.svg',
        'Swedish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/f578430c9b7ab617c107893afbb501c0.svg',
        'Latin': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/f7cee6cc09270371b097129faf792c2a.svg',
        'Irish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/ef0bfb96037b127473bd7bcbfde1a6ed.svg',
        'Norwegian (Bokmål)': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/90b37d97edc66e830dc2286279548f67.svg',
        'Hebrew': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/f818f545a703ddaa046ca8786e781742.svg',
        'High Valyrian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/2880099b038848abbfd11104097953ad.svg',
        'Ukrainian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/7c6e12bc57527843082f7f5bb77c9862.svg',
        'Idonesian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/339c0413e542f19b234971d7740447e7.svg',
        'Romanian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/357e13bb10cf86fc06552d563957e2e6.svg',
        'Finnish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/b4d0e4f6451f504e1441eb93efdbea5e.svg',
        'Danish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/6af84a7cb8e99ea8a567c2b9c55b9926.svg',
        'Czech': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/828bf0fea457d3beaaab3d6c0bfcc975.svg',
        'Zulu': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/112e1531d0ac198a9424bd1b0a7166e6.svg',
        'Hawaiian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/312e21f793c555787d01a45e20ee8191.svg',
        'Welsh': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/f773f1b240623072e48843ecdf90d756.svg',
        'Swahili': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/335311988405b4354e1b6ae9037c02db.svg',
        'Hungarian': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/2ed8d0a73eab3c9cba0290e2b459684a.svg',
        'Scottish Gaelic': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/09eba3135efe8fe93a4662dba813b921.svg',
        'Haitian Creole': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/8cb302b44c183c1a8ec3b90caf90d922.svg',
        'Esperanto': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/6de7e4731b2a82a6458268e1a3d67ce4.svg',
        'Klingon': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/76d654213a8282b0ebc25b4f535ee003.svg',
        'Navajo': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/bbc8ad0cfe2596d5193376ebdc3e969c.svg',
        'Yiddish': 'https://d35aaqx5ub95lt.cloudfront.net/vendor/55bad151fa6a8d9e2376fc9697c671c8.svg'
    }

def get_bandeira(x):
    # Essa função não tá fazendo nada, mas to com medo de tirar, então vai ficar aqui
    return bandeiras[x]

def collect_languages():
    linguas = []
    response = requests.get(f'https://www.duolingo.com/api/1/courses/list?_=1740862940188', headers=headers).json()

    for i in response:
        if i['from_language_name'] != "English":
            continue
        linguas.append(i['learning_language_name'])

    return linguas



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

def insert_competitor(user, lang):
    data = collect_user_data(user)

    if data == None:
        return None
    
    if lang == None:
        return ''

    display_name = data['fullname']
    avatar_url = 'https:' + data['avatar'] + '/xlarge'
    xp = '0'
    streak = data['site_streak']
    icon_language = get_bandeira(lang)

    for i in data['languages']:
        if i['learning'] == False:
            continue
        if i['language_string'] == lang:
            xp = i['points']
            break

    already_in_list = db.get_competitor(user).data

    if not already_in_list:
        db.post_competitor({
            "name" : user,
            "avatar": avatar_url,
            "display_name" : display_name,
            "flag" : icon_language,
            "language" : lang,
            "xp" : xp,
            "streak" : streak
        })

        return True

    return False

def get_competitors():
    response = db.get_competitors().data
    return response

def atualizar_rank():
    competitors = get_competitors()
    for competitor in competitors:
        data = collect_user_data(competitor['name'])
        for i in data['languages']:
            if i['language_string'] == competitor['language']:
                competitor['xp'] = int(i['points'])
                competitor['streak'] = int(data['last_streak']['length'])

    for competitor in competitors:
        db.update_competitor(competitor)