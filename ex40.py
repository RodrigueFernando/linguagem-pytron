#Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) 
# e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo
#  número 1 e pelo número 7.
#Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) e 
# por ele mesmo. Por exemplo, o número 7 é primo, 
# pois pode ser dividido apenas pelo número 1 e pelo número 7.
# Faça um programa que leia um número inteiro positivo N e 
# imprima 1 se ele for primo e 0 caso contrário.

resto=0
primo=0

n=int(input())
if n <=0:
 
  print(resto)
else:
 
 for i in range(2,n):
    if n % i==0:
     resto= resto+1
 if resto==0:
    primo=1

print(primo)

