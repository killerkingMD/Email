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

# Loop do menu
while true; do
    show_key_menu
    read -p "Digite sua escolha: " choice
    case $choice in
        1)
            generate_key
            ;;
        2)
            list_keys
            ;;
        3)
            delete_key
            ;;
        4)
            show_dev_info
            ;;
        5)
            echo "Saindo..."
            exit 0
            ;;
        *)
            echo -e "\e[31mOpção inválida. Tente novamente.\e[0m"
            ;;
    esac
    echo
done
