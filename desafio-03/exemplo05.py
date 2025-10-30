# 5- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário
# é bissexto ou não.
# Um ano é bissexto se for divisível por 4, 
# exceto anos centenários (divisíveis por 100) 
# que não são divisíveis por 400.

ano = int(input('Digite o ano: '))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, 'É um ano bissexto.')
else:
    print(ano, 'Não é um ano bissexto.')