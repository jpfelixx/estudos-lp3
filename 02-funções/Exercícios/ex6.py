#Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
#converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
nota = int(input("Digite sua pontuação: "))

def conversor_de_notas(nota):
    if(nota<=100.00 and nota>=90.00):
        return 'A'
    elif(nota<90.00 and nota>=75.00):
        return 'B'
    elif(nota<75.00 and nota>=65.00):
        return 'C'
    elif(nota<65.00 and nota>=60.00):
        return 'D'
    elif(nota<60.00 and nota>=0.00):
        return 'F'
    else:
        return "O valor  não pertence a nenhuma escala! "

print("A sua nota convertida para o padrão de letras é: ",conversor_de_notas(nota))