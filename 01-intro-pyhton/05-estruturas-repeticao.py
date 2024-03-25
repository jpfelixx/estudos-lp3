#for, while
#key words- break,continue

for letra in 'celola broken':
    print(letra)


itens = ['banana','maça','morango'];

for item in itens:
    print(item)

#existem laços de repetição por não saber o número máximo de itens numa lista


#Range - função que recebe 3 valores, start,stop e step - é mais usado para pegar valores específicos, se vc quer ir do início até o fianl -> usar for i
for i in range(5):
    print(i)

print('--------------')


for i in range(10,35,5):
    print(i)

#lista = [0,12,3...40..100]
#liste  range são funções,, list é uma função que lista -> converter coisas para uma lista
#type()-> devolve o tipo da variável
# type(list(range(10)))-> devolve o tipo lista
lista = list(range(101))


#len -> te dá o tamamho da sequencia, de 1 a x

len(' iai bem')

print('--------------')

contador = 0;
while contador <= 5:
    print(contador)
    contador+=1

print('--------------')


numeros = [1,3,16,10,5,7,9,18]

for numero in numeros:
    if numero%2 == 0:
      print(numero)
      break

numeros = [1,3,16,10,5,7,9,18]
for numero in numeros:
    if numero%2 == 1:
      continue  #pula a iteração
    print(numero)



#Compreensão de lista
#Forma concisa de criar listas em pyhton



numeros = [21,2,3,4,5,6,7]
quadrados = []

for numero in numeros:
    quadrados.append(numero**2);



quadrados = [numero ** 2 for numero in numeros]
print(quadrados)


print('--------------')

palavra = 'ola mundo'
lertras = [letra for letra in palavra]
letras = [letra.upper()  for letra in palavra]
print(letras)

numeros = [1,32,3,4,42,18,-10,73]
par = [n for n in numeros if n%2 == 0]
print(par)


