import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas")
letras_qntd = int(input("Quantas letras você quer na sua senha? "))
numeros_qntd = int(input("Quantos números você quer na sua senha? "))
simbolos_qntd = int(input("Quantos símbolos você quer na sua senha? "))

senha_ordenada = []

for caracter in range(0, letras_qntd):
    senha_ordenada.append(random.choice(letras))

for caracter in range(0, numeros_qntd):
    senha_ordenada.append(random.choice(numeros))

for caracter in range(0, simbolos_qntd):
    senha_ordenada.append(random.choice(simbolos))

senha_aleatoria = ''
random.shuffle(senha_ordenada)   # Embaralhar uma lista

for senha in senha_ordenada:
    senha_aleatoria += senha

print(senha_aleatoria)




