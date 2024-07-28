import os

# Verifique se a chave API existe
key_file = "api_key.txt"
if not os.path.isfile(key_file):
    print("Chave API não encontrada. Por favor, execute o script de instalação novamente.")
    exit(1)

with open(key_file, "r") as file:
    api_key = file.read().strip()

def generate_temporary_email():
    print("Gerando e-mail temporário...")
    # Adicione aqui a lógica para gerar um e-mail temporário usando a API
    # Exemplo: response = requests.post(url, headers=headers, data=data)
    print("E-mail temporário gerado com sucesso!")

def check_inbox():
    print("Verificando a caixa de entrada...")
    # Adicione aqui a lógica para verificar a caixa de entrada usando a API
    # Exemplo: response = requests.get(url, headers=headers)
    print("E-mails na caixa de entrada: [E-mails listados aqui]")

def read_specific_email(email_id):
    print(f"Lendo e-mail com ID: {email_id}")
    # Adicione aqui a lógica para ler um e-mail específico usando a API
    # Exemplo: response = requests.get(url, headers=headers)
    print(f"Conteúdo do e-mail {email_id}: [Conteúdo do e-mail]")

def display_menu():
    print("========================================")
    print("Menu: Gerador👑")
    print("========================================")
    print("█▀▀▀▀▀▀▀▀           ▀▀▀▀▀▀▀▀█")
    print("1. Gerar um e-mail temporário")
    print("2. Verificar a caixa de entrada")
    print("3. Ler um e-mail específico")
    print("4. Sair")
    print("█▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄▄▄█")
    
    choice = input("Escolha uma opção: ")

    if choice == '1':
        generate_temporary_email()
    elif choice == '2':
        check_inbox()
    elif choice == '3':
        email_id = input("Digite o ID do e-mail que deseja ler: ")
        read_specific_email(email_id)
    elif choice == '4':
        print("Saindo do script...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    while True:
        display_menu()
