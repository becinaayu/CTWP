def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Deve ser um desses : ")
        for opcao in lista_opcoes:
            print(opcao)
        resposta = input(msg)
    return resposta
carro = forca_opcao("Diga o seu carro de interesse : ", ['Up', 'Celta', 'Uno'])
sair_ou_nao = forca_opcao("Você deseja continuar ou encerrar ? ",['Continuar','Encerrar'])
sim_ou_nao = forca_opcao("Diga sim ou não : ",['sim','não'])
print(carro,sair_ou_nao,sim_ou_nao)