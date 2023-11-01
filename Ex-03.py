# 3 - Inversão de lista: Escreva uma função que inverta uma lista dada.


def inverte_lista(lista):
    ultimo = len(lista)-1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo-i]
        lista[ultimo-i] = aux
    return lista
   
lista = [1,2,3,4,5,6,7]
lista = inverte_lista(lista)
print(lista)

# Jeito ruim:

def inverte_lista_ruinzao(lista):
    invertida = []
    for i in range(len(lista)-1,-1,-1):
        invertida.append(lista[i])
    return invertida

lista = [1,2,3,4,5]
invertida = inverte_lista_ruinzao(lista)
print(invertida)