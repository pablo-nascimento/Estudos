# Curso Python - FIAP
# Protocolos de Rede - Introducao ao FTP
# 12.07.2022 - 11h12

# Importando a biblioteca ftplib
from ftplib import *

# criando o objeto ftp e passando como parametro o dominio com o protocolo ftp para testes.
ftp = FTP("ftp.ibiblio.org")

# mensagem
print(ftp.getwelcome())

# fechando a conexao
ftp.quit()