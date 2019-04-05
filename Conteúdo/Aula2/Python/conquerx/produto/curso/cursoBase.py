class CursoBase(object):
    
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
    
    def _funcaoEscondida(self):
        """
        Funcão que não aparecerá no help dos programas. Mas ela pode ser acessada. Ela é "fake" escondida 
        """
        print("Funcao escondida")
        
    def funcaoNormal(self):
        """
        Funcão normal
        """
        print("Funcao normalzinha, básica")