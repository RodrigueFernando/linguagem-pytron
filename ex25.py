#Sejam A, B e C os três lados de um triângulo. 
# Faça um programa que leia o valor de três lados de um triângulo A, B e C.
#  Seu algoritmo deve informar se o triangulo é: Escaleno (todos os lados diferentes); 
# Isósceles (possui dois lados iguais); e 
# Equilátero (todos os lados iguais); 
# Não forma triângulo (quando a soma de dois lados é menor que o terceiro lado).

a = int(input())
b = int(input())
c = int(input())

if a + b < c or   a + c < b or  c+ b < a:
    print("INVALIDO")
else:
    if a != b and a != c and b != c:
     print("ESCALENO")

    elif a == b and b== c:
     print("EQUILATERO")

    if a == b != c or b == c != a or a==c !=b:
     print("ISOSCELES")
        


    

    

