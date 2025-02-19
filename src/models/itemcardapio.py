class ItemCardapio:
    def __init__(self, nome, preco, categoria):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria

    def exibir_detalhes(self):
        return f"{self._nome} - {self._categoria} - R${self._preco}"