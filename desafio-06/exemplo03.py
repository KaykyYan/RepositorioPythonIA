# 3: Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

import requests

cep = input('\nDigite o CEP: ')
resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' in dados:
        print('CEP não encontrado.')
    else:
        print(f"\nLogradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
else:
    print('Erro ao consultar o CEP.')