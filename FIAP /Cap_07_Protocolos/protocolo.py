# Curso Python - FIAP
# Protocolos de Rede
# 28.06.2022 - 21h52

import socket


resp = "S"

while (resp == "S"):
    url = input ("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("URL: ", url, " / IP: ", ip)
    resp = input("Pressione S para uma nova consulta de IP.").upper()