#9-    Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares. 
i = 0
qtd_pares = 0
qtd_impares = 0
while i<10:
    num = input(f"Diga o {i+1}º número: ")
    while not num.isnumeric():
        print("Tem que ser um inteiro!!")
        num = input(f"Diga o {i+1}º número: ") 
    num = int(num)
    if num%2==0:
        qtd_pares += 1
    else:
        qtd_impares += 1
    i += 1
print(f"Você digitou {qtd_pares} pares e {qtd_impares} impares")