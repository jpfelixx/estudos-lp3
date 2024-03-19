
#Aplicação de Descontos

valorinical = float(input('Digite o valor da compra '))
valorfinal = 0 

if(valorinical >= 0.01 and valorinical<=9.9):
    valorfinal = valorinical
    print("O valor final da compra é ",valorfinal)

elif(valorinical>= 10.0 and valorinical<=99.9):
    valorfinal = valorinical-(0.05*valorinical)
    print("O valor final da compra com desconto de 5% é ",valorfinal)

elif(valorinical>= 100.0 and valorinical<=499.9):
    valorfinal = valorinical-(0.10*valorinical)
    print("O valor final da compra com desconto de 10% é ",valorfinal)

else:
    valorfinal = valorinical-(0.15*valorinical)
    print("O valor final da compra com desconto de 15% é ",valorfinal)




