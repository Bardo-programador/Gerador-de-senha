from random import choice

numero_digitos = int(input("quantos caracteres a senha deve ter?"))
def gerador_de_senha(digitos):
    caracteres_disponiveis = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*-+/"
    senha = ''
    for digitos in range(numero_digitos):
        senha += choice(caracteres_disponiveis)
    print(f"Sua senha é {senha}")
    
gerador_de_senha(numero_digitos)
