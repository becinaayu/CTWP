# 2 - Números pares: Escreva uma função que recebe uma lista de
# numeros como entrada e retorna uma nova lista contendo apenas os
# numeros pares da lista original 

def conta_par(lista):
    qtd = 0
    for num in lista:
        if num%2 == 0:
            qtd += 1
    return qtd

lista = [2,4,5,1,9,8]
print(f'Os pares são {conta_par(lista)}')