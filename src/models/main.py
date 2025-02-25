from usuario import Usuario
from restaurante import Restaurante
from pedido import Pedido
from itemcardapio import ItemCardapio
from entregador import Entregador
from tkinter import *

class App:
    def __init__(self, master=None):
        # Janela de Login
        self.master = master
        master.title("Login")
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

        self.tituloCadastro = Label(master, text="Realizar Login", font=("Arial", "14", "bold"))
        self.tituloCadastro.pack(pady=10)  # Adiciona o título com espaçamento

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

        # Botão de cadastro
        self.cadastrar = Button(self.quartoContainer)
        self.cadastrar["text"] = "Cadastre-se"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 12
        self.cadastrar["command"] = self.abrirCadastro
        self.cadastrar.pack(pady=5)

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        # Variáveis globais para armazenar informações
        self.usuario = None
        self.restaurante = None
        self.pedido = None
        self.entregador = None

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "gean" and senha == "123":
            self.mensagem["text"] = "Autenticado"
            self.usuario = Usuario(usuario, "1234", "Rua XYZ")  # Atribuindo dados do usuário após autenticação
            self.master.withdraw()  # Fecha a janela de login
            self.mostrarRestaurantes()  # Abre a janela de pedidos
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def abrirCadastro(self):
        # Janela de Cadastro
        self.cadastroWindow = Toplevel(self.master)
        self.cadastroWindow.title("Cadastro de Cliente")

        self.nomeCadastroLabel = Label(self.cadastroWindow, text="Nome Completo", font=self.fontePadrao)
        self.nomeCadastroLabel.pack(pady=5)

        self.nomeCadastro = Entry(self.cadastroWindow)
        self.nomeCadastro["width"] = 30
        self.nomeCadastro["font"] = self.fontePadrao
        self.nomeCadastro.pack(pady=5)

        self.telefoneLabel = Label(self.cadastroWindow, text="Número de Telefone", font=self.fontePadrao)
        self.telefoneLabel.pack(pady=5)

        self.telefone = Entry(self.cadastroWindow)
        self.telefone["width"] = 30
        self.telefone["font"] = self.fontePadrao
        self.telefone.pack(pady=5)

        self.emailLabel = Label(self.cadastroWindow, text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(pady=5)

        self.email = Entry(self.cadastroWindow)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(pady=5)

        self.senhaCadastroLabel = Label(self.cadastroWindow, text="Criar Senha", font=self.fontePadrao)
        self.senhaCadastroLabel.pack(pady=5)

        self.senhaCadastro = Entry(self.cadastroWindow)
        self.senhaCadastro["width"] = 30
        self.senhaCadastro["font"] = self.fontePadrao
        self.senhaCadastro["show"] = "*"
        self.senhaCadastro.pack(pady=5)

        self.cadastrarButton = Button(self.cadastroWindow, text="Cadastrar", command=self.cadastrarCliente)
        self.cadastrarButton.pack(pady=10)

    def cadastrarCliente(self):
        # Aqui você pode armazenar os dados do cadastro
        nome = self.nomeCadastro.get()
        telefone = self.telefone.get()
        email = self.email.get()
        senha = self.senhaCadastro.get()

        # Simulando a criação de um novo usuário
        self.usuario = Usuario(nome, senha, telefone)

        # Exibe a mensagem de sucesso
        self.mensagem["text"] = f"Cadastro de {nome} realizado com sucesso!"
        self.cadastroWindow.destroy()  # Fecha a janela de cadastro

    def mostrarRestaurantes(self):
        # Cria uma nova janela para escolher o restaurante 
        self.pedidoWindow = Toplevel(self.master)
        self.pedidoWindow.title("Escolher Restaurante")
        
        self.mensagem = Label(self.pedidoWindow, text="Escolha um restaurante", font=self.fontePadrao)
        self.mensagem.pack()

        self.restauranteBtn1 = Button(self.pedidoWindow, text="Pizza Hut", command=self.escolherRestaurante1)
        self.restauranteBtn1.pack()

        self.restauranteBtn2 = Button(self.pedidoWindow, text="Hamburgueria do João", command=self.escolherRestaurante2)
        self.restauranteBtn2.pack()

    def escolherRestaurante1(self):
        self.pedidoWindow = Toplevel(self.master)
        self.pedidoWindow.title("cardapio")
        
        item1 = ItemCardapio("Pizza", 30.0, "Prato principal")
        item2 = ItemCardapio("Coca-cola", 5.0, "Bebida")
        item3 = ItemCardapio("tapioca", 7.0, "complemento")

        restaurante1 = Restaurante("Pizza Hut")
        restaurante1.adicionar_item(item1)
        restaurante1.adicionar_item(item2)
        restaurante1.adicionar_item(item3)

        self.restaurante = restaurante1
        self.mostrarCardapio()

    def escolherRestaurante2(self):
        self.pedidoWindow = Toplevel(self.master)
        self.pedidoWindow.title("cardapio")
        
        item4 = ItemCardapio("Hambúrguer", 20.0, "Prato principal")
        item5 = ItemCardapio("Suco de laranja", 6.0, "Bebida")
        item6 = ItemCardapio("HotDog", 5.0, "Lanche")

        restaurante2 = Restaurante("Hamburgueria do João")
        restaurante2.adicionar_item(item4)
        restaurante2.adicionar_item(item5)
        restaurante2.adicionar_item(item6)

        self.restaurante = restaurante2

    def mostrarCardapio(self):
        # Exibe os itens do cardápio
        self.mensagem["text"] = f"Cardápio do {self.restaurante._nome}:"

        for item in self.restaurante._cardapio:
            label_item = Label(self.pedidoWindow, text=item.exibir_detalhes(), font=self.fontePadrao)
            label_item.pack()

        self.finalizarPedidoBtn = Button(self.pedidoWindow, text="Finalizar Pedido", command=self.finalizarPedido)
        self.finalizarPedidoBtn.pack()

    def finalizarPedido(self):
        # Criando o pedido
        if self.restaurante is not None and self.usuario is not None:
            self.pedido = Pedido(self.usuario, self.restaurante, self.restaurante._cardapio)

            # Exibindo o resumo do pedido
            self.mensagem["text"] = self.pedido.exibir_resumo()

            # Criando um entregador
            self.entregador = Entregador("Carlos Silva", "987654321", "Moto")

            # Atribuindo o pedido ao entregador
            self.entregador.atribuir_pedido(self.pedido)

            # Exibindo o status após o entregador pegar o pedido
            self.mensagem["text"] = self.pedido.exibir_resumo()

            # Finalizando a entrega
            self.entregador.finalizar_entrega(self.pedido)

            # Exibindo o status final
            self.mensagem["text"] = self.pedido.exibir_resumo()


def main():
    janela = Tk()
    App(janela)
    janela.mainloop()


# Chama a função main para rodar o sistema
if __name__ == "__main__":
    main()
