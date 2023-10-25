def conta_pares(numeros):
    pares = 0
    for num in numeros:
        if num% 2== 0:
            pares+=1
    return pares
lista = [1,2,3,4,5,6] # variavel global pode ser acessada em qualquer lugar do código
qtd_pares = conta_pares([2,4,6,8,10])
print(qtd_pares)
