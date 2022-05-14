#Você está responsável pelo bolo de aniversário da sua priminha e decidiu que o bolo
# terá uma vela para cada ano da idade total dela. Quando ela assopra as velas, ela só é
# capaz de apagar apenas as velas mais altas. Sua tarefa é fazer um programa que leia a idade
# A da sua sobrinha e a altura das velas. Após isso, seu programa deve imprimir a quantidade
# de velas que ela vai conseguir apagar.

#Por exemplo, se sua sobrina está fazendo 4 anos e o bolo possui 4 velas de tamanhos 4, 4, 1, 3, então ela
# só vai conseguir apagar as duas mais altas, de tamanho 4. Portanto, a resposta deve ser 2.

idade=int(input())
tamanho=[]
max=0
pos=0
x=0
cont=0
for i in range(idade):
  vela = int(input())
  tamanho.append(vela)
x= len(tamanho)-1

for j in range(len(tamanho)-1):
  print("J",j)
  for i in range(len(tamanho)-1):
   print("i",i)
   if tamanho[j] > tamanho[i]:
       pos= tamanho[j]


for i in range(len(tamanho)):
  print("i",i)

  if pos == tamanho[i]:
    print("lista",i)
    max=max+1

print("resposta",max)
print("pos",pos)


print(lista)
#andando na lista10
def repeticao_isabela(s):
  i=0
  while i<len(s)-1:
    j=i+1
    while j<len(s):
      if s[i] == s[j]:
        return True
      j=j+1
    i=i+1
  return False