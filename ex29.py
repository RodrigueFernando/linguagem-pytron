#Faça um programa que leia dois números inteiros N e M e 
# imprima a soma de todos os números entre eles (inclua N e M na soma). 
# Faça sua solução utilizando laço de repetição.

n=int(input())
m=int(input())

soma=0


if n > m:
  print()
while n <= m:

 soma=  soma+n
 n=n+1

print(soma)