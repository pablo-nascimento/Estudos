# Curso Python - FIAP
# APlicacao Cliente
# 28.06.2022 - 22h21

from socket import * # importando toda a biblioteca

servidor = "localhost" # endereco do servidor
porta = 43210 # porta de entrada

msg = bytes(input("Digite alguma coisa: "), "utf-8") # capturando o que o usuario informa e convertendo para bytes.
obj_socket = socket(AF_INET, SOCK_STREAM) # criando o objeto socket
obj_socket.connect((servidor, porta)) # conectando ao servidor especificado acima
obj_socket.send(msg) # metodo send, enviar a mensagem
resposta = obj_socket.recv(1024) # armazenando a resposta de tamanho de 1024 bytes.
print("Recebemos...." ,resposta)
obj_socket.close() # fechando o objeto socket, fechando a conexao.