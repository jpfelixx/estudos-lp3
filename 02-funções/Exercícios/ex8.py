#Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como 
#argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores
#são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes
#textos fornecidos pelo usuário
#- usar função update

def contador_de_palavras(frase):
    dicionario = {}
    frase = frase.split()
    for word in frase:
       i = 0
       if word not in dicionario:
            i+=1
            dicionario[word] = i
       else:
            i+=1
            dicionario[word] = i
           

  


    








frase = input("Digite uma frase")
print(contador_de_palavras(frase.strip()))
