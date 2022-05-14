#Faça um programa que leia um número inteiro N e imprima a 
# soma de todos os fatoriais entre 0 e N (inclusive N). 
# Não utilize bibliotecas matemáticas.

fat=1
n=0
soma=1
n=int(input())
for i in range(1,n+1):
 
    fat = fat*i
    soma=soma+fat
   
print(soma)  
    

