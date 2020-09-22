# -*- coding: utf-8 -*- #

# ----------------------------------------- #
# ------- Checker de invite discord ------- #
# ------- By WhoniX#3737            ------- #
# ------------------------------------------#

import requests

f = open("discords-testes.txt", "r")
for word in f:
    r = requests.get(f"https://canary.discordapp.com/api/v6/invite/{word}")
    if r.status_code == 200:
        print(f"[+] Código discord -> {r.status_code} -> Link funcionando! -> https://discord.gg/{word}")
        arquivo = open('discord-lives.txt', 'r')
        servidores = arquivo.readlines()
        servidores.append(f"[+] Codigo discord -> {r.status_code} OK -> Link funcionando -> https://discord.gg/{word}")
        arquivo = open('discord-lives.txt', 'w')
        arquivo.writelines(servidores)
    if r.status_code == 404:
        print(f"[x] Código discord -> {r.status_code} -> Link inválido -> https://discord.gg/{word}")