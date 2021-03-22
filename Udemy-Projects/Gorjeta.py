print("Bem vindo a Calculadora de GORJETA")

conta = float(input("Digite quanto deu a conta: "))
porcentagem = int(input("Qual será a porcentagem da gorjeta(5%, 10%, 12%): "))
pessoas = int(input("Dividido entre quantas pessoas: "))

gorjeta_conta = porcentagem / 100 + 1
gorjeta = conta / pessoas * gorjeta_conta

print(f"Cada pessoa deve pagar R${round(gorjeta,2)} de gorjeta")