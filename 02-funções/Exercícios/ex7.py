#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
#O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra,
#letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

def guess():
    letter = input("Digite uma letra: ")
    return letter.lower()


def forca(word):
    contador = 1
    tentativas =  set()
    vector = [ '_ ']*len(word)
    
    while contador <= 7:
         print(f"{contador}° tentativa:")
         print(vector)
         print('\n')
         letter = guess()
         tentativas.add(letter)

         print("Letras que já foram testadas: ", tentativas)

         cont = 0
         for l in word:
             if l == letter:
                 vector[cont]=letter
             cont+=1
         
         if(vector == word):
             break
        
         contador+=1
              
word = "laranja"
forca(word.lower())