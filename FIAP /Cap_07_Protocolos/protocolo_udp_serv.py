# Curso Python - FIAP
# Protocolos de Rede - Aplicacao servidora com protocolo UDP
# 12.07.2022 - 10H06

from socket import * # Importando todos os métodos da biblioteca socket
servidor = "localhost" # Definindo o endereco do servidor
porta = 43210 # Definindo a porta de entrada das conexoes

# Criando o objeto socket (Define o tipo de identificacao com o servidor(host name ou ip) - trabalhar com o protocolo UDP)
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind(servidor, porta) # Inicializando o servidor com o endereco e porta definidos.
print("Servidor pronto... ")

# Loop infinito
while True:
    # recvfrom com range maximo de conexoes para esperar alguma conexao
    # metodo retorna uma tupla com os dados em bytes que vieram do cliente, e os dados do proprio cliente.
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem......", origem) # Exibindo a origem
    print("Dados....... ", dados.decode()) # Exibindo os dados depois de decodificar o que vem em bytes, para string
    resposta = input("Digite a resposta: ") # informando a resposta
    # sendto - enviando a resposta ja codificada em bytes para a origem.
    obj_socket.sendto(resposta.encode(), origem)
obj_socket.close() # fechando o objeto socket para liberar a porta usada na conexao.