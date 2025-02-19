from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone)
        self._endereco = endereco
        self._pedidos = []

    def realizar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def visualizar_pedidos(self):
        return [pedido.exibir_resumo() for pedido in self._pedidos]

    def atualizar_endereco(self, endereco):
        self._endereco = endereco
