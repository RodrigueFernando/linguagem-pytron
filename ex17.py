#A avenida principal da cidade de Algoritmopolis possui limite de velocidade de L km/h.
#  Se o motorista ultrapassar essa velocidade, 
# é aplicado uma multa de R$ M, mais R$ A por cada km acima do limite. 
# Faça um programa que leia o limite L, o valor da multa M, 
# o valor adicional A e a velocidade V captada pelo radar e 
# informe o valor total da multa. Considere L e V sempre como números inteiros. 
# Apresente a resposta com duas casas decimais.

limite     = int(input())
valor_multa= float(input())
valor_adicional= float(input())
velocidade = int(input())


if velocidade <= limite:
    baixa = 0
    print("{:.2f}".format(baixa))
else:  
    valor_adicional = valor_adicional *(velocidade - limite)
    valor_multa = valor_multa + valor_adicional


    print("{:.2f}".format(valor_multa))

   

