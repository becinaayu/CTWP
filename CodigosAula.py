i = 2
while i < 10:
    print(i)
    i+=1

for i in range(10): # Faça com que uma variável assuma todos os valores deste conjunto
    print(i)

# While e For são estruturas de repetição
# While é mais geral do que o For


for i in range(10):
    print(i)
for char in "danilo": # vai 'soletrar' a variável
    print(char) 

for i in range(1, 100, 7): # printou de 1 até 100 pulando 7 números
    print(i)


for i in range (0,10,-2): # Conjunto vazio
    print(i)

# Média de 5 notas usando o for
soma = 0
for i in range(5):
    nota = int(input(f"Diga a {i+1}º nota do aluno : "))
    soma += nota
print(soma/5)


# Validando senha e user: 

user = 'cinayu'
senha = '1234'
for i in range(3): # Para ter 3 repetições
    tentativa_user = input("Digite seu usuário : ")
    tentativa_senha = input("Digite sua senha:")
    if user == tentativa_user and senha == tentativa_senha:
        print("Acesso liberado")
        break


# Tabuada de todos os números de 1 até 10 usando for:

for num in range(1,11):
    print(f"\nTabuada do {num}")
    for tab in range(1,11):
       print(f"{num} x {tab} = {num*tab}")

# Usando listas:
# A lista permite guardar valores, como se fosse um banco de dados


lista = [0, 2.1, 'qualquer coisa', True]
for elem in lista:
    print(elem)

# As arrays nas listas sempre iniciam do 0

lista = [30,40,50,60,70,80,90]
print(lista[0]) # Irá printar o 30!

# Listas e indices:

lista = [30,40,50,60,70,80,90]
for elem in lista:
    elem = 1
print(lista)

for i in range(len(lista)):
    lista[i] = 1
print(lista)

# Append

lista = []
lista.append(34) # adiciona à lista
print(lista)
lista.append(50)
print(lista)

# Exercicio de Listas

lista = []
for i in range(5):
    nota = input(f"Digite a {i+1}° nota : ")
    while not nota.isnumeric() or (int(nota)<0 or int(nota)>10):
        print("Tem que ser um inteiro de 0 até 10")
        nota = input(f"Digite a {i+1}° nota : ")
    nota = int(nota)
    lista.append(nota)
    print(lista)
    
    

soma = 0
for nota in lista: # Acessa a nota por elemento
    soma+=nota
media = soma/len(lista)
print(media)

abaixo = 0
acima = 0
for nota in lista:
    if nota >=5:
        acima+=1
    else:
        abaixo +=1
print(acima)
print(abaixo)

soma = 0
for i in range(len(lista)): # Acessa a nota por indice
    nota = lista[i]
    soma+=nota
media = soma/len(lista)
print(media)

acima = 0
abaixo = 0
for i in range(len(lista)):
    nota = lista[i]
    if nota >=5:
        acima+=1
    else:
        abaixo +=1
print(acima)
print(abaixo)

# Manipulando listas:

nomes = ['Danilo', 'Beatriz', 'Giovanna', 'Isabela', 'Miguel', 'Pedro', 'Maria', 'João', 'Henrique', 'Yan']
for i in range(len(nomes)):
    if nomes[i] == 'Danilo':
        print("O Danilo é muito top")
        print(f"O indice dele na lista é {i}")
        break
    else:
        print("Somente o Danilo é Top")
