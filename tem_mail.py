import os
import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Verifique se a chave API existe
key_file = "api_key.txt"
if not os.path.isfile(key_file):
    print(Fore.RED + "Chave API não encontrada. Por favor, execute o script de instalação novamente.")
    exit(1)

with open(key_file, "r") as file:
    api_key = file.read().strip()

def gerar_email_temporario():
    print(Fore.YELLOW + "Gerando e-mail temporário...")
    url = "https://api.mail.tm/accounts"  # Exemplo de URL da API (substitua pela URL correta)
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        email = response.json()
        print(Fore.GREEN + f"E-mail temporário gerado com sucesso: {email}")
    else:
        print(Fore.RED + "Erro ao gerar e-mail temporário. Tente novamente mais tarde.")

def verificar_caixa_entrada():
    print(Fore.YELLOW + "Verificando a caixa de entrada...")
    # Lógica para verificar a caixa de entrada
    pass

def ler_email_especifico():
    print(Fore.YELLOW + "Lendo um e-mail específico...")
    # Lógica para ler um e-mail específico
    pass

def menu():
    while True:
        print(Fore.CYAN + "========================================")
        print(Fore.CYAN + "Menu: Gerador👑")
        print(Fore.CYAN + "========================================")
        print(Fore.CYAN + "█▀▀▀▀▀▀▀▀           ▀▀▀▀▀▀▀▀█")
        print(Fore.CYAN + "1. Gerar um e-mail temporário")
        print(Fore.CYAN + "2. Verificar a caixa de entrada")
        print(Fore.CYAN + "3. Ler um e-mail específico")
        print(Fore.CYAN + "4. Sair")
        print(Fore.CYAN + "█▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄▄▄█")
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")
        
        if escolha == '1':
            gerar_email_temporario()
        elif escolha == '2':
            verificar_caixa_entrada()
        elif escolha == '3':
            ler_email_especifico()
        elif escolha == '4':
            print(Fore.GREEN + "Saindo...")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
