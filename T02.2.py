#Faça um programa que leia um valor inteiro N. Após isso, 
# leia N valores inteiros. Em seguida leia um número inteiro X. 
# Ao fim escreva o número de vezes que o número X foi lido do usuário.
from datetime import datetime
now = datetime.now()
veiculos_ano = ['1999', '2000', '1998', '1998','2021']
idade = 0
memoria = 0
ano_atual = now.year
i =0
 
while i < len(veiculos_ano):
    ano = int(veiculos_ano[i])
    idade = ano_atual - ano
    if memoria == 0:
        memoria = idade
    if idade >= memoria:
        print (veiculos_ano[i])
        memoria =idade    
    
    i = i + 1
 
print(memoria)