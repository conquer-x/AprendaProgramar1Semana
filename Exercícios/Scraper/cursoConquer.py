# 
# ConquerX: ConquerX: Introducao a programacao - Python
# Este arquivo define uma classe para guardar as informações de um curso
# retirados de uma página da web
class CursoConquer(object):
    
    def __init__(self, nome, cidade, local, data, freq, preco):
        """
        Inicia os parâmetros necessários
        """
        self.nome = nome
        self.cidade = cidade
        self.local = local
        self.data = data
        self.freq = freq
        self.preco = preco

    def __str__(self):
        """
        Define como será impressa esta classe
        """
        ret = "{} - {} - {} - {} - {} - {}".format(self.nome, self.cidade, self.local, \
               self.data, self.freq, self.preco)
        return ret 

    def __iter__(self):
        """
        Ajuda para converter a classe em dicionário
        """
        return iter(self.__dict__.items())
