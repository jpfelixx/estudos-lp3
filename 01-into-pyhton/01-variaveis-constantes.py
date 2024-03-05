#identificadores nomes de variáveis, funções. São Case sensitive

nome = "jotas e emes"
speed = 10.2
love = False

#python não tem constante, é expresso por letra maiúscula. Porém , mesmo assim, o valor da constante pode ser modificado
PI = 3.1459
#comentário de uma linha 

'''
comentário de mais uma linha


'''
#docstring ->documentar código de funções, classes etc
def somar(numero , valor):

    '''
    Função que soma 2 números
    paramêtro1: numero
    paramêtro: valor
    return: retorna a multiplicação dos 2 números
    '''
    return numero*valor


                   #####chamadas#####
#somar("joao", 33542) # não da erro visível no documento
somar (10,2345)

## Js e pyhton são dinâmicos, ou seja, não precisam de tipo

