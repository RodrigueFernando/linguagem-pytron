#Faça um programa que leia um número inteiro positivo N.
# Após isso o programa deve ler N números inteiros e ao 
# final da leitura imprimir o maior, 
# menor e a soma dos números lidos.


menor=0
maior=0
soma=0
cont=1
n=int(input())

 
for i in range(n):

    valor=int(input())
    if cont==1:
      menor=valor
      maior=valor
    if valor <= menor:
      menor=valor
    if valor>= maior:
      maior=valor
      
    soma=soma+valor 
    cont=cont+1 
            
print(maior)      
print(menor)
print(soma)

