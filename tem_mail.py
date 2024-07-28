import os
import requests
import json

# Função para gerar um e-mail temporário
def gerar_email_temporario():
    print("Gerando e-mail temporário...")
    url = "https://api.mail.tm/accounts"
    domain_response = requests.get("https://api.mail.tm/domains")
    
    if domain_response.status_code == 200:
        domain = domain_response.json()[0]['domain']
        email_address = f"{os.urandom(6).hex()}@{domain}"
        payload = {
            "address": email_address,
            "password": "password123"
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            print(f"E-mail temporário gerado com sucesso: {email_address}")
            return email_address, payload['password']
        except requests.exceptions.RequestException as e:
            print(f"Erro ao gerar e-mail: {e}")
            return None, None
    else:
        print("Erro ao obter o domínio para o e-mail temporário.")
        return None, None

# Função para obter token
def obter_token(email_address, password):
    url = "https://api.mail.tm/token"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "address": email_address,
        "password": password
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        token_info = response.json()
        return token_info.get('token')
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter token: {e}")
        return None

# Função para verificar caixa de entrada
def verificar_caixa_entrada(token):
    print("Verificando a caixa de entrada...")
    url = "https://api.mail.tm/messages"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        emails = response.json().get('hydra:member', [])
        if emails:
            print("E-mails na caixa de entrada:")
            for email in emails:
                print(f"ID: {email['id']}, Assunto: {email['subject']}, Remetente: {email['from']['address']}")
        else:
            print("Nenhum e-mail encontrado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao verificar caixa de entrada: {e}")

# Função para ler e-mail específico
def ler_email_especifico(token, email_id):
    print(f"Lendo e-mail ID {email_id}...")
    url = f"https://api.mail.tm/messages/{email_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        email = response.json()
        if email:
            print(f"Assunto: {email.get('subject')}")
            print(f"De: {email.get('from').get('address')}")
            print(f"Corpo: {email.get('text')}")
        else:
            print("E-mail não encontrado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao ler e-mail: {e}")

# Menu principal
def menu():
    email_address, password = None, None
    token = None
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
            email_address, password = gerar_email_temporario()
            if email_address:
                token = obter_token(email_address, password)
                input("Pressione Enter para voltar ao menu...")
        elif escolha == '2':
            if token:
                verificar_caixa_entrada(token)
            else:
                print("Por favor, gere um e-mail temporário primeiro.")
            input("Pressione Enter para voltar ao menu...")
        elif escolha == '3':
            if token:
                email_id = input("Digite o ID do e-mail para ler: ")
                ler_email_especifico(token, email_id)
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
