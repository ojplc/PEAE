from packages.calculos.fatorial import Peae

calculo_true = Peae(quantidade = 5, grupo = 3, repeticao = True)
print(calculo_true.permutar_quantidade())
print(calculo_true.permutar_em_grupos())

calculo_false = Peae(quantidade = 5, grupo = 3, repeticao = False)
print(calculo_false.permutar_quantidade())
print(calculo_false.permutar_em_grupos())

