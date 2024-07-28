import requests
import random
import string
import re
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def generate_random_string(length=10):
    """Gera uma string aleatória de letras minúsculas e números."""
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_temp_email():
    """Cria um e-mail temporário usando o serviço 1secmail."""
    username = generate_random_string()
    domain = '1secmail.com'
    email = f"{username}@{domain}"
    return email

def check_inbox(email):
    """Verifica a caixa de entrada do e-mail temporário."""
    username, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def read_email(email, email_id):
    """Lê um e-mail específico na caixa de entrada."""
    username, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={email_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_links(text):
    """Extrai links de um texto."""
    return re.findall(r'(https?://\S+)', text)

def show_menu():
    """Exibe o menu principal com cores e enfeites."""
    print(f"\n{Fore.RED}========================================{Style.RESET_ALL}")
    print(f"{Fore.RED}Menu: Gerador👑{Style.RESET_ALL}")
    print(f"{Fore.RED}========================================{Style.RESET_ALL}")
    print(f"{Fore.RED}█▀▀▀▀▀▀▀▀           ▀▀▀▀▀▀▀▀█{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1. Gerar um e-mail temporário{Style.RESET_ALL}")
    print(f"{Fore.GREEN}2. Verificar a caixa de entrada{Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. Ler um e-mail específico{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}4. Sair{Style.RESET_ALL}")
    print(f"{Fore.RED}█▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄▄▄█{Style.RESET_ALL}")
    print(f"{Fore.RED}Escolha uma opção:{Style.RESET_ALL}")

def main():
    temp_email = None

    while True:
        show_menu()
        choice = input()

        if choice == '1':
            temp_email = create_temp_email()
            print(f"{Fore.YELLOW}E-mail temporário gerado: {Fore.CYAN}{temp_email}{Style.RESET_ALL}")
            input(f"\n{Fore.GREEN}Pressione Enter para voltar ao menu principal...{Style.RESET_ALL}")

        elif choice == '2':
            if not temp_email:
                print(f"{Fore.RED}Por favor, gere um e-mail temporário primeiro.{Style.RESET_ALL}")
            else:
                inbox = check_inbox(temp_email)
                if inbox:
                    print(f"{Fore.BLUE}Caixa de entrada:{Style.RESET_ALL}")
                    for email in inbox:
                        print(f"{Fore.CYAN}ID: {email['id']}, De: {email['from']}, Assunto: {email['subject']}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}A caixa de entrada está vazia.{Style.RESET_ALL}")
            input(f"\n{Fore.GREEN}Pressione Enter para voltar ao menu principal...{Style.RESET_ALL}")

        elif choice == '3':
            if not temp_email:
                print(f"{Fore.RED}Por favor, gere um e-mail temporário primeiro.{Style.RESET_ALL}")
            else:
                inbox = check_inbox(temp_email)
                if not inbox:
                    print(f"{Fore.YELLOW}A caixa de entrada está vazia.{Style.RESET_ALL}")
                else:
                    email_ids = [str(email['id']) for email in inbox]
                    while True:
                        email_id = input("Digite o ID do e-mail que deseja ler (ou pressione Enter para voltar ao menu): ")
                        if email_id == "":
                            break
                        elif email_id in email_ids:
                            email_content = read_email(temp_email, email_id)
                            if email_content:
                                print(f"{Fore.BLUE}Conteúdo do e-mail:{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}De: {email_content['from']}{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}Assunto: {email_content['subject']}{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}Data: {email_content['date']}{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}Conteúdo: {email_content['textBody']}{Style.RESET_ALL}")
                                links = extract_links(email_content['textBody'])
                                if links:
                                    print(f"{Fore.GREEN}Links encontrados:{Style.RESET_ALL}")
                                    for link in links:
                                        print(f"{Fore.BLUE}{link}{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Erro ao ler o e-mail ou e-mail não encontrado.{Style.RESET_ALL}")
                            input(f"\n{Fore.GREEN}Pressione Enter para voltar ao menu principal...{Style.RESET_ALL}")
                            break
                        else:
                            print(f"{Fore.RED}ID inválido. Tente novamente.{Style.RESET_ALL}")

        elif choice == '4':
            print(f"{Fore.RED}Saindo...{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
