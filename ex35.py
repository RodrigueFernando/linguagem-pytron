#Faça um programa que leia dois números inteiros e imprima o máximo divisor comum (MDC) entre eles. 
# Dica: pesquise sobre o algoritmo de euclides.

mdc=1
i=2
x1=int(input())
x2=int(input())

while i < x1:
    if x1 %i==0 and x2%i==0:
     mdc=i
    i+=1
print(mdc)