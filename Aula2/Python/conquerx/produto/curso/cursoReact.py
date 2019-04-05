from .cursoBase import CursoBase


class CursoReact(CursoBase):
    def __init__(self, cidade, local, data, freq, preco):
        super().__init__('React', cidade, local, data, freq, preco)
        self.variavel_exclusiva = 'material 1,2,3'