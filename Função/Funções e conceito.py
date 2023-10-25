def input_numerico(msg):            # def = declarando uma função
    resposta = input (msg)          # resposta = dummy variable ( assume valores dentro de uma função)
    while not resposta.isnumeric():
        print("Tem que ser um número inteiro")
        resposta = input (msg)
    resposta = int(resposta)
    return resposta                 # return (variável) para poder executar a variável fora da função

ano = input_numerico("Diga seu ano de nascimento : ")
qtd = input_numerico("Diga a quantidade de garrafas : ")
print(ano,qtd)