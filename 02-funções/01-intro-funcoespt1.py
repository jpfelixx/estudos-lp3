# Funções - entrada, processamento e saída
'''
Temos a declaração e a chamada da função
só pode chamar a função depois de declarar ela

'''
print("olá") #-> função já declarada no python

#sum()assim como o print é uma outra função já declarada

#Declaração
'''

def nome (paramentro1, parametro2):
    return valor

'''
#função sem parâmetro e sem retorno
def imprimir_saudação():
    print("olá juaaão")

#função sem parâmetro e com retorno
def imprimir_saudação1():
    return"olá juaaão"

imprimir_saudação1()
print(imprimir_saudação1())

#função com parâmetro e sem retorno
def imprimir_nome(a):  # a é o parâmetro
    print(f'Nome: {a}')

#função com parâmetro e com retorno
def imprimir_nome2(a):  # a é o parâmetro
    return f'Nome: {a}'


imprimir_nome("Ipanemabrina") #Ipanemabrina é o argumento
print(imprimir_nome2("IpanemaBrina") ) #IpanemaBrina é o argumento



# não existe polimorfismo em Python-> Não tem sobrecarga, Tem Override

'''
Parâmetro -> refencia referida definida na assinatura da função, pode ser acessado no bloco da função
Arguemento -> é o valor ou referência enviada/passada para o parâmetro -> Consquentemente função, argmt só existe qnd voç^chama a função

'''

'''

- Função pura-> não tem efeito colateral , como retornar uma valor -> tem parâmetro e retorno
- Função não pura->  tem efeito colateral , como impimir um valor, d emodo geral limita mais o código

'''

# entrada = [[10,9][9,7][8,9]]
#calcular media - lista de notas - media
#calcular médias - lista de lista de notas - lista de médias


#lista dentro de lista


notas_alunos =  [
  [10.0 , 9.0],
  [10.0 , 9.0],
  [10.0 , 9.0],

]
  



def calcular_media(notas):
    return sum(notas)/len(notas)


def calcular_medias(notas_alunos):
   # medias = []

   # for notas in notas_alunos:

        #medias.append(calcular_media(notas))


    return[calcular_media(notas) for notas in notas_alunos]

print(calcular_medias(notas_alunos))





def nova_saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

print(nova_saudacao(saudacao='bomdia', nome='joao'))
# se eu nomeio um, eu tenho que nomear o outro


#*args (Non-Keyword argument)

def calcular_media(notas):
    return sum(notas)/len(notas)

calcular_media(([10.0,7.0,9.0]))
# e se eu quiser chamar sem ser uma lista?

def calcular_mediass(*notas):
        print(type(notas))
        return sum(notas)/len(notas)

print(calcular_mediass(10.0,9.0))
print(calcular_mediass(10.0,9.0,7.0))


# o asterisco indica que vc pode passar uma quantidade x de argumentos, quantos vc quiser, indica que vc recebe o parêmetro como tupla