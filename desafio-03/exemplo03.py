# 3- Calculadora de IMC

# Desenvolva um programa que calcule o 
# Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura 
# (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo 
# com a tabela padrão de IMC.
# < 18.5: classificacao = "Abaixo do peso" 
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

abaixo_do_peso = 18.5;
peso_normal = 25;
sobrepeso = 30;

resultado = peso / (altura * altura)

if resultado < abaixo_do_peso:
    print(f'Você esta abaixo do peso: {resultado:.2f}')
elif resultado < peso_normal:
    print(f'Você esta no peso normal: {resultado:.2f}')
elif resultado < sobrepeso:    
    print(f'Você esta sobrepeso: {resultado:.2f}')
else:
    print(f'Você está obeso: {resultado:.2f}')