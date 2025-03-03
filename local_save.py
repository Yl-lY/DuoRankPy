import csv
import functions as func
import os

local_save = 'rank_competidores.csv'
exist = os.path.isfile(local_save)
cabecalho = ["Nome", "Avatar", "Display Name", "Bandeira", "Idioma", "XP", "STREAK"]

def adicionar_na_lista(user, lang):
    data = func.collect_user_data(user)

    if lang == None:
        return ''

    if data == None:
        # print(f'Usuário {user} não encontrado, ou língua')
        return None
    
    display_name = data['fullname']
    avatar_url = 'https:' + data['avatar'] + '/xlarge'
    xp = '0'
    streak = data['site_streak']
    icon_language = func.get_bandeira(lang)

    for i in data['languages']:
        if i['learning'] == False:
            continue
        if i['language_string'] == lang:
            xp = i['points']
            break
    
    already_in_list = False

    with open(local_save, 'r') as arquivo:
        csv_writer = csv.reader(arquivo, delimiter=';')
        for line in csv_writer:
            if line[0] == user:
                already_in_list = True
                break
            continue

    if not already_in_list:
        with open('rank_competidores.csv', 'a', newline='') as arquivo:
            csv_writer = csv.writer(arquivo, delimiter=';')
            if not exist:
                csv_writer.writerow(cabecalho)
            csv_writer.writerow([user, avatar_url, display_name, icon_language, lang, xp, streak])
        return True
    
    return False

def pegar_competidores():
    lista_competidores = []
    with open('rank_competidores.csv', 'r') as arquivo:
        csv_writer = csv.reader(arquivo, delimiter=';')
        for item in csv_writer:
            if item[0] == "Nome":
                continue
            lista_competidores.append(item)

    return lista_competidores

def atualizar_rank():
    competitors = pegar_competidores()
    for competitor in competitors:
        data = func.collect_user_data(competitor[0])
        for i in data['languages']:
            if i['language_string'] == competitor[3]:
                competitor[4] = int(i['points'])
                competitor[5] = int(data['last_streak']['length'])

    with open('rank_competidores.csv', 'w', newline='') as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=';')
        csv_writer.writerow(cabecalho)
        for competitor in competitors:
            csv_writer.writerow(competitor)
            