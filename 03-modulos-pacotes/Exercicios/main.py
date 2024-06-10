from uteis.modulos2 import calculador_imc , grau , pesoideal

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = round(calculador_imc(altura,peso),2)
print("O seu IMC é igual a: " , imc)
print("De acordo com o seu imc, a classificação de seu peso é:",grau(imc))

if(imc<18.5):
    ganhos = (pesoideal(imc,altura,peso))
    print("Voçê deve ganhar no mínimo", ganhos[0] ," kg e no máximo",ganhos[1],"kg")
if(imc>24.9):
    perdas = (pesoideal(imc,altura,peso))
    print("Voçê deve perder no mínimo", perdas[0] ," kg e no máximo",perdas[1],"kg")




