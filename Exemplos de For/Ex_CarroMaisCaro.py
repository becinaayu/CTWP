carros = ['Uno', 'Celtinha', 'Audi', 'City']
precos = [10,200,1000,10000]
cor = ['Preto','Brabo','Rosa','Azul']
indice_maior = 0
maior = precos[indice_maior]
for i in range(1,len(precos)):
    candidato = precos[i]
    print(f'Vou testar se {candidato} > {maior}')
    if candidato > maior:
        print(f"Vou trocar {maior} por {candidato}")
        maior = candidato
        indice_maior = i
print(precos[indice_maior], carros[indice_maior])