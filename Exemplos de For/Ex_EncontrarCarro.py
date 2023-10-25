carros = ['Uno', 'Celta', 'Audi', 'City']
preco = [10,20,1000000,1]
for i in range(len(carros)):
    if carros[i] == 'Celtinha':
        print(f'{carros[i]} custa R${preco[i]},00.')
        break
    elif i == len(carros)-1: # O menos 1 serve para garantir que chegou ao fim da lista
        print('Carro não encontrado')