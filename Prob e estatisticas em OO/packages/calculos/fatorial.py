class Peae:
    def __init__(self, quantidade: int, grupo: int = 1, repeticao: bool = True):
        if not isinstance(quantidade, int):
            raise ValueError(f"'Quantidade' é esperada em int, mas recebida em {type(quantidade)}")
        elif not isinstance(grupo, int):
            raise ValueError(f"'Grupo'é esperada em int, mas recebida em {type(grupo)}")
        elif not isinstance(repeticao, bool):
            raise ValueError(f"'Repetição' é esperada em bool, mas recebida em {type(repeticao)}")
        
        elif quantidade < 0 or grupo < 0:
            raise ValueError("Valores não podem ser negativos")
        else:
            self.quantidade = quantidade
            self.grupo = grupo
            self.repeticao = repeticao


        
        
        
        
    def fatorial(self, _grupos = False): 
        produto = 1
        valor = self.quantidade
        if valor == 0:
            return int(1)

        if not _grupos:
            if valor > 0:
                while valor > 1:
                    produto *= valor
                    valor -= 1
                return int(produto)
            else: 
                print("valor inválido")
                produto = 0
       
        else:
            if valor > 0:
                for z in range(self.grupo):
                    produto *= valor
                    valor -= 1
                return int(produto)
            else: 
                print("valor inválido")
                produto = 0

    def permutar_em_grupos(self):
        if not self.repeticao:
            repetido = Peae(quantidade = self.grupo)
            permutacao_sem_repeticao = self.fatorial(_grupos = True) / repetido.fatorial()
            return int(permutacao_sem_repeticao)
        else:
            return self.fatorial(_grupos = True)

        
