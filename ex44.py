#Considere que seu computador só consegue realizar operações de soma ou subtração, 
#ou seja, está com as operações de divisão e multiplicação inoperantes. 
# Faça um programa que leia dois números inteiros positivos A e B, 
# onde A é a base e B é o expoente de uma potência. Após isso, 
#calcule o valor da potência sem utilizar as operações inoperantes. 
#Imprima o valor de A elevado a B

A=int(input())
B=int(input())
potencia=0
cont=0
cont =A
if B==0:
    cont=1
else:
    for i in range(B-1):
        for j in range(A):
            potencia=potencia+cont

        cont=potencia
        potencia=0
print(cont)
