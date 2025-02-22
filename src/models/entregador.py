from pessoa import Pessoa

class Entregador(Pessoa):
    def __init__(self, nome, telefone, veiculo):
        super().__init__(nome, telefone)
        self._veiculo = veiculo
        self._pedidos_entregues = []

    def atribuir_pedido(self, pedido):
        self._pedidos_entregues.append(pedido)
        pedido.atualizar_status('Em entrega')

    def finalizar_entrega(self, pedido):
        pedido.atualizar_status('Entregue')