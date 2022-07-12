# Curso Python - FIAP
# Protocolos de Rede - Aplicacao cliente com protocolo UDP
# 12.07.2022 - 10h25

from socket import * # Importando os métodos da biblioteca socket

servidor = "127.0.0.1" # Definindo o endereco do servidor
porta = 43210 # Definindo a porta de conexao

obj_socket = socket(AF_INET, SOCK_DGRAM) # Definindo a identificacao com o servidor (endereco IP ou hostname), estipular  o UDP
obj_socket.connect((servidor, porta)) # Conectando  o servidor com o endereco e porta definidos
saida = "" # Inicializando a variavel saida

while saida != "X": # variavel saida for diferente de X
    msg = input("Mensagem: ") # Recebendo uma mensagem

    # sendto - enviando a mensagem codificada (bytes) para o servidor na porta definidda
    obj_socket.send(msg.encode(), (servidor, porta))

    # Aguardando a resposta informando o range maximo de conexoes de onde essa resposta pode vir
    # metodo recvfrom gera uma tupla com os dados (resposta que veio do servidor), e informacoes da origem desses dados
    dados, origem = obj_socket.recvfrom(65535)
    print("Resposta do servidor...... ", dados.decode()) # dando a saida da mensagem do servidor, ja decodificada
    saida = input("Digite X para sair... ").upper() # aguardando X para sair do laco
obj_socket.close() # fechando o objeto socket para liberar a porta usada na conexao.

