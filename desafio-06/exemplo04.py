# 4: Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.

import requests

moeda = input('\nDigite o código da moeda (ex: USD, EUR, GBP): ').upper()
resposta = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL')
if resposta.status_code == 200:
    chave = f'{moeda}BRL'
    dados = resposta.json().get(chave)
    if dados:
        print(f"\nCotação atual de {moeda}/BRL:")
        print(f"Valor atual: R$ {dados['bid']}")
        print(f"Máximo: R$ {dados['high']}")
        print(f"Mínimo: R$ {dados['low']}")
        print(f"Data e hora da atualização: {dados['create_date']}")
    else:
        print('Moeda não encontrada.')
else:
    print('Erro ao consultar cotação.')