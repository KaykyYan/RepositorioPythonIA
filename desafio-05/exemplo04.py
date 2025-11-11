# 4: Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias


if __name__ == "__main__":
    print("=== CÁLCULO DE IDADE EM DIAS ===\n")
    ano_nasc = int(input("Digite o ano de nascimento: "))
    idade_dias = calcular_idade_em_dias(ano_nasc)
    print(f"Sua idade aproximada em dias é: {idade_dias} dias\n")
    print("=== FIM ===")
