# 5- Calculadora de Soma com Entrada do Usuário

# Leia 2 valores inteiros e armazene-os nas variáveis A e B. 
# Efetue a soma de A e B, atribuindo o seu resultado à variável X. 
# Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 
# Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.

valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

soma = valor1 + valor2;

print(f"\nPrimeiro número digitado: {valor1}")
print(f"Segundo número digitado: {valor2}")
print(f"X = {soma}")
