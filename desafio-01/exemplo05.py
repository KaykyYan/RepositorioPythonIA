# 5- Calculadora de Número Inteiro
# Leia quatro valores inteiros A, B, C e D. 
# A seguir, calcule e mostre a diferença do produto de A e B 
# pelo produto de C e D segundo a 
# fórmula: DIFERENCA = (A * B - C * D).
# Entrada: O arquivo de entrada contém 4 valores inteiros. 
# Saída: Imprima a mensagem 
# "DIFERENCA = " com todas as letras maiúsculas.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))

resultado = num1 * num2 - num3 * num4

print(f'DIFERENCA = {resultado}')