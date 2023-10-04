qtd = 5
i = 0
soma = 0
while i < qtd:
    num = input("Digite um número: ")
    while not num.isnumeric():
        num = input("Digite um número: ")
    num = int(num)
    soma += num
    i+=1
media = soma/qtd
print(soma)
print(media)