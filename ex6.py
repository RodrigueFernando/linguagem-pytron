#Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas. 
# Faça um programa que leia o valor total da compra e um valor de desconto 
# (de 0 a 100, representando a porcentagem de desconto). 
# O programa de escrever o valor da compra com o desconto aplicado. 
# Escreva a saída com duas casas decimais.
# ENTRADA:
a=float(input())
b=float(input())

# PROCESSAMENTO:
porcentagem =(b/100)
desconto =a*porcentagem 
total=a*(1-porcentagem )


print("{:.2f}".format(total))
#print("{:.2f}".format(porcentagem))