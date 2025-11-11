# 3: Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
# Permitir que o usuário informe o preço do produto e o percentual de desconto.
# Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> float:
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)


if __name__ == "__main__":
    print("=== CÁLCULO DE DESCONTO ===\n")
    preco = float(input("Digite o preço original do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))
    preco_final = calcular_preco_com_desconto(preco, desconto)
    print(f"Preço final com desconto: R$ {preco_final:.2f}\n")
    print("=== FIM ===")
