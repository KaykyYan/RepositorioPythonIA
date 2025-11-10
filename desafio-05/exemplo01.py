# Aula 09 - Exercícios de Funções em Python
# Autor: [Seu Nome]
# Descrição: Conjunto de funções para cálculo de gorjeta, verificação de palíndromo,
# cálculo de desconto em produto e idade em dias.


# Função 1 - Calcular Gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor total da conta
    e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): Valor total da conta.
        porcentagem_gorjeta (float): Porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: Valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Função 2 - Verificar Palíndromo
def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços e pontuação.

    Parâmetros:
        texto (str): Palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum())
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Função 3 - Calcular Preço com Desconto
def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o preço final de um produto após aplicar o desconto.

    Parâmetros:
        preco_original (float): Preço original do produto.
        percentual_desconto (float): Percentual de desconto (ex: 10 para 10%).

    Retorna:
        float: Preço final com desconto aplicado.
    """
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)  


# Função 4 - Calcular Idade em Dias
from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.

    Parâmetros:
        ano_nascimento (int): Ano de nascimento da pessoa.

    Retorna:
        int: Idade aproximada em dias.
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  
    return idade_dias


# Programa Principal
if __name__ == "__main__":
    print("=== CÁLCULOS DIVERSOS ===\n")

    # 1. Cálculo da gorjeta
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem de gorjeta desejada (%): "))
    valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}\n")

    # 2. Verificação de palíndromo
    texto_usuario = input("Digite uma palavra ou frase: ")
    resultado = verificar_palindromo(texto_usuario)
    print(f"É palíndromo? {resultado}\n")

    # 3. Cálculo de preço com desconto
    preco = float(input("Digite o preço original do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))
    preco_final = calcular_preco_com_desconto(preco, desconto)
    print(f"Preço final com desconto: R$ {preco_final:.2f}\n")

    # 4. Cálculo da idade em dias
    ano_nasc = int(input("Digite o ano de nascimento: "))
    idade_dias = calcular_idade_em_dias(ano_nasc)
    print(f"Sua idade aproximada em dias é: {idade_dias} dias\n")

    print("=== FIM DO PROGRAMA ===")