# 7 - Número máximo: Escreva uma funçao que encontre o número máximo em
# uma lista dada de numeros sem usar a função embutida max().


'''def encontrar(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

lista = [1,20,1,4,0]
resultado = encontrar(lista)
print(resultado)'''


def acha_maior(lista):
    indice_maior = 0
    maximo = lista[0]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato > maximo:
            maximo = candidato
            indice_maior = i
    return indice_maior

lista = [12,20,1000,4,0]
local_maior = acha_maior(lista)
print(f'O maior número está localizado na posição: {local_maior}')

