from packages.calculos.fatorial import Peae

class Help(Peae):
    def __init__(self):
        pass
    
    def Peae(self):
        print("A classe Peae aceita 3 parâmetros:")
        print("")
        print("Quantidade: representa a quantidade de itens a serem permutados")
        print("")
        print("Grupo: representa o tamanho do conjunto de itens nas operações de permutação e combinação")
        print("")
        print("Repetição: controla se a operação a ser executada em permutar_em_grupos será uma permutação")
        print("ou uma combinação")

    def fatorial(self):
        print("A função fatorial usará a variável quantidade para fazer a operação fatorial")

    def permutar_em_grupos(self):
        print("A função permutar_em_grupo efetuará a operação de permutação se repeticao = True,")
        print("e efetuará a operação de combinação se repeticao = False")
    

ajuda = Help()