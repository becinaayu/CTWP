# 10 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = input('Digite um número inteiro: ')
while not num.isnumeric() or int(num)<=0:
    print("Número inválido, tente novamente")
    num = input('Digite um número inteiro: ')
num = int(num)
i = 0
fat = 1
saida = ''
while i < num:
    i += 1
    fat *= i
    if i!= num:
        saida += f'{i}*'
    else:
        saida+=f'{i}={fat}'
print(fat)
print(saida)
    