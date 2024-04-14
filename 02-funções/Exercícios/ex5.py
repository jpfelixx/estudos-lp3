#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma
#palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida 
#de frente para trás e de trás para frente da mesma forma).
# ex: ana
frase = input("Digite uma palavra: ")

def verificador_palindromo(frase):
    f  = frase.replace(" ", "").lower()
    f2 = f[::-1]
   
    if(f == f2):
        return True
    else:
        return False

boolean = verificador_palindromo(frase)
status ='É palídromo' if boolean else 'não é palídromo'
print(status)

