#Ex04 - Simulador 'de Eleições': Crie um programa que simule uma votação com 
#três candidatos. O programa deve pedir ao usuário para votar várias vezes e,
#no final, mostrar o número de votos de cada candidato e quem foi o vencedor.

candidatos = {

    'candidato_1': 0 ,
    'candidato_2': 0 ,
    'candidato_3': 0 ,
    
}


def votação(n):
    
     while n > 0 : 
           print(" vote: 1 - candidato | 2- candidato | 3 - candidato  ")
           voto = int(input("digite o código correspondente ao candidato: "))
           if(voto == 1):
               candidatos['candidato_1']+=1
           elif(voto == 2):
               candidatos['candidato_2']+=1
           elif(voto == 3):
               candidatos['candidato_3']+=1
           n-=1
      
     n = candidatos[max(candidatos, key=candidatos.get)] 
     ca =  max(candidatos, key=candidatos.get)
     print(f'o candidato que mais teve votos foi o: {ca}  com {n} votos'  )
     print(candidatos)


n  = int(input("Digite o número de vezes que deseja votar "))

votação(n)