'''
Ex02. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde 
(OMS), crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em
qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o 
indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5          Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00        Obesidade de Classe 3

'''
def calculador_imc(alt, peso):
    imc = peso/pow(alt,2)
    return imc

def grau(imc):
    if(imc<18.5):
        return "Baixo peso"
    elif(imc>=18.5 and imc<=24.9):
        return "Peso normal"
    elif(imc>24.9 and imc<=29.9):
        return "Excesso de peso"
    elif(imc> 29.9 and imc<=34.9):
        return "Obesidade de Classe 1"
    elif(imc>34.9 and imc<=39.9):
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def pesoideal(imc,altura,peso):
    if(imc<18.5):
        return 1
    else:
        return 2