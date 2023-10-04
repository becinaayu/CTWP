#7- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: 
#Tabuada de 5: 
#5 X 1 = 5 
#5 X 2 = 10 
#... 
#5 X 10 = 50 
print("Vamos calcular a tabuada!") 
num = (input("Digite seu número : ")) 
while not num.isnumeric():
    num = (input("Digite seu número : ")) 
num = int(num)
i=1
while i <= 10:
    print(f"{num}x{i} = {num*i}")
    i+=1

# Exemplo:

print("Vamos mostrar a tabuada!")
num = 1
while num <= 10:
    print(f"A tabuada do {num} é : ")
    i=1
    while i <= 10:
        print(f"{num}x{i} = {num*i}")
        i += 1
    num+=1 
    