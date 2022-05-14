#Faça um programa que leia três números inteiros
# A, B e C e imprima o maior deles.
A = int(input())
B = int(input())
C = int(input())

if A > B and A >C:
    print(A)
else:
    if B > A and B > C:
        print(B)
    else:
        print(C)    

