#Faça um programa que leia uma string S e imprima imprima 1 
# e ela é palíndromo e 0 caso contrário. 
# Uma string é palíndromo se quando lido da
#  esquerda para a direita é igual ao ser lido da direita para a esquerda. 
# Exemplos: "arara", "amor e roma".
#  Observações importantes:
#  1) Seu programa deve desconsiderar caracteres de espaço;
#  2) Seu programa NÃO deve criar uma string auxiliar, 
# ou seja, ele deve dizer se a string é palíndromo 
# apenas acessando/consultando seus caracteres.
cont=0
lista=[]
cont=0
i=0
j= 0
lista= input()
j = len(lista)-1

while i < len(lista):

  while lista[i] == ' ' or  lista[i] == ',':
   i = i +1   
    #and (i < len(lista)-1):       
  while  lista[j] == ' ' or lista[j] == ',':            # and j>0:
    j = j-1
 # if  lista[i]  ==  lista [j]:
  #  cont =1
  #  print("=",cont)
  if lista[i]  !=  lista [j]:
    cont=0
  else:
    cont=1
  if lista[i] != ' ' :
    i = i+1
  if lista[j] != ' ' :
    j = j-1

print(cont)