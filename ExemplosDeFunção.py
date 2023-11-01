'''def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num 

idade = verifica_numero("Diga sua idade : ", "Sua idade deve ser um número inteiro!")
qtd_garrafas = verifica_numero("Quantas garrafas você quer ? ", "A quantidade de garrafas deve ser um número inteiro")'''


# A variável global não é a que você quer alterar

def media(numeros):
    soma = 0
    for num in numeros:
        soma+= num
    media_lista = soma/len(numeros)
    return media_lista

notas1 = [10,2,3,9,6] 
notas2 = [2,3,5,1,7] 
notas3 = [1,1,1,1,1] 
medias = []

media1 = media(notas1)
medias.append(media1)
print(medias)

media2 = media(notas2)
medias.append(media2)
print(medias)

media3 = media(notas3)
medias.append(media3)
print(medias)