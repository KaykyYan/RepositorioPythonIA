# 2: Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


if __name__ == "__main__":
    print("=== VERIFICADOR DE PALÍNDROMO ===\n")
    texto_usuario = input("Digite uma palavra ou frase: ")
    resultado = verificar_palindromo(texto_usuario)
    print(f"É palíndromo? {resultado}\n")
    print("=== FIM ===")
