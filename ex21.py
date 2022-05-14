#Faça um programa que leia os coeficientes a, b e c de
#  uma equação do segundo grau ax² + bx + c. 
# Após isso, calcule e imprima a soma das raízes da equação. 
# Se as raízes não forem reais, imprima 
# nan (use print(math.nan))
import math
a = float(input())
b = float(input())
c = float(input())

delta =   math.pow(b, 2) - 4*a*c

if delta < 0:
    print(math.nan)
elif delta == 0:
    
    x1 = (-b + math.sqrt(delta)) /(2*a)

else:
    x1 = (-b + math.sqrt(delta)) /(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)    
    soma = x1 + x2
    print("{:.2f}".format(soma))
