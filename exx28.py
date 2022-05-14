#Faça um programa que leia dois números inteiros X e Y e 
# imprima todos os números de X até Y, seguidos nos números de Y até X.
#  Se X for maior que Y, imprima INVALIDO.
x =int(input())
y =int(input())
i = x
if x <= 0 and y <= 0:
    print(x)
elif x > y:
    print("INVALIDO")
while i <= y:
    print(i)
    i=i+1

i = y
while i >= x:
 print(i)
 i=i-1  


    
