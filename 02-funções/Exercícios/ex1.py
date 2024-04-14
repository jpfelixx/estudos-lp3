#Ex01 - Jogo de Adivinhação Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu
#aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
import random
def jogo_advinhar(number, numero_aleatorio):
    if number == numero_aleatorio:
        return 1
    elif number < numero_aleatorio:
        return 2
    else:
        return 3

numero_aleatorio = random.randint(0, 100)
while True:
    number = int(input("Digite um valor entre 0 a 100: "))
    v = jogo_advinhar(number, numero_aleatorio)
    if v == 1:
        print("Acertou!!")
        break
    elif v == 2:
        print("Tente novamente! Chute um valor mais alto!!")
    else:
        print("Tente novamente! Chute um valor mais baixo!!")

      
  