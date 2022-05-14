#Ana gosta muito de matemática e de brincar com números.
# Ela definiu o conceito de "Número da Ana.
# Se um número inteiro não negativo N é produto
# de três números inteiros consecutivos então N é um "Número da Ana".

#Faça um programa que leia um número inteiro
# não negativo N e imprima "S" se for um
# "Número da Ana" e "N" caso contrário.
# Por exemplo, 120 é um "Número da Ana",
# pois é resultado da multiplicação 4 x 5 x 6.
i=0
cont=0
n = (input("numero"))
while i > cont:
    lista = n.split()

    n1 = int(lista[0])
    n2 = int(lista[1])
    n3 = int(lista[2])
    if n == n:
        cont = len(lista)

total = (n1 *n2) *n3
def imprimir(n,total):
    if n == total:
        print("S")
    else:
        print("N")

imprimir(n,lista)