'''
Main
'''
import matematica #Tudo do módulo vai estar sendo importado -> from matematica import*, mas da primeira maneira eu preciso referenciar o arquivo módulo
from matematica import PI as PI_MAT , somar #maneira mais adequada de importar, mostra exatamente o que está sendo utilizado
# PI_MAT está renomeando o PI do módulo matemática
#quando importa dessa maneira vc não precisa colocar o "matemática"/modulo na frente(Matemnática.pi), vc tem acesso direto a ela
"ex:"

print("---")
print(PI_MAT)
print("---")

print(matematica.PI) #acessa coisas mais especificas a partir do .
print(matematica.subtrair(10,1))

# from matemática import somar as SUM

# Estatistica é o pacote geral; descritiva e inferencial são os módulos
from estatistica.descritiva import maximo  
from estatistica.inferencial import VALOR

print(maximo([20,9,220]))