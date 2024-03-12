#12/03/2024

# 1. Operadores aritméticos
 # +,-,/,*,%.    **->potência

n1 = 10
n2 = 10
n3 = 9.9

m = (n1+n2+n3) / 3
#print(m)

numero = 10
numero = numero ** 3
print(numero)

## 2. Operadores Lógicos
 #and, or, not

print(True and False)
print(False and False)
print(True or  True)
print(True or  False)

false = False and False
false = False or True # - retorna true


'''
Exemplo:

permite a entrada no sistema
usuário não bloqueado E
usuário não é funcionário E
hora atual entre 8h e 18h

'''
# caso seja adm pode acessar de qualquer forma

usuario_bloqueado = False
usuario_funcionario = True
hora = 22
usuerAdm  = True

funcionario_ativo = usuario_funcionario and not usuario_bloqueado
horario_comercial = hora >=8 and hora <=18

if( funcionario_ativo and horario_comercial)or usuerAdm:
     print('acesso liberado')
else:
      print('acesso negado')



      def dentro_do_horario(hora):
            return hora>= 8 and hora<=18
      
#  3. Operadores de comparação
# == , != ,> ,<, >=, <=
nota1 = 10
nota2 = 5.5

if(nota1>nota2):
      print('aluno foi melhor na prova 1')
else: 
     print('aluno foi melhor na prova 2')

# 4. Operador is, is not
'''
Comparar se os objs são os mesmo -> mesmo espaço de memória

'''
a = [1,2,3]
b = [1,2,3]

print(a == b) #mesmos valores, true
print(a is b) #false
c = b
print(c is b) #true, é uma espécie de ponteiro devido a declaração(c = b)  anterior


#Operador in, not in
#usado para verficar se um elemento existe em uma sequência
opcoes =  ('sim','não','talvez')
opcao = input("digite uma opcão")
## experiência do usuário, caso ele seja um macaco e digite um sim de maneira errônea
opcao = opcao.lower().strip() #strip: tira os espaços

#cascateamento de funções
# ' SiM'
# ' sim'
# 'sim'

opcoes = {
'sim' : ['sim','s','y'],
'nao' : ['nao','n','not']
}

if opcao in opcoes:
    print('ok')

else:
     print('inválido')
 














