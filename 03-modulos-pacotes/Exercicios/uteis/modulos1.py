'''
Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
'''

def  volefiltro (comprimento,altura,largura):
    volume = (comprimento*altura*largura)/1000.0
    data = [volume,volume*3]
    return data

def potencia(volume, temdesejada, tempambiente):
    pot =  round(volume*0.05*(temdesejada  - tempambiente),2)
    return pot
