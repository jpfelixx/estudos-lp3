#tipos:

#1. Numérico
 #int, float, complex,

 #int 
idade = 10
heat = -10
#float
minhapacienciia = -0.001


#2. Bool
wasIsilly= True
doIwantRevange = True

# 3. Strings
Nome ="Divanilda"
name ='nhai'
 

 #multilinhas = mantêm formatação da string

frse = """" OLá world,
td bem
lala
"""

# interpolação :
nome = "João"
idade = 17
frase = f"OLá { nome }. Você tem  {idade} anos"
print(frase)

#char
letra = 'a'
letter = "b"

#acesso de um caracter da string
#phyton dá para ir de trás para frente em um array-> começa no -1 o último caractere,não 0
nome = "tinaluDivalinda"
print(nome[10])
print(nome[1])
print(nome[-1])
print(nome[3])
print(nome[0:4])

#String em pyhton são objetos
nome.upper() #-> devolve uma string em maiúsculo
print(nome.capitalize())
print(nome.upper())

# 4. Lista em pyhton são objetos
#lista de valores: é indexada e pode ser alterada

habilidades = ['English','encher saco das emes e da jota','Java','HTML','TYSCRIPT','JavaScript','Cobol','CSS','PHP']
print(habilidades[5])

habilidades.append("#c") # inserir no final da lista
print(habilidades)
habilidades.insert(3, 'Juizo') #insere em uma posição específica
print(habilidades)

print(habilidades)

for x in habilidades:
    print(x)
 

def somar(n1, n2):
    return n1*n2
 
somar(10,-1)

somar(n2=10,n1=-193)

#Tuple(Tupla)
#lista de valores que não pode ser alterada(inserir valor ou modificar)(escolhas)
opcoes = ("si","não", "talvez") #parênteses  indica que é tupla

print(opcoes[0])

#set (conjuto)
#conjunto de valores que não permite elementos duplicados. Não é indexado
habilidades = {'pyhton','java', 'c#','java'}
print(habilidades)

# 6. dict (dicionario) -> conjunto de chaves e valores
#espécie de obj de uma classe

#palavra -> definição
#chave -> valor
#key -> value

nome = 'Pedro Alvarez Cabral'
idade = 59
habilidades = ['descobrir o brazil','matar indio','cume']
empregado = 'no'

candidato = {
    'nome': 'Pedro Alvarez Cabral' ,
    'idade' : 59,
    'habilidades':['descobrir o brazil','matar indio','cume'],
    'empregado':'no'

}

print(candidato)


#7 . None
none = None # serve para quando não quiser inicializar a varíavel

#https://wiki.python.org.br/ListaDeExercicios
