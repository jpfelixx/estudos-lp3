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
    print('tu é uma kidv,ai cume terra')
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