# Curso Python - FIAP
# Bibliotecas Externas.
# 28.06.2022 - 21h11

import platform
# Biblioteca Python - usando para acesso a informacoes do sistema.

from datetime import datetime # Datas
import getpass

print("Nome da Máquina ............. ", platform.node())
print("Arquitetura ............. ", platform.architecture())
print("Nome do SO ............. ", platform.system())
print("Versao do SO ............. ", platform.release())
print("Processador ............. ", platform.processor())
print("Python .......... ", platform.python_version())
print("\n")

# uso da biblioteca datetime
print(datetime.now())  # Data atual
print(datetime.now().year) # Somente o ano
print(datetime.now().month) # Mes
print(datetime.now().day) # Dia
print("\n")

# Uso da biblioteca getpass
print(getpass.getuser()) # Usuario da máquina atraves da funcao getuser
print(getpass.getpass("Digite sua senha: ")) # funcao getpass
