from usuario import Usuario
from restaurante import Restaurante
from pedido import Pedido
from itemcardapio import ItemCardapio
from entregador import Entregador




def main():
    # Criando alguns itens de cardápio
    item1 = ItemCardapio("Pizza", 30.0, "Prato principal")
    item2 = ItemCardapio("Coca-cola", 5.0, "Bebida")
    item3 = ItemCardapio("Hambúrguer", 20.0, "Prato principal")
    item4 = ItemCardapio("Suco de laranja", 6.0, "Bebida")
    
    # Criando um restaurante e adicionando itens ao cardápio
    restaurante1 = Restaurante("Pizza Hut")
    restaurante1.adicionar_item(item1)
    restaurante1.adicionar_item(item2)
    
    restaurante2 = Restaurante("Hamburgueria do João")
    restaurante2.adicionar_item(item3)
    restaurante2.adicionar_item(item4)
    
    # Criando um usuário
    nome_usuario = input("Digite seu nome: ")
    telefone_usuario = input("Digite seu telefone: ")
    endereco_usuario = input("Digite seu endereço: ")
    
    usuario = Usuario(nome_usuario, telefone_usuario, endereco_usuario)
    
    # Mostrando os restaurantes
    print("\nEscolha um restaurante:")
    print("1. Pizza Hut")
    print("2. Hamburgueria do João")
    
    escolha_restaurante = int(input("\nDigite o número do restaurante desejado: "))
    
    match escolha_restaurante:
        case 1:
            restaurante = restaurante1
        case 2:
            restaurante = restaurante2
        case _:
            print("Opção inválida!")
            return
    
    # Mostrando o cardápio
    print(f"\nCardápio do {restaurante._nome}:")
    for idx, item in enumerate(restaurante._cardapio, 1):
        print(f"{idx}. {item.exibir_detalhes()}")
    
    # O usuário escolhe os itens do pedido
    itens_escolhidos = []
    while True:
        escolha_item = int(input("\nDigite o número do item que deseja adicionar ao pedido (0 para finalizar): "))
        
        match escolha_item:
            case 0:
                break
            case 1 | 2 | 3 | 4:
                if 1 <= escolha_item <= len(restaurante._cardapio):
                    itens_escolhidos.append(restaurante._cardapio[escolha_item - 1])
            case _:
                print("Opção inválida!")
    
    if not itens_escolhidos:
        print("Nenhum item selecionado para o pedido.")
        return

    # Criando o pedido
    pedido = Pedido(usuario, restaurante, itens_escolhidos)
    
    # O usuário realiza o pedido
    usuario.realizar_pedido(pedido)
    print(f"\nPedido realizado para o restaurante {restaurante._nome}.")
    
    # O restaurante recebe o pedido
    restaurante.receber_pedido(pedido)
    print(f"Status do pedido: {pedido._status}")
    
    # Criando um entregador
    entregador = Entregador("Carlos", "8888-8888", "Moto")
    
    # O entregador atribui o pedido a ele
    entregador.atribuir_pedido(pedido)
    print(f"Status do pedido: {pedido._status}")
    
    # O entregador finaliza a entrega
    entregador.finalizar_entrega(pedido)
    print(f"Status do pedido: {pedido._status}")
    
    # O usuário visualiza os pedidos realizados
    print("\nHistórico de pedidos:")
    print(usuario.visualizar_pedidos())

# Chama a função main para rodar o sistema
if __name__ == "__main__":
    main()
