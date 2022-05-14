
potencia= 0

A=int(input("digite o valor de A:"))
B=int(input("digite o valor de B:"))
cont =A
for i in range(B-1):
   
    for j in range(A):
        
        potencia=potencia+cont
    cont=potencia
    potencia=0
print(cont)


