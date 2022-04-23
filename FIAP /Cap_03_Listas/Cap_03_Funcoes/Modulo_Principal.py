# Módulo principal - abaixo, declaraçao de importacao das funcoes definidas em Identificacao_de_Funcoes.py

from Cap_03_Listas.Cap_03_Funcoes.Identificacao_de_Funcoes import *
minhaLista = []
print('Preenchendo...')
preencherInventario(minhaLista) 

print('Exibindo...')
exibirInventario(minhaLista)

print('Pesquisando...')
localizarLista(minhaLista)

print('Excluindo itens...')
excluirInventario(minhaLista)

print('Resumo dos valores...')
mostrarResumoValores(minhaLista)
