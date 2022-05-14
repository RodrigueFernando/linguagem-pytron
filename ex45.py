#Faça um programa que leia um conjunto de valores que correspondem as idades
# de pessoas de uma comunidade. Quando o valor fornecido for um número negativo, 
# significa que não existem mais idades para serem lidas. Após a leitura, 
# seu programa deve informar
#A média das idades das pessoas (com duas casas decimais)
#A quantidade de pessoas maiores de idade
#A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) 
# (com duas casas decimais
media=0
maior_idade=0
idosas=0
porg=0
i=0 
idade=1
cont=-1
total_idade=0


while  idade  > 0:
   idade=int(input(""))
   if idade > 0:
     total_idade=total_idade+idade
  
   if idade >18:
       maior_idade=maior_idade+1
   if idade > 75:
       idosas=idosas+1

   i=i+1 
   cont=cont+1                                                                          
   
   
porg=(idosas/cont)*100
#total_idade=total_idade+1
media=((total_idade/cont))

print("{:.2f}".format(media))
print(maior_idade)
print("{:.2f}%".format(porg))
