from Exercicios.uteis.modulos2 import calculador_imc , grau 
peso = input(int("Digite o seu peso"))
altura = input(int("Digite a sua altura"))
imc = calculador_imc(altura,peso)
# ideal = pesoideal(imc,altura,peso)
print("O seu IMC é igual a: " , imc)
print("De acordo com o seu imc, a classificação de seu peso é:",grau(imc))


