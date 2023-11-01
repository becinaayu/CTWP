# 5 - Dedução de lista: Escreva uma função que recebe uma lista como entrada
# e retorna uma nova lista sem elementos duplicados

# Jeito não limpo


'''lista = [1,2,3,2,4,5,4]

for elem_a in lista:
    filtrada = []
    encontrei = False
    #print(f"Vou verificar se o {elem_a} está na lista {filtrada}")
    for elem_b in filtrada:
        #print(f"Verificando se {elem_b} = {elem_a}")
        if elem_b == elem_a:
            encontrei = True
            #print(f"Encontrei o {elem_a} na {filtrada}")
            break
    if encontrei == False:
        #print(f"Como não encontrei o {elem_a}, vou adicionar")
        filtrada.append(elem_a)
        #print(filtrada)'''




def elem_in_lista(alvo,lista):
    for elem in lista:
        if elem == alvo:
            return True
    return False
def remove_repetidos(lista):
    filtrada = []
    for elem_a in lista:
        pertence_ou_nao = elem_in_lista(elem_a, filtrada)
        if pertence_ou_nao == False:
            filtrada.append(elem_a)
    return filtrada

lista = [1,2,3,2,4,5,4]
sem_repeticoes = remove_repetidos(lista)
print(sem_repeticoes)