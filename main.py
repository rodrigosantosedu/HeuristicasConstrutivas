# -*- coding: utf-8 -*-
lista_linhas=[]
matriz_cidades =[]
arq = open('brazil58.tsp', 'r')
lista_linhas = arq.readlines()
tamanho_matriz= lista_linhas[3][11:len(lista_linhas[3])]
print (tamanho_matriz)
arq.close()
