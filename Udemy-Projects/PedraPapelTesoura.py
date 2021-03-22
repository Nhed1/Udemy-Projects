import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
imagens = [pedra, papel, tesoura]

print("PEDRA PAPEL TESOURA")
user = int(input("Regras:\n0 - pedra\n1 - papel\n2 - tesoura\n> "))

if (user >= 0) and (user < 3):   # o if aqui serve para não mostrar as imagens caso o número for errado
    print(imagens[user])    # Puxar uma imagem da lista
    pc = random.randint(0,2)
    print("Computador escolheu:")
    print(imagens[pc])

if user < 0 or user > 2:
    print("Isso não é uma opção")
elif user == 0 and pc == 2:
    print("Você ganhou")
elif user == 2 and pc == 0:
    print("Você perdeu")
elif user > pc:
    print("Você ganhou!")
elif pc > user:
    print("Você perdeu!")
else:
    print("Empate")



