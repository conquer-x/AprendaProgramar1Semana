from conquerx.produto.curso.cursoBase import CursoBase


class CursoIntro(CursoBase):
    def __init__(self, cidade, local, data, freq, preco):
        super().__init__('Introducao a programacao', cidade, local, data, freq, preco)
        self.variavel_exclusiva = 'material 1,2,3'