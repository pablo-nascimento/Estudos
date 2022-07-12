# Curso Python - FIAP
# Protocolos de Rede -  FTP - envio de arquivos
# 12.07.2022 - 11h20

# Importando a biblioteca ftplib
from ftplib import *

ftp = FTP("ftp.ibiblio.org") # Criando o objeto ftp, conectando ao servidor ftp ibiblio
print(ftp.getwelcome()) # dando a saida da mensagem de conexao bem sucedida

usuario = input("Usuario: ") # Receber o usuario
senha = input("Senha: ") # Receber a senha

ftp.login(usuario, senha) # metodo login passando usuario e senha.

print("Diretorio Atual: ", ftp.pwd()) # pwd, para mostrar o diretorio atual apos o login

ftp.cwd("pub") # metodo cwd para mudar o diretorio (diretorio informado no parametro)

print("Diretorio Corrente: ", ftp.pwd()) # diretorio atual

print(ftp.retrlines("LIST")) # Listar todos os arquivos que se encontram na pasta

ftp.quit() # saindo da conexao ftp.