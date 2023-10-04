#2-    Faça um programa que leia e valide as seguintes informações:
#a.    Nome: maior que 3 caracteres;
#b.    Idade: entre 0 e 150;
#c.    Salário: maior que zero;
#d. Sexo: 'f' ou 'm';
#e.    Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome : ")
while len(nome) <= 3:
    print('Seu nome deve ter ao menos 3 caracteres, tente novamente')
    nome = input("Digite seu nome : ")
idade = int(input("Digite sua idade : "))
while (idade < 0 or idade > 150):
    print('Você não tem menos que 0 e mais que 150 anos, tente novamente')
    idade = int(input("Digite sua idade : "))
salario = int(input("Digite seu salario : "))
while salario < 0:
    print('Você é pobre mas nem tanto, tente novamente')
    salario = int(input("Digite seu salario : "))
sx = input("Digite seu sexo f/m : ")
while not (sx == 'f' or sx == 'm'):
    print('f ou m, tente novamente')
    sx = input("Digite seu sexo f/m : ")
ec = input("Digite seu estado civil 's', 'c', 'v' ou 'd' : ")
while ec != 's' and ec != 'c' and (ec != 'v' and ec != 'd'):
    print('s, c, v ou d, tente novamente')
    ec = input("Digite seu estado civil 's', 'c', 'v' ou 'd' : ")