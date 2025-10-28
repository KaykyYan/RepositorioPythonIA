# 4- Calculadora de Preço Total
# Desenvolva um programa que calcule o preço total de uma compra.
# Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3 
# O programa deve calcular o preço total e exibir todas 
# as informações, incluindo o resultado final.

produto = "Cadeira Infantil";
preco = 12.40;
qtd = 3

resultado = preco * qtd;

print(f'Produto: {produto}')
print(f'Preço Unitário: R$ {preco:.2f}') 
print(f'Quantidade: {qtd}')
print(f'Preço Total: R$ {resultado:.2f}')