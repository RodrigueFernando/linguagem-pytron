import math 
L=float(input())
A=float(input())
c=float(input())
m=float(input())

latas=math.ceil((L*A)/m)
c=c*latas

print("{}".format(latas))
print("{:.2f}".format(c))