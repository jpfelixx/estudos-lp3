
def nova_saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

print(nova_saudacao(saudacao='bomdia', nome='joao'))
# se eu nomeio um, eu tenho que nomear o outro

print("olá"," mundo" , sep="hello") # sep é o q aparace entre os espaços

#valores padrão para parâmetro
def nova_saudacao(nome, saudacao="bom dia"):
    return f'{saudacao} {nome}'

def nova_saudacao(nome, saudacao=" moanoite"):
    return f'{saudacao} {nome}'

#simula o overload(sobrescreve) do Java


 #return {
  #   'vogais'
 #}