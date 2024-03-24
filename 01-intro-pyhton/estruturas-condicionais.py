# if 
idade = 10

# if condição
#  código
#  código
#  código

#: Indica que a condição do if acabou

if idade >=18:
    print('maior de idade')



#if else
if idade >=18:
    print('maior de idade')
else:
    print('maior de idade')

    

#if/elif/else

#crianca = 0 - 12
#adolecesnte = 13 a 17
#adulto 18 a 59
#idoso = 60+


if idade <= 12:
    print('tu é uma kid,vai cume terra')
elif idade <=17:
    print('aborrecente')
elif idade <=59:
    print('adulto, vai trabalhar seu CLT')
else:
    print('gilloina')

#EXEMPLO DE IF ANINHADO
email = 'adm@hotmail.com'

senha = "1231"

if email == 'adm@hotmail.com'and senha =='1231':
    print('entrooo =)')
else:
    print('HACKER!')


#Entrada numero

'''
1- Domingos
2- Segunda
3- Terça
4- Quarta
5- Quinta
6- Sexta
7- Saybadu na balayda


n tem switch case em python - match

'''
dia =3 

dias = {

1:'Domingo' ,
2: 'Segunda',
3: 'Terça' ,
4: 'Quarta',
5: 'Quinta',
6: 'Sexta',
7: 'Saybadu na balayda'

}

if dia in dias :
    print(dias[dia])


    #Operador ternário

    idade = 20

    if idade >=18:
        status ='maior de idade'
    else:
        status = 'menor de idade'


status ='Maior de idade' if idade >=18 else 'Menor de idade'
#é utilizado apenas para mudar o valor de uma variável, se tiver mais linhas de código po recomendado é utilizar o IF

#MATH CASE espécie de switch, só que mais poderoso
#é usado para avaliar mais de uma coisa, agrupar cases

dia = 3
match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case _:
        print("inválido") #é o 'default' do match


#imprimir
#1 e 7 - fim de semana
# 2,3 4,5 e 6 -dia

 #| indica que pode ser umas das opções, é uma espécie de or só que não devolve boolean
match dia:
    case 1 | 7:
        print("fim de semana")
    case 2 |3|4|5|6 :
        print("dia útil")
    case _:
        print("inválido") #é o 'default' do match



 
        

