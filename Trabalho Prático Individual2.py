n=int(input("digite o valor de N:"))
maior=0

for i in range(n):
    valor=int(input("informe  {}:".format(i+1)))
    
    if i==1:
        maior= valor
    elif maior<valor:
         maior =valor
  


print(maior)           