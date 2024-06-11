from uteis.modulos1 import volefiltro, potencia

comprimento = float(input("Digite o comprimento do aquário: "))
altura = float(input("Digite a altura do aquário: "))
largura = float(input("Digite a largura do aquário: "))
altura = float(input("Digite a temperatura ambiente: "))
largura = float(input("Digite a temperatura desejada n aquário: "))

data  = volefiltro(comprimento,altura,largura)
print("O volume do aquário em litros é: ",data[0])
print("A quantidade em litros de filtragem por hora necessária para manter a qualidade da água é: ",data[1])
print("A potencia do do termostato é: ",potencia(data[0],25.0,18,))




