#Faça um algoritmo que leia 2 valores inteiros A e B.
# Coloque-os em ordem crescente
#  (ou seja, ao final A deve armazenar o menor valor e B o maior valor). 
# Utilize o modelo abaixo apresentado no final do exercício, modificando 
# apenas o processamento

A = int(input())
B = int(input())

if A==B:
    print(A)
    print(B)
if A > B:
   aux = A
   A   = B
   B   = aux

print(A)
print(B)
    