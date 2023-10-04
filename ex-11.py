# 11 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = 25
i = 2
while i < num:
    print(f"{num}%{i} = {num%i}")
    if num % i == 0:
        print(f'{num} NÃO É PRIMO')
        break
    elif i >= num/2:
        print(f"{num} é primo, parabéns")
        break
    i+=1