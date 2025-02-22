from usuario import Usuario
from restaurante import Restaurante
from pedido import Pedido
from itemcardapio import ItemCardapio
from entregador import Entregador
from tkinter import *

class App:
    def __init__(self, master=None):
        
        master.title("cadastro")
        # Adicionando título 'Realizar Cadastro'
        self.tituloCadastro = Label(master, text="Realizar Cadastro", font=("Arial", "14", "bold"))
        self.tituloCadastro.pack(pady=10)  # Adiciona o título com espaçamento

        self.fontePadrao = ("Arial", "10")
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        # Variáveis globais para armazenar informações
        self.usuario = None
        self.restaurante = None

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
            self.usuario = Usuario(usuario, "1234", "Rua XYZ")  # Atribuindo dados do usuário após autenticação
            self.mostrarRestaurantes()
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def mostrarRestaurantes(self):
        # Exibe uma nova interface para escolher o restaurante
        self.mensagem["text"] = "Escolha um restaurante"

        self.restauranteLabel = Label(self.quartoContainer, text="Escolha o restaurante:", font=self.fontePadrao)
        self.restauranteLabel.pack()

        self.restauranteBtn1 = Button(self.quartoContainer, text="Pizza Hut", command=self.escolherRestaurante1)
        self.restauranteBtn1.pack()

        self.restauranteBtn2 = Button(self.quartoContainer, text="Hamburgueria do João", command=self.escolherRestaurante2)
        self.restauranteBtn2.pack()

    def escolherRestaurante1(self):
        item1 = ItemCardapio("Pizza", 30.0, "Prato principal")
        item2 = ItemCardapio("Coca-cola", 5.0, "Bebida")

        restaurante1 = Restaurante("Pizza Hut")
        restaurante1.adicionar_item(item1)
        restaurante1.adicionar_item(item2)

        self.restaurante = restaurante1
        self.mostrarCardapio()

    def escolherRestaurante2(self):
        item3 = ItemCardapio("Hambúrguer", 20.0, "Prato principal")
        item4 = ItemCardapio("Suco de laranja", 6.0, "Bebida")

        restaurante2 = Restaurante("Hamburgueria do João")
        restaurante2.adicionar_item(item3)
        restaurante2.adicionar_item(item4)

        self.restaurante = restaurante2
        self.mostrarCardapio()

    def mostrarCardapio(self):
        # Exibe os itens do cardápio
        self.mensagem["text"] = f"Cardápio do {self.restaurante._nome}:"

        for item in self.restaurante._cardapio:
            label_item = Label(self.quartoContainer, text=item.exibir_detalhes(), font=self.fontePadrao)
            label_item.pack()

        self.finalizarPedidoBtn = Button(self.quartoContainer, text="Finalizar Pedido", command=self.finalizarPedido)
        self.finalizarPedidoBtn.pack()

    def finalizarPedido(self):
        # Lógica para finalizar o pedido
        print("Pedido Finalizado")
        # A lógica real de finalizar o pedido pode ser adicionada aqui (como no seu código original)

def main():
    janela = Tk()
    App(janela)
    janela.mainloop()

# Chama a função main para rodar o sistema
if __name__ == "__main__":
    main()
