import flet as ft
from usuario import Usuario
from restaurante import Restaurante
from pedido import Pedido
from itemcardapio import ItemCardapio
from entregador import Entregador

# Lista global para armazenar os usuários cadastrados
usuarios_cadastrados = []

# Lista global para armazenar os itens no carrinho
carrinho = []  # Carrinho global

# Lista global para armazenar os pedidos realizados
pedidos_realizados = []  # Para armazenar os pedidos confirmados

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

    # Exibindo o cardápio numerado
    for idx, item in enumerate(restaurante._cardapio, 1):
        page.add(ft.Text(f"{idx}. {item._nome} - R${item._preco}", size=16))

    # Input para adicionar item ao carrinho
    item_input = ft.TextField(label="Digite o nome ou número do item")
    add_item_button = ft.ElevatedButton("Adicionar ao Carrinho", on_click=lambda e: add_item_to_cart(page, item_input, restaurante))

    # Exibir o botão para ver carrinho
    ver_carrinho_button = ft.ElevatedButton("Ver Carrinho", on_click=lambda e: show_cart(page, restaurante))
    
    page.add(item_input, add_item_button, ver_carrinho_button)

    back_button = ft.ElevatedButton("Voltar", on_click=lambda e: show_restaurant_selection(page))
    page.add(back_button)

# Função para adicionar item ao carrinho
def add_item_to_cart(page: ft.Page, item_input: ft.TextField, restaurante: Restaurante):
    global carrinho  # Declara que estamos modificando a variável global carrinho
    item_selecionado = None
    item_input_value = item_input.value  # Pega o valor digitado no campo de texto
    
    # Verificar se é um número ou nome
    try:
        item_idx = int(item_input_value) - 1  # Converter para índice
        if 0 <= item_idx < len(restaurante._cardapio):
            item_selecionado = restaurante._cardapio[item_idx]
    except ValueError:
        # Se não for número, procurar pelo nome
        for item in restaurante._cardapio:
            if item._nome.lower() == item_input_value.lower():
                item_selecionado = item
                break
    
    if item_selecionado:
        carrinho.append(item_selecionado)
        page.add(ft.Text(f"{item_selecionado._nome} adicionado ao carrinho"))
    else:
        page.add(ft.Text("Item não encontrado", color="red"))

    # Limpar o campo de entrada após adicionar o item
    item_input.value = ""  # Limpa o campo de texto
    page.update()  # Atualiza a página para refletir a mudança no campo de texto

# Função para exibir o carrinho
def show_cart(page: ft.Page, restaurante: Restaurante):
    page.clean()
    if carrinho:
        total = sum(item._preco for item in carrinho)
        page.add(ft.Text("Carrinho:", size=20))
        for item in carrinho:
            page.add(ft.Text(f"{item._nome} - R${item._preco}", size=16))
        page.add(ft.Text(f"Total: R${total:.2f}", size=20))

        # Botão para finalizar compra
        finalizar_button = ft.ElevatedButton("Finalizar Compra", on_click=lambda e: show_payment_page(page))
        page.add(finalizar_button)
    else:
        page.add(ft.Text("Carrinho vazio", size=20))

    back_button = ft.ElevatedButton("Voltar ao cardápio", on_click=lambda e: show_menu(page, restaurante))
    page.add(back_button)

# Função para exibir a página de pagamento
def show_payment_page(page: ft.Page):
    page.clean()
    page.add(ft.Text("Confirmação de pagamento", size=20))

    nome_input = ft.TextField(label="Nome de usuário", autofocus=True)
    senha_input = ft.TextField(label="Senha", password=True)

    confirm_payment_button = ft.ElevatedButton("Confirmar Pagamento", on_click=lambda e: confirm_payment(page, nome_input, senha_input))
    
    page.add(nome_input, senha_input, confirm_payment_button)

# Função para confirmar o pagamento
def confirm_payment(page: ft.Page, nome_input: ft.TextField, senha_input: ft.TextField):
    nome = nome_input.value
    senha = senha_input.value
    
    if nome and senha:
        usuario = verificar_usuario(nome, senha)
        if usuario:
            # Criando o pedido
            pedido = Pedido(usuario, "Restaurante", carrinho)  # Criação do pedido
            pedidos_realizados.append(pedido)  # Armazenando o pedido
            
            # Criando o entregador
            entregador = Entregador("João", "123456789", "Moto")  # Passando o veículo agora
            entregador.atribuir_pedido(pedido)  # Atribuindo o pedido ao entregador
            
            page.clean()
            page.add(ft.Text("Pagamento realizado com sucesso!", size=20))
            page.add(ft.Text(f"Pedido será entregue por {entregador._nome}", size=20))  # Exibindo entregador

            # Botão para realizar outro pedido
            realizar_outro_pedido_button = ft.ElevatedButton("Realizar outro pedido", on_click=lambda e: restart_order(page))
            page.add(realizar_outro_pedido_button)
        else:
            page.add(ft.Text("Nome de usuário ou senha incorretos", color="red"))
    else:
        page.add(ft.Text("Por favor, preencha todos os campos", color="red"))

# Função para reiniciar o pedido
def restart_order(page: ft.Page):
    global carrinho  # Limpa o carrinho global
    carrinho = []
    show_restaurant_selection(page)

# Função para rodar o app
def main(page: ft.Page):
    show_login_page(page)

# Inicializa o Flet
ft.app(target=main)
