import flet as ft

def main(pagina):

    def iniciar_chat(evento):
       pagina.dialog = janela #popup
       janela.open = True
       pagina.update()
    
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario} entrou no chat!"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # pagina inicial
    titulo = ft.Text("Chat")
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    pagina.add(titulo)
    pagina.add(botao_iniciar)

    # criação da janela em popup
    titulo_janela = ft.Text("Bem-vindo ao chat!")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_nome_usuario, 
        actions=[botao_entrar])

    # dentro do chat em si
    chat = ft.Column()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    # criar tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    
ft.app(main, view=ft.WEB_BROWSER)