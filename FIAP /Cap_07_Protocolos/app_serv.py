# Curso Python - FIAP
# APlicacao Servidora
# 28.06.2022 - 22h03

from socket import *

servidor = "127.0.0.1" # Definindo o endereco do servidor
porta = 43210 # porta de entrada

obj_socket = socket(AF_INET, SOCK_STREAM) # (Tipo de identificacao com o servidor, para trabalhar com o TCP)
obj_socket.bind((servidor, porta)) # Setar o servidor, com o endereco e a porta ja definidos.
obj_socket.listen(2) # Quantidade maxima de conexoes que a aplicacao consegue suportar.

print("Aguardando cliente...")

while True:
    conexao, cliente = obj_socket.accept() # Aguarda a conexao de algum cliente.
    print("Conectado com ", cliente, ".")
    while True:
        msg = str(conexao.recv(1024)) # Variavel que recebe a mensagem da conexao com o tamanho de bytes por pacote
        print("Recebemos...", msg)
        msg_enviada = "Ola"
        conexao.send(msg_enviada) # Enviando a mensagem.
        break
    conexao.close()

