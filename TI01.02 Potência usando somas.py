
potencia= 0

A=int(input())
B=int(input())
cont =A
if B==0:
    cont=1
else:
    for i in range(B-1):
        for j in range(A):
            
            potencia=potencia+cont
        cont=potencia
        potencia=0
print(cont)


