# 4- Conversor de Temperatura 

# Crie um programa que converta temperaturas entre Celsius,
# Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem 
# e a unidade para qual deseja converter.

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f'Fahrenheit = {fahrenheit:.2f}')
print(f'Kelvin = {kelvin:.2f}')
