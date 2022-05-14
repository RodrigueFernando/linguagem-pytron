#Faça um programa que leia um número inteiro positivo N. 
# Após isso o programa deve ler N números inteiros e ao final da leitura imprimir 
# o maior deles
maior=0
cont=0
n=int(input())

for i in range(n):
    valor=int(input())
    if cont ==1:
      maior = valor
      cont=cont+1
    if maior  < valor:
       maior = valor

print(maior)