class Restaurante:
    def __init__(self, nome):
        self._nome = nome
        self._cardapio = []
        self._pedidos = []

    def adicionar_item(self, item):
        self._cardapio.append(item)

    def listar_cardapio(self):
        return [item.exibir_detalhes() for item in self._cardapio]

    def receber_pedido(self, pedido):
        self._pedidos.append(pedido)
        pedido.atualizar_status('Recebido')