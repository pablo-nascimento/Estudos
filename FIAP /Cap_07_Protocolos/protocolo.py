# Curso Python - FIAP
# Protocolos de Rede
# 28.06.2022 - 21h52

import socket # Importando a biblioteca socket, para o uso com protocolos de comunicacao em rede


resp = "S" # variavel ja inicializada

while (resp == "S"):
    url = input ("Digite uma URL: ") # variavel URl recebendo o que for digitado.
    ip = socket.gethostbyname(url)
    # variavel ip que vai receber o retorno da funcao gethostbyname
    # funcao que, recebe como parametro a url informada pelo usuario e retorna o endereco IP desta URL.

    print("URL: ", url, " / IP: ", ip)
    resp = input("Pressione S para uma nova consulta de IP.").upper()