import requests

# Função para gerar um e-mail temporário
def gerar_email_temporario():
    print("Gerando e-mail temporário...")
    domain = "mailinator.com"
    email_address = f"{os.urandom(6).hex()}@{domain}"
    print(f"E-mail temporário gerado com sucesso: {email_address}")
    return email_address

# Função para verificar caixa de entrada
def verificar_caixa_entrada(email_address):
    print("Verificando a caixa de entrada...")
    email_username = email_address.split('@')[0]
    url = f"https://www.mailinator.com/api/v2/domains/public/inboxes/{email_username}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        emails = response.json().get('messages', [])
        if emails:
            print("E-mails na caixa de entrada:")
            for email in emails:
                print(f"ID: {email['_id']}, Assunto: {email['subject']}, De: {email['from']}")
        else:
            print("Nenhum e-mail encontrado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao verificar caixa de entrada: {e}")

# Função para ler e-mail específico
def ler_email_especifico(email_address, email_id):
    print(f"Lendo e-mail ID {email_id}...")
    email_username = email_address.split('@')[0]
    url = f"https://www.mailinator.com/api/v2/domains/public/inboxes/{email_username}/messages/{email_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        email = response.json()
        if email:
            print(f"Assunto: {email.get('subject')}")
            print(f"De: {email.get('from')}")
            print(f"Corpo: {email.get('parts')[0].get('body')}")
        else:
            print("E-mail não encontrado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao ler e-mail: {e}")

# Menu principal
def menu():
    email_address = None
    while True:
        print("========================================")
        print("Menu: Gerador👑")
        print("========================================")
        print("1. Gerar um e-mail temporário")
        print("2. Verificar a caixa de entrada")
        print("3. Ler um e-mail específico")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            email_address = gerar_email_temporario()
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '2':
            if email_address:
                verificar_caixa_entrada(email_address)
            else:
                print("Por favor, gere um e-mail temporário primeiro.")
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '3':
            if email_address:
                email_id = input("Digite o ID do e-mail para ler: ")
                ler_email_especifico(email_address, email_id)
            else:
                print("Por favor, gere um e-mail temporário primeiro.")
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

