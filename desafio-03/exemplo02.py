# 2- Classificador de Idade

# Crie um programa que solicite a idade do usuário
# e classifique-o
8  # em uma das seguintes categorias:
# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos)
# Idoso (60 anos ou mais).

idade = int(input('Digite a sua idade: '))
crianca = 12
adolecentes = 17
adulto = 18
idoso = 60

if idade <= crianca:
    print(f'Você é uma criança: ({idade} anos)')
elif idade <= adolecentes:
    print(f'Você é uma adolescente: ({idade} anos)')
elif idade <= adulto:
    print(f'Você é uma adulto: ({idade} anos)')
else:
    print(f'Você é uma idoso: ({idade} anos)')
