#Ex07 -  Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta ( o usuário não vê ) e o 
# usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
def entrada():
    opc = input("|Digite 1 para tentar adivinhar uma letra\n|Digite 2 para tentar adivinhar a Palavra\n: ").strip()

    if opc == '1':
        letter = input("Digite uma letra: ").strip()
        if len(letter) == 1 and letter.isalpha():
            return letter.lower()
        else:
            print("Caractere inválido!")
            return entrada()
        
    elif opc == '2':
        frase = input("Digite uma palavra: ").strip()
        if len(frase ) > 1 and frase.isalpha():
            return frase.lower().strip()
        else:
            print("Palavra inválida!")
            return entrada()
    else:
        print("Opção inválida!")
        return entrada()

def forca(word):
    contador = 1
    tentativas =  set()
    vector = ['_']*len(word)
    
    while contador <= 10:
         print("\n")
         print(f"{contador}° tentativa:")
         print(vector)
         letter = entrada()

         if(letter == word ):
             return 'YOU WIN!'
           
         else:
            tentativas.add(letter)
            print("Letras/Palavras que já foram testadas: ", tentativas)
            cont = 0

            for l in word:
                if l == letter:
                    vector[cont]=letter 
                cont+=1  

         if '_' not in vector:
           print(vector)
           return "YOU WIN! Acertou a palavra"
         
         elif contador==10:
            print(vector)
            return "YOU LOST! GAME OVER"
         contador+=1

word = "Abacate"
print(forca(word.lower()))