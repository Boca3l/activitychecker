import os
import time
import random

# Função Verifica e instala a biblioteca pyautogui
def instalar_pyautogui():
    try:
        import pyautogui
    except ModuleNotFoundError:
        print("Biblioteca pyautogui não encontrada. Instalando...")
        os.system("pip install pyautogui")
        print("Instalação concluída!")
        print("Execute o programa novamente!")

# Executa a função que instala a biblioteca
instalar_pyautogui()

# Agora importa a biblioteca (após garantir que está instalada)
import pyautogui

# Lista de mensagens predefinidas
mensagens = [
    "Salve pai",
    "joga mt slc",
    "!empregos",
    "O homem eh uma maquina",
    "slc bom dms",
    "salve familia",
    "!empregos"
]

# Função para enviar uma mensagem
def enviar_mensagem(mensagem):
    pyautogui.typewrite(mensagem,interval=0.01)  # Digita a mensagem
    pyautogui.press('enter')       # Pressiona Enter

# Loop para enviar cada mensagem da lista
print("Bot iniciado. Pressione Ctrl + C para encerrar.")
try:
    # Espera 10 segundos antes de começar a enviar as mensagens
    print("Aguardando 10 segundos antes de iniciar...")
    time.sleep(10)

    while True:
        for mensagem in mensagens:
            enviar_mensagem(mensagem)
            # Gera um intervalo aleatório entre 30 segundos e 1 minuto (tempo sempre em segundos)
            intervalo = random.randint(30, 60)
            print(f"Aguardando {intervalo} segundos antes da próxima mensagem...")
            time.sleep(intervalo)
except KeyboardInterrupt:
    print("Bot interrompido pelo usuário.")