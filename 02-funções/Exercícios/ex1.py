#Ex01 - Jogo de Adivinhação Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu
#aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

# Ex2- Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.


#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para 
#digitar uma frase e retorne o número de vogais e consoantes na frase.

#Ex04 - Simulador 'de Eleições': Crie um programa que simule uma votação com 
#três candidatos. O programa deve pedir ao usuário para votar várias vezes e,
#no final, mostrar o número de votos de cada candidato e quem foi o vencedor.


#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma
#palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida 
#de frente para trás e de trás para frente da mesma forma).
# ex: ana


#Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
#converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

#fonte do padrão de  notas adotado:


#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
#O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra,
#letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

#Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como 
#argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores
#são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes
#textos fornecidos pelo usuário.
import random

def jogo_advinhar(number,numero_aleatorio):
  if(number==numero_aleatorio):
    return 1
  elif(number<numero_aleatorio):
    return 2
  else:
    return 3
                   
numero_aleatorio = random.randint(0,100)
while True:
    number = int(input("Digite um valor entre 0 a 100: "))
    v = jogo_advinhar(number,numero_aleatorio )
    if(v == 1):
      print("acertou!!") 
      break
    elif(v==2):
      print("Tente novamente! chute um valor mais alto!! ") 
    else:
      print("Tente novamente! chute um valor mais baixo!!") 

      
  