# 2: Crie um programa que gera um perfil de usuário aleatório usando a API "Random User Generator". O programa deve exibir o nome, email e país do usuário gerado.

import requests

resposta = requests.get('https://randomuser.me/api/')
if resposta.status_code == 200:
    dados = resposta.json()['results'][0]
    nome = f"{dados['name']['first']} {dados['name']['last']}"
    email = dados['email']
    pais = dados['location']['country']
    print(f'\nUsuário gerado:')
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'País: {pais}')
else:
    print('\nErro ao gerar usuário.')