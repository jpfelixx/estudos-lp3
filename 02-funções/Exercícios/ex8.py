#Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves
#são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com os textos 
#fornecidos pelo usuário
def retirada_de_nao_alpha(frase, aux):
    for l in frase:  #retira da frase o que não for letra ou espaço
        if l.isalpha() or l == " ":
            aux+=l
    return aux

def contador_de_palavras(frase):
    aux = ""
    dicionario = {}

    aux = retirada_de_nao_alpha(frase, aux)

    aux = aux.split() # Separação da frase em palavras -> "transforma meio que em um vetor"
    for word in aux: # Para cada palavra na frase
        if word not in dicionario: #caso não a palavra não esteja, adiona ela no dicionário
            dicionario[word] = 1
        else:
          dicionario[word]+=1 #caso esteja, o seu value é incrementado

    return dicionario

frase = input("Digite uma frase: ")
print(contador_de_palavras(frase.strip())) #Tira os espaços iniciais




