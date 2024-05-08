# Passo a passo do projeto (lógica de programação), o Algoritmo:

# 1. Abrir o sistema da empresa;
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pa
import pyautogui as pa
import pygetwindow as gw
import pandas as pd
import time

pa.PAUSE = 0.5
# ocorre após o enter

# pa.click : clica com o mouse
# pa.write : escreve um texto
# pa.press : pressiona uma tecla do teclado
# pa.hotkey : pressiona duas ou mais teclas do teclado (control c)

# abre o Chrome

def is_window_maximized():
    # Obtém a janela do Chrome
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[1]  # Supondo que existe apenas uma janela do Chrome aberta
    # Verifica se a janela do Chrome está maximizada
    return chrome_window.isMaximized

# Abrir o Chrome
pa.press('winleft')  # Pressiona a tecla do Windows para abrir o menu Iniciar
pa.write('chrome')   # Escreve "chrome" para procurar o navegador Chrome
pa.press('enter')     # Pressiona Enter para abrir o Chrome

# Verifica se a janela do Chrome já está maximizada
if not is_window_maximized():
    # Maximizar a janela do Chrome em tela cheia
    pa.hotkey('winleft', 'up')  # Pressiona as teclas Windows + Seta para cima para maximizar a janelachrome

time.sleep(1)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")

time.sleep(1)

pa.click(x=822, y=512)
pa.write("gustavobianchini@estudante.ufscar.br")
pa.press("tab")
pa.write("123456")
pa.press("tab")
pa.press("enter")

# 2. Fazer o Login;
# 3. Abrir/Importar a base de dados de produtos para cadastrar;
tabela = pd.read_csv("produtos.csv")

print(tabela)
# 4. Cadastrar um produto;

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    pa.click(x=728, y=378)
    pa.write(codigo)
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")

    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pa.write(obs)
    pa.press("tab")
    pa.press("enter")

    pa.press("tab")
        
    pa.scroll(5000)
    
# 5. Repetir tudo até o fim da lista de produtos.



