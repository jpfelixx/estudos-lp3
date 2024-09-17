class Pessoa:
    def __init__(self, nome, idade,prontuario):
        self.__nome = nome
        self.__idade = idade
        self.__prontuario = prontuario


    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setIdade(self, idade):
        self.__idade = idade

    def getIdade(self):
        return self.__idade

    def setProntuario(self, prontuario):
        self.__prontuario = prontuario

    def getProntuario(self):
        return self.__prontuario

