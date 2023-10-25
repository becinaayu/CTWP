carros = ['Uno', 'Celtinha', 'Audi', 'City']
preco = [10,20,1000000000000,100000]
cor = ['Preto','Brabo','Rosa','Azul']
resposta = input("Digite o nome do carro para saber as informações : ")
while resposta not in carros:
    print("Deve ser um desses : ")
    for carro in carros:
        print(carro)
    resposta = input("Digite o nome do carro para saber as informações : ")
for i in range(len(carros)):
    if carros[i] == resposta:
        indice = i
        print(f"O carro {carros[indice]} custa R${preco[indice]},00 e está disponível na cor{cor[indice]}.")