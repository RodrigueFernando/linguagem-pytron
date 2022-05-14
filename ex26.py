#Faça um programa que leia um número inteiro positivo N e 
# imprima todos os números de 1 até N.

n =int(input())
i=1

if n < 0:
    print("negativo")
while i <= n:
     print(i)
     i = i +1
    