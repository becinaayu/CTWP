print("Bem vindo à Vinheria Agnello!")
print("Vamos iniciar sua compra.")
nome = input("Digite seu nome : ")
ano = input("Digite seu ano de nascimento : ")
while not ano.isnumeric():
    print("Digite o ano!")
    ano = input("Digite seu ano de nascimento : ")
ano = int(ano)
endereco = input("Escreva o seu endereço : ")
if ano > 2005:
    print(f"Que coisa feia {nome}! Não são permitidas as compras de bebidas para menores de idade")
else:
    print("Temos 3 tipos de vinho de alta qualidade")
    print("Vinho de Rosas - R$140 / Vinho J'esuis Belle - R$200 / Vinho Cianuretto - R$350")
    escolha = input("Digite qual vinho irá querer levar vr / vjb / vc : ")
    if escolha == 'vr':
        qtd_vr = input("Quantas garrafas de Vinho de Rosa irá levar? : ")
        while not qtd_vr.isnumeric():
            qtd_vr = input("Quantas garrafas de Vinho de Rosa irá levar? : ")
    qtd_vr = int(qtd_vr)
    vr = 140
    qtd_vr * vr

    if escolha == 'vjb':
        qtd_vjb = input("Quantas garrafas de Vinho J'esuis Belle irá levar? : ")
        while not qtd_vjb.isnumeric():
        qtd_vjb = input("Quantas garrafas de Vinho J'esuis Belle irá levar? : ")
    qtd_vjb = int(qtd_vjb)
    vjb = 200
    qtd_vjb * vjb
    if escolha == 'vc':
        qtd_vc = input("Quantas garrafas de Vinho Cianuretto irá levar? : ")
        while not qtd_vc.isnumeric():
          qtd_vc = input("Quantas garrafas de Vinho Cianuretto irá levar? : ")
    qtd_vc = int(qtd_vc)
    vc = 350
    qtd_vc * vc
    valor_final = (qtd_vc + qtd_vjb) + qtd_vr
frete = 30
if valor_final > 500:
    print(f"Compra finalizada {nome}, o valor ficou R${valor_final} e será entregue em {endereco}")
    print("Por conta do valor você recebeu frete grátis")
    print(f"{nome}, Muito obrigado pela preferência e volte sempre")
else:
    print(f"Compra finalizada {nome}, o valor somente dos vinhos ficou R${valor_final} com o frete de R${frete} ficará R${valor_final+frete} e será entregue em {endereco}!")
    print(f"{nome}, Muito obrigado pela preferência e volte sempre")
