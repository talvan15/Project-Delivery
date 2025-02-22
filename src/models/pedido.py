class Pedido:
    def __init__(self, cliente, restaurante, itens):
        self._cliente = cliente
        self._restaurante = restaurante
        self._itens = itens
        self._status = 'Aguardando'

    def calcular_total(self):
        return sum(item._preco for item in self._itens)

    def atualizar_status(self, status):
        self._status = status

    def exibir_resumo(self):
        itens_resumo = [item.exibir_detalhes() for item in self._itens]
        total = self.calcular_total()
        return f"Pedido de {self._cliente.get_nome()} - Status: {self._status} - Itens: {', '.join(itens_resumo)} - Total: R${total}"