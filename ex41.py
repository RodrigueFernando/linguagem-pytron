#Faça um programa que leia um número inteiro N
#  e imprima a soma de todos os números primos entre 1 e N (inclusive N).

n=int(input())

soma = 0

for i in range(2, n + 1):
    primo=1
    for cont in range(2,i):
        if i % cont==0:
            primo=0
    if primo==1:
        soma=soma+i
print(soma)


        

