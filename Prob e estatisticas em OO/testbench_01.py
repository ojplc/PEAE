from packages.calculos.fatorial import Peae
from packages.calculos.help import ajuda

ajuda.fatorial()

calculo_true = Peae(quantidade = 5, grupo = 3, repeticao = True)
print(calculo_true.fatorial())
print(calculo_true.permutar_em_grupos())

calculo_false = Peae(quantidade = 5, grupo = 3, repeticao = False)
print(calculo_false.fatorial())
print(calculo_false.permutar_em_grupos())

