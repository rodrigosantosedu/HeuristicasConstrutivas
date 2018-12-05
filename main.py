# -*- coding: utf-8 -*-
lista_linhas=[]
matriz_cidades =[]
arq = open('brazil58.tsp', 'r')
lista_linhas = arq.readlines()
tamanho_matriz= int(lista_linhas[3][11:len(lista_linhas[3])])

for i in range(tamanho_matriz-1):
    temp =[]
    linha_aux = lista_linhas[7+i].split(" ")
    for j in range(len(linha_aux)):
        elemento = linha_aux[j]
        temp.append(elemento)
    matriz_cidades.append(temp[:])

print (matriz_cidades)
arq.close()
