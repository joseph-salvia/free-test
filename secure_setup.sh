#!/bin/bash

#if/else statement to check if the directory is available
if [ -z "$1" ]; then
	echo -e "\033[31mEnter a project name to proceed!!\033[0m"
	exit 1
fi

if [ -d "$1" ]; then
	echo -e "\033[31mError, Project already exists\033[0m"
	exit 1
fi

echo "================================="
echo "SECURE PROJECT SCAFFOLD GENERATOR"
echo "================================="
echo "Project name: $1"
echo "Timestamp: $(date)"
echo "--------------------"

echo ""

mkdir -p $1/scripts
echo "[✓] Created Directory: $1/"
echo "[✓] Created Directory: $1/scripts"
mkdir -p $1/config
echo "[✓] Created Directory: $1/config"
mkdir -p $1/logs
echo "[✓] Created Directory: $1/logs"
mkdir -p $1/secrets
echo "[✓] Created Directory: $1/secrets"

echo ""

touch $1/config/app.conf
echo "[✓] Created File: $1/config/app.conf"
touch $1/secrets/api.key
echo "[✓] Created File: $1/secrets/api.key"
touch $1/scripts/deploy.sh
echo "[✓] Created File: $1/scripts/deploy.sh"

echo ""

echo "----------------------------"
echo "Security Permissions Applied"
echo "----------------------------"
chmod 700 $1/secrets
echo "[🔒] 700 (Owner Only) : my_app/secrets/"
chmod 600 $1/secrets/api.key
echo "[🔒] 600 (Owner Only) : my_app/secrets/api.key"
chmod 700 $1/scripts/deploy.sh
echo "[🔒] 700 (Owner Only) : my_app/scripts/deploy.sh"
chmod 644 $1/config/app.conf
echo "[📖] 644 (Public Read) : my_app/config/app.conf"
chmod 755 $1/logs
echo "[📂] 755 (Public Enter) : my_app/logs/"

echo ""

echo -e "\e[32m----------------------------\e[0m"
echo -e "\e[32m	SETUP COMPLETE!\e[0m"
echo -e "\e[32m----------------------------\e[0m"
echo "Ready to deploy. Run 'cd my_app' to start."
echo "================================="
