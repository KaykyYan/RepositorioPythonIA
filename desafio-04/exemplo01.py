# O enunciado das atividades estão nos slides da Aula 08.
# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) 
# entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. 
# Siga as especificações abaixo:

# A calculadora deve solicitar ao usuário que insira dois números e uma operação.
# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
# Trate os seguintes erros:
# Entrada inválida (não numérica) para os números
# Divisão por zero
# Operação inválida
# Use try/except para capturar e tratar os erros apropriadamente.
# Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
# Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
# Crie um programa que permita a um professor registrar as notas de uma turma. 
# O programa deve continuar solicitando notas até que o professor digite 'fim'. 
# Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
# No final, deve exibir a média da turma.
# Crie um programa que verifique se uma senha é forte. 
# Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
# O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
# Crie um programa que solicite ao usuário que insira números inteiros. 
# O programa deve continuar solicitando números até que o usuário digite 'fim'. 
# Para cada número inserido, o programa deve informar se é par ou ímpar. 
# Se o usuário inserir algo que não seja um número inteiro, o programa deve
# informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.

while True:
    try:
        operacao = input('Escolha a operação (+, -, *, /): ')
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print('Erro: Divisão por zero não é permitido')
                continue
            resultado = num1 / num2
        else:
            print('Operação inválida. Tente novamente.')
            continue

        print(f'Resultado: {resultado}')
        break

    except ValueError:
        print('Erro: Digite apenas números válidos.')
    