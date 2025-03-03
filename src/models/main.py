import flet as ft
from usuario import Usuario
from restaurante import Restaurante
from pedido import Pedido
from itemcardapio import ItemCardapio
from entregador import Entregador

# Lista global para armazenar os usuários cadastrados
usuarios_cadastrados = []

# Função para exibir a tela de cadastro
def cadastro_page(page: ft.Page):
    page.clean()  # Limpa a tela antes de adicionar os novos componentes
    page.title = "Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    nome_input = ft.TextField(label="Nome", autofocus=True)
    telefone_input = ft.TextField(label="Telefone")
    endereco_input = ft.TextField(label="Endereço")
    senha_input = ft.TextField(label="Senha", password=True)  # Usando TextField com password=True
    confirmar_senha_input = ft.TextField(label="Confirmar Senha", password=True)  # Usando TextField com password=True
    
    cadastrar_button = ft.ElevatedButton("Cadastrar", on_click=lambda e: handle_cadastro(page, nome_input, telefone_input, endereco_input, senha_input, confirmar_senha_input))
    
    login_button = ft.TextButton("Já tem conta? Faça login", on_click=lambda e: show_login_page(page))
    
    page.add(nome_input, telefone_input, endereco_input, senha_input, confirmar_senha_input, cadastrar_button, login_button)

# Função chamada ao clicar no botão de cadastro
def handle_cadastro(page: ft.Page, nome_input: ft.TextField, telefone_input: ft.TextField, endereco_input: ft.TextField, senha_input: ft.TextField, confirmar_senha_input: ft.TextField):
    nome = nome_input.value
    telefone = telefone_input.value 
    endereco = endereco_input.value
    senha = senha_input.value
    confirmar_senha = confirmar_senha_input.value
    
    if nome and telefone and endereco and senha and confirmar_senha:
        if senha == confirmar_senha:
            usuario = Usuario(nome, telefone, endereco)
            usuario.senha = senha  # Atribuindo a senha diretamente ao atributo da classe Usuario
            usuarios_cadastrados.append(usuario)  # Adicionando o usuário na lista de cadastrados
            page.clean()
            show_login_page(page)
        else:
            page.add(ft.Text("As senhas não coincidem", color="red"))
    else:
        page.add(ft.Text("Por favor, preencha todos os campos", color="red"))

# Função para exibir a tela de login
def show_login_page(page: ft.Page):
    page.clean()  # Limpa a tela antes de adicionar os novos componentes
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    nome_input = ft.TextField(label="Nome", autofocus=True)
    senha_input = ft.TextField(label="Senha", password=True)  # Usando TextField com password=True
    
    login_button = ft.ElevatedButton("Entrar", on_click=lambda e: handle_login(page, nome_input, senha_input))
    
    cadastro_button = ft.TextButton("Não tem conta? Cadastre-se", on_click=lambda e: cadastro_page(page))
    
    page.add(nome_input, senha_input, login_button, cadastro_button)

# Função chamada ao clicar no botão de login
def handle_login(page: ft.Page, nome_input: ft.TextField, senha_input: ft.TextField):
    nome = nome_input.value
    senha = senha_input.value
    
    if nome and senha:
        usuario = verificar_usuario(nome, senha)
        if usuario:
            page.clean()
            show_restaurant_selection(page)
        else:
            page.add(ft.Text("Nome de usuário ou senha incorretos", color="red"))
    else:
        page.add(ft.Text("Por favor, preencha todos os campos", color="red"))

# Função para verificar o usuário e senha
def verificar_usuario(nome: str, senha: str):
    # Verificando se o nome e senha do usuário correspondem aos cadastrados
    for usuario in usuarios_cadastrados:
        if usuario._nome == nome and usuario.senha == senha:
            return usuario  # Retorna o usuário caso as credenciais sejam válidas
    return None  # Retorna None caso não encontre o usuário

# Função para exibir a tela de seleção de restaurante
def show_restaurant_selection(page: ft.Page):
    # Criando os itens de cardápio
    item1 = ItemCardapio("Pizza", 30.0, "Prato principal")
    item2 = ItemCardapio("Coca-cola", 5.0, "Bebida")
    item3 = ItemCardapio("Hambúrguer", 20.0, "Prato principal")
    item4 = ItemCardapio("Suco de laranja", 6.0, "Bebida")
    
    # Criando os restaurantes
    restaurante1 = Restaurante("Pizza Hut")
    restaurante1.adicionar_item(item1)
    restaurante1.adicionar_item(item2)
    
    restaurante2 = Restaurante("Hamburgueria do João")
    restaurante2.adicionar_item(item3)
    restaurante2.adicionar_item(item4)

    # Tela de seleção do restaurante
    page.clean()
    page.add(ft.Text("Escolha um restaurante:", size=20))

    def on_restaurant_select(selected_restaurante):
        if selected_restaurante == 1:
            restaurante = restaurante1
        elif selected_restaurante == 2:
            restaurante = restaurante2
        else:
            return
        
        show_menu(page, restaurante)

    btn_rest1 = ft.ElevatedButton("Pizza Hut", on_click=lambda e: on_restaurant_select(1))
    btn_rest2 = ft.ElevatedButton("Hamburgueria do João", on_click=lambda e: on_restaurant_select(2))
    page.add(btn_rest1, btn_rest2)

# Função para exibir o cardápio de um restaurante
def show_menu(page: ft.Page, restaurante: Restaurante):
    page.clean()
    page.add(ft.Text(f"Cardápio do {restaurante._nome}:", size=20))

    def add_item_to_order(selected_item_idx):
        item = restaurante._cardapio[selected_item_idx]
        if item:
            page.add(ft.Text(f"Item {item._nome} adicionado ao pedido"))

    for idx, item in enumerate(restaurante._cardapio, 1):
        button = ft.ElevatedButton(item._nome, on_click=lambda e, idx=idx-1: add_item_to_order(idx))
        page.add(button)

    back_button = ft.ElevatedButton("Voltar", on_click=lambda e: show_restaurant_selection(page))
    page.add(back_button)

# Função para rodar o app
def main(page: ft.Page):
    show_login_page(page)

# Inicializa o Flet
ft.app(target=main)
