#8- A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo 
 
a = 1 
b = 1 
i = 0 
c = a+b 
print(a)
print(b)
while i < 10: 
    c = a+b 
    a=b # 'a' recebe quem estava no 'b' ( 1 )
    b=c # 'b' recebe quem estava no 'c' ( c = a+b = 2)
    i+=1 # repetições até chegar no 10
    print(c)
    
# Exemplo proporção aurea:
a = 1 
b = 1 
i = 0 
c = a+b 
print(a)
print(b)
while i < 10: 
    c = a+b 
    a=b 
    b=c 
    print(f"{b}/{a} = {b/a}")
    i+=1 
    print(c)