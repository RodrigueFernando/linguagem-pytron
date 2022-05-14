#Faça um algoritmo que leia 3 valores inteiros
#  A, B e C. Coloque-os em ordem crescente
#  (ou seja, ao final A deve armazenar o menor valor, 
# C o maior e B o valor do meio). 
# Utilize o modelo abaixo apresentado no final do exercício, 
# modificando apenas o processamento
# ENTRADA:
a = int(input())
b = int(input())
c = int(input())

# PROCESSAMENTO:
if a > b  and a > c:
    aux = a
    a   = c
    c   = aux
elif b > c:
    aux = b
    b = c
    c = aux     

if a > b:
    aux = a
    a   = b
    b   = aux

           
    
# SAIDA:
print(a)
print(b)
print(c)