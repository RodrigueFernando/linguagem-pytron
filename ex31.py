#Faça um programa que leia um número natural N e imprima o número harmônico de ordem N. 
# Um número harmônico H é definido por:
#H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

nr = int(input())
i=1
h=0
while i <= nr:
   
    h= 1+(1/i)
    i=i+1
   
print("i",i)   
print(h)