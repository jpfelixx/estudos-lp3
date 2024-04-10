#Ex01 - Jogo de Adivinhação Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu
#aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
import random



def jogo_advinhar(number):
    numero_aleatorio = random.randint()
    if(number==numero_aleatorio):
        return 1
    elif(number<numero_aleatorio):
        return 2
    else:
        return 3
                  

        
    

while True:
    number = int(input("Digite um valor entre 0 a 100: "))
    v = jogo_advinhar(number)
    if(v == 1):
    
    
    
    
  '''
  
  print("acertou!!") 
print("valor mais alto!!") 
print("valor mais alto!!") 
  
  '''  
    

                  

        

while True:
    number = int(input("Digite um valor entre 0 a 100: "))