# 4- Comprimento da lista: Escreva uma função que retorne o comprimento de uma
# lista sem usar a função embutida len().

def comprimento_lista(lista):
    contador = 0
    for num in lista:
        contador += 1
    return contador

lista = [2,5,1,7]
print(f'O comprimento da lista é de {comprimento_lista(lista)} elementos')


