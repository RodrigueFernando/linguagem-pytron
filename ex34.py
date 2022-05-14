#sequencia de fibonacci
nr=int(input())

anterior = 0
prox = 1
i=1
cont=0


if nr<=0:
  print("")

#print(' {}'.format(prox),end='')
print(prox ,end=' ')
while i<nr:
    cont = anterior+prox
    #print(' {}'.format(cont),end='')
    print(cont, end= ' ')

    anterior = prox
    prox=cont
    i+=1




  