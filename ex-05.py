#5- Faça um programa que receba dois números inteiros e gere os números 
# inteiros que estão no intervalo compreendido por eles. 
 
num1 = (input("Digite um valor : ")) 
while not num1.isnumeric():
    print("Tem que ser número!")
    num1 = int(input("Digite um valor : ")) 
num1 = int(num1)
num2 = (input("Digite um valor : ")) 
while not num2.isnumeric():
    print("Tem que ser número!")
    num2 = int(input("Digite um valor : "))
num2 = int(num2)
while num1 < num2:
    print(num1)
    num1+=1

while num2 < num1:
    print(num2)
    num2+=1

