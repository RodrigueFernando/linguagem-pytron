#Faça um programa que leia dois números inteiros positivos X e Y e 
# imprima todos os números de X até Y. 
# Se X for maior que Y, imprima INVALIDO.

x =int(input())
y =int(input())

if x <= 0 and y <= 0:
    print()
elif x > y:
    print("INVALIDO")
while x <= y:
    print(x)
    x = x+1