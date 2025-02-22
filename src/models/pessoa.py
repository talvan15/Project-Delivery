class Pessoa:
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone