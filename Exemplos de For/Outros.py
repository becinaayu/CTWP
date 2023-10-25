lista = ['a','b','c','d']
print(lista[0]) # Acessando o conjunto por indice
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista = ['a','b','c','d']
for i in range(len(lista)): # For por indice; consegue a posição de onde o elemento está.
    print(f"lista[{i}] = {lista[i]}")

for elem in lista: # For por elemento; não tem informação da posição
    print(elem) 


for i in range (0,10,2):
    print(i)


lista = ['a','b','c','d']
for elem in lista:
    elem = 1
    print(elem)
    
for i in range(len(lista)):
    lista[i] = 1
print(lista)





 