
import math
a=float(input())
b=float(input())
c=float(input())

delta=math.pow(b,2)-(4*a*c)

x1=((-b)+math.sqrt(abs(delta)))/(2*a)
x2=((-b)-math.sqrt(abs(delta)))/(2*a)

print("{:.2f}".format(x1))
print("{:.2f}".format(x2))