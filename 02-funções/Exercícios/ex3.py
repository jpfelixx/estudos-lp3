#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para 
#digitar uma frase e retorne o número de vogais e consoantes na frase.

letras = {
    'vogais': 0 ,
    'consoantes' : 0,
}

def contador(frase):
    for letter in frase:
        if letter in 'aeiou':
            letras['vogais']+=1
        else:
            letras['consoantes']+=1
     
frase = input("Digite uma frase: ")
frase = frase.replace(" ","").lower() 
contador(frase)

print("o número de vogais da palvara é: " ,letras['vogais'])
print("o número de consoantes da palvara é: " ,letras['consoantes'])