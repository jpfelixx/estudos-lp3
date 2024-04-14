
def nova_saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

print(nova_saudacao(saudacao='bomdia', nome='joao'))
# se eu nomeio um, eu tenho que nomear o outro

print("olá"," mundo" , sep="hello") # sep é o q aparace entre os espaços

#valores padrão para parâmetro
def nova_saudacao(nome, saudacao="bom dia"):
    return f'{saudacao} {nome}'

def nova_saudacao(nome, saudacao=" moanoite"):
    return f'{saudacao} {nome}'

#simula o overload(sobrescreve) do Java


 #return {
  #   'vogais'
 #}


'''
#Ex07 -  Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa
#com uma palavra oculta ( o usuário não vê ) e o usuário tenta adivinhar a palavra, letra 
# por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

def entrada():
    letter = input("Digite uma letra: ")
    if len(letter) == 1 and letter.isalpha():
        return letter.lower()
    else :
        return 0

def loop_de_verficação(letter):
    while letter == 0:
        print("caracter inválido!")
        letter = entrada()
    return letter

def forca(word):
    contador = 1
    tentativas =  set()
    vector = ['_']*len(word)
    
    while contador <= 10:
         print(f"{contador}° tentativa:")
         print(vector)
         print('\n')
         letter = entrada()

         if(letter == 0 ):
            letter = loop_de_verficação(letter)
         tentativas.add(letter)
         print("Letras que já foram testadas: ", tentativas)
         cont = 0

         for l in word:
             if l == letter:
                 vector[cont]=letter 
             cont+=1  

         if '_' not in vector:
           print(vector)
           return "YOU WIN"
         
         elif contador==10:
            print(vector)
            return "YOU LOST! GAME OVER"
         contador+=1

word = "Latorre"
print(forca(word.lower()))
'''
