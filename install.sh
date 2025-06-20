#!/bin/bash

echo -e "\e[92m📦 Instalando dependencias para Crist-OSINT-Tool...\e[0m"

# Detectar sistema
if [ -x "$(command -v apt)" ]; then
    # Debian, Kali, Termux (APT)
    pkg install -y python git curl || apt install -y python3 git curl
fi

pip install requests colorama --break-system-packages 2>/dev/null || pip3 install requests colorama

echo -e "\e[92m✅ Instalación completa. Ejecuta con:\e[0m"
echo -e "\e[96m  python3 main.py\e[0m"

sleep 1
xdg-open "https://www.youtube.com/@TechConWin" 2>/dev/null || :
