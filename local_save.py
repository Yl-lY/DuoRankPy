import csv
import functions as func
import os

local_save = 'rank_competitors.csv'
exist = os.path.isfile(local_save)

def atualizar_rank():
    with open('rank_competidores.csv', 'w', newline='') as arquivo:
        ...

def adicionar_na_lista(user, lang):
    data = func.collect_user_data(user)

    if data == None:
        print(f'Usuário {user} não encontrado')
        return False
    
    display_name = data['fullname']
    avatar_url = 'https:' + data['avatar'] + '/xlarge'
    xp = '0'

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
        with open('rank_competidores.csv', 'a') as arquivo:
            csv_writer = csv.writer(arquivo, delimiter=';')
            if not exist:
                csv_writer.writerow(["Nome", "Avatar", "Display Name", "Lingua", "XP"])
            csv_writer.writerow([user, avatar_url, display_name, lang, xp])
        return True
    
    return False

def pegar_competidores():
    lista_competidores = {}
    with open('rank_competidores.csv', 'r') as arquivo:
        csv_writer = csv.reader(arquivo, delimiter=';')
        for item in csv_writer:
            if item[0] == "Nome":
                continue
            lista_competidores[item[0]] = item[3]

    return lista_competidores