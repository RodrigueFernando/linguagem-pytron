

#dimensoes = input('dimensão').split()

linhas =3 #int(dimensoes[0])
colunas = 3#int(dimensoes[1])



matriz = [0] * linhas
for i in range(linhas):
 matriz[i] = [0] * colunas

valores = [int(i) for i in input("valores").split()]
print(valores)
m = valores[0]


for lin in range(linhas):
 for col in range(colunas):

   matriz[lin][col] = m
   m += 1


print(matriz)