import math

#Faça um programa que leia um número inteiro E de eleitores de um município,

# um número inteiro B que representa o número de votos brancos, um número N de votos nulos 

# e um número V de votos válidos. O programa deve calcular e escrever o percentual que 

# cada um representa em relação ao total de eleitores,

# além da porcentagem de ausentes. Formate sua saída conforme exemplos abaixo.

e=int(input())

b=int(input())

n=float(input())

v=float(input())

nulo = (n/e) *100
valido  =(v/e) *100
ausente =(100*((e-b-n-v)) )/e

print("nulos:{:.2f}%".format(nulo))
print("brancos:{:.2f}% ".format( ((b/e)*100)))
#print("brancos: %.2f "% ((b/e)*100))
print("validos:{:.2f}%".format(valido))

print("Ausentes:{:.2f}%".format(ausente))

