nota = [10,8,9,10]
def soma_nota(notas): # muda a cada chamada
    soma = 0
    for nota in notas:
        soma+= nota
    media = soma/len(notas)
    return media

media_final = soma_nota(nota)
print(media_final)

# Ou 

def calcula_media(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
    media = soma/len(lista_notas)
    return media
notas_1 = [10,8,9,10]
notas_2 = [10,20,30]
notas_3 = [11,12,13,14,15]

media_1 = calcula_media(notas_1)
media_2 = calcula_media(notas_2)
media_3 = calcula_media(notas_3)

print(media_1,media_2,media_3)