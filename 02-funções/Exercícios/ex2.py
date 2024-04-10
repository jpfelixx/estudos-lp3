# Ex2- Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
n = int(input("digite um número: "))
def tabuada(n):
    for i in range(0, 11):
        result = n* i
        print(f'{n} x {i} = {result}')
        
tabuada(n)
