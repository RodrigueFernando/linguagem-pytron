#Exercício 01 - Valores ordenados:
#Faça um programa que leia um número inteiro e positivo N. 
# Após isso leia N números inteiros. Ao fim, imprima 1 se 
# a sequência de números lidos estão ordenados em forma crescente e
#  -1 se estão ordenados de forma decrescente. 
# Se não estão ordenados, imprima 0. 
# Considere que uma sequência de tamanho N 
# é crescente quando X1 <= X2 <= ... <= XN e
#  decrescente quando X1 >= X2 >= ... >= XN. 
# No caso desse exercício, se todos os valores lidos forem iguais, 
# considere como um segmento crescente.
crescente=0
descrecente=0
desordenado=0
cont=0
menor=0
maior=0
n=int(input())

for i in range(n):
     valor=int(input())
     if i ==0:
        maior=valor
        menor=valor
     elif maior<= valor:
        maior= valor
        cont=cont+1
        crescente=crescente+1

     elif menor >=  valor:
       
         cont=cont+1
         descrecente=descrecente+1
if cont < i: 
    print(desordenado)
else:    
    if crescente == cont :
        crescente=1
        print(crescente)
    
    elif descrecente==cont:
        descrecente=-1
        print(descrecente)
   