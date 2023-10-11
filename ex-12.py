# 12 - Faça um programa que pede as notas de 5 alunos 
# calcule o mostre a média aritmética de 4 notas.

alunos = 0
while alunos < 5:
    i = 0
    soma = 0
    while i < 4:
        nota = input(f"Diga a {i+1}º nota do/a {alunos+1}° aluno/a : ")
        while not nota.isnumeric():
             print("Você deve digitar um número!")
             nota = input(f"Diga a {i+1}º nota do/a {alunos+1}° aluno/a : ")
        nota = int(nota)
        soma += nota
        i += 1
    alunos+=1
    media = soma / i
    print(f"A média é {media}")
    if media < 4:
        print("Reprovado")
    elif media < 6:
        print("Você ficará de exame")
    else:
        print("Passou")
