# 1 - Soma de uma lista: Escreva uma função que recebe uma lista de 
# números como entrada a soma de todos os números na lista.

def soma(numeros):
    soma = 0 
    for i in numeros:
        soma += i
    return soma

lista = [10,10,8,5]
print(f'A soma de todos os números na lista deu : {soma(lista)}')



    



