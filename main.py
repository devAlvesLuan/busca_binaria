import math

def busca_binaria(lista_numeros, alvo, primeiro_indice, ultimo_indice, contador=0):
    meio_indice = 0

    if primeiro_indice > ultimo_indice:
        print(contador)
        return - 1    
        
    tamanho_lista = ultimo_indice - primeiro_indice + 1
    if tamanho_lista % 2 == 0:
        meio_indice = math.ceil((ultimo_indice + primeiro_indice) / 2)
    else:
        meio_indice = (ultimo_indice + primeiro_indice) // 2
    
    contador += 1
    if alvo == lista_numeros[meio_indice]:
        print(contador)
        return meio_indice
    elif alvo < lista_numeros[meio_indice]:
        return busca_binaria(lista_numeros, alvo, primeiro_indice, meio_indice - 1, contador)
    else:
        return busca_binaria(lista_numeros, alvo, meio_indice + 1, ultimo_indice, contador)

        
lista_numeros = list(map(int, input().split()))
lista_numeros.sort()
alvo = int(input())

print(busca_binaria(lista_numeros, alvo, 0, len(lista_numeros) - 1))
