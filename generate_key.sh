#!/bin/bash

# Função para exibir o menu com enfeites e gradiente de cores
show_key_menu() {
    echo -e "\e[38;5;196m========================================\e[0m"
    echo -e "\e[38;5;202mMenu: Gerador de Chaves🔑\e[0m"
    echo -e "\e[38;5;208m========================================\e[0m"
    echo -e "\e[38;5;196m█▀▀▀▀▀▀▀▀           ▀▀▀▀▀▀▀▀█\e[0m"
    echo -e "\e[38;5;214m1. Gerar uma nova chave\e[0m"
    echo -e "\e[38;5;220m2. Listar chaves existentes\e[0m"
    echo -e "\e[38;5;226m3. Excluir uma chave\e[0m"
    echo -e "\e[38;5;226m4. Informações do Desenvolvedor\e[0m"
    echo -e "\e[38;5;190m5. Sair\e[0m"
    echo -e "\e[38;5;196m█▄▄▄▄▄▄▄▄           ▄▄▄▄▄▄▄▄█\e[0m"
    echo -e "\e[38;5;226mEscolha uma opção:\e[0m"
}

# Função para gerar uma nova chave usando Python
generate_key() {
    new_key=$(python3 -c "import uuid; print(uuid.uuid4())")
    echo $new_key >> keys.txt
    echo -e "\e[32mChave gerada: $new_key\e[0m"
    echo -e "\e[34mPressione Enter para voltar ao menu...\e[0m"
    read
}

# Função para listar chaves existentes
list_keys() {
    if [ -f keys.txt ]; then
        echo -e "\e[34mChaves existentes:\e[0m"
        cat keys.txt
    else
        echo -e "\e[31mNenhuma chave encontrada.\e[0m"
    fi
    echo -e "\e[34mPressione Enter para voltar ao menu...\e[0m"
    read
}

# Função para excluir uma chave
delete_key() {
    if [ -f keys.txt ]; then
        echo -e "\e[34mChaves existentes:\e[0m"
        cat -n keys.txt
        read -p "Digite o número da chave que deseja excluir (ou 't' para excluir todas): " key_number
        if [ "$key_number" == "t" ]; then
            rm keys.txt
            echo -e "\e[32mTodas as chaves foram excluídas.\e[0m"
        else
            sed -i "${key_number}d" keys.txt
            echo -e "\e[32mChave $key_number excluída.\e[0m"
        fi
    else
        echo -e "\e[31mNenhuma chave encontrada para excluir.\e[0m"
    fi
    echo -e "\e[34mPressione Enter para voltar ao menu...\e[0m"
    read
}

# Função para exibir informações do desenvolvedor
show_dev_info() {
    echo -e "\e[38;5;202m========================================\e[0m"
    echo -e "\e[38;5;208mInformações do Desenvolvedor\e[0m"
    echo -e "\e[38;5;202m========================================\e[0m"
    echo -e "\e[38;5;214mDesenvolvedor: KillerkingMD\e[0m"
    echo -e "\e[38;5;220mTelegram: https://t.me/killerkingMD\e[0m"
    echo -e "\e[38;5;226m========================================\e[0m"
    echo
    echo -e "\e[34mPressione Enter para voltar ao menu...\e[0m"
    read
}

# Função para validar a chave fornecida pelo usuário
validate_key() {
    local key="$1"
    if grep -q "$key" keys.txt; then
        echo -e "\e[32mChave válida.\e[0m"
        return 0
    else
        echo -e "\e[31mChave inválida.\e[0m"
        return 1
    fi
}

# Pergunta ao usuário se deseja instalar o script
read -p "Você deseja instalar o script? (y/n): " choice

if [[ "$choice" != "y" ]]; then
    echo "Instalação cancelada."
    exit 0
fi

# Solicita a chave ao usuário
read -p "Digite a chave para validação: " user_key
validate_key "$user_key" || exit 1

# URL dos scripts no GitHub
SCRIPT_URL="https://raw.githubusercontent.com/killerkingMD/Email/main/tem_mail.py"
KEY_SCRIPT_URL="https://raw.githubusercontent.com/killerkingMD/Email/main/generate_key.sh"

# Nome dos arquivos para os scripts
SCRIPT_NAME="tem_mail.py"
KEY_SCRIPT_NAME="generate_key.sh"

# Baixa o script Python usando wget
echo -e "\e[34mBaixando o script Python...\e[0m"
wget -O $SCRIPT_NAME $SCRIPT_URL

# Verifica se o wget foi bem-sucedido
if [ $? -eq 0 ]; then
    echo -e "\e[32mScript Python baixado com sucesso.\e[0m"
else
    echo -e "\e[31mErro ao baixar o script Python.\e[0m"
    exit 1
fi

# Baixa o script de geração de chaves
echo -e "\e[34mBaixando o script de geração de chaves...\e[0m"
wget -O $KEY_SCRIPT_NAME $KEY_SCRIPT_URL

# Verifica se o wget foi bem-sucedido
if [ $? -eq 0 ]; then
    echo -e "\e[32mScript de geração de chaves baixado com sucesso.\e[0m"
else
    echo -e "\e[31mErro ao baixar o script de geração de chaves.\e[0m"
    exit 1
fi

# Instala as dependências necessárias
echo -e "\e[34mInstalando dependências...\e[0m"
pip install requests colorama

# Verifica se a instalação das dependências foi bem-sucedida
if [ $? -eq 0 ]; then
    echo -e "\e[32mDependências instaladas com sucesso.\e[0m"
else
    echo -e "\e[31mErro ao instalar as dependências.\e[0m"
    exit 1
fi

# Torna os scripts executáveis
chmod +x $SCRIPT_NAME
chmod +x $KEY_SCRIPT_NAME

# Guia intuitiva para o usuário
echo
echo -e "\e[38;5;196m========================================\e[0m"
echo -e "\e[38;5;202mGuia Intuitiva de Uso do Script\e[0m"
echo -e "\e[38;5;208m========================================\e[0m"
echo
echo -e "\e[38;5;214m1. Para iniciar o Menu do script, execute o seguinte comando:\e[0m"
echo -e "\e[38;5;220m   python $SCRIPT_NAME\e[0m"
echo
echo -e "\e[38;5;226m2. No menu apresentado, escolha a opção 1 para gerar um e-mail temporário.\e[0m"
echo
echo -e "\e[38;5;190m3. Para verificar a caixa de entrada, escolha a opção 2.\e[0m"
echo
echo -e "\e[38;5;226m4. Para ler um e-mail específico, escolha a opção 3 e insira o ID do e-mail.\e[0m"
echo
echo -e "\e[38;5;220m5. Para sair do script, escolha a opção 4.\e[0m"
echo
echo -e "\e[38;5;196m========================================\e[0m"
echo -e "\e[38;5;202mFim da Guia Intuitiva\e[0m"
echo -e "\e[38;5;208m========================================\e[0m"

# Executa o script Python
echo -e "\e[34mExecutando o script Python...\e[0m"
python $SCRIPT_NAME
