lista = [4,2,6,1,7,0]
print(lista)
for i in range(len(lista)//2):
    ultimo = len(lista)-1
    aux = lista[i]
    lista[i] = lista[ultimo-i]
    lista[ultimo-i] = aux
    print(lista)
print()
lista = [4,2,6,1,7,0]
print(lista[::-1]) # Somente em Python para inverter a ordem
