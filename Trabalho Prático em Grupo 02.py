

qtd_imoveis= int(input('informe quantidade de vendas:')) 

i=0  

casa=0  

fazenda=0  

apartamento=0  

carro=0  

Comissao=0 
somaCasa=0
valorCasa=0
valorFazanda=0
fazenda=0
apartamento=0


for i in range(qtd_imoveis):
    imovel=int(input('Infome tipo de imovel: 1- Casa, 2- Fazenda, 3- Apartamento, 4- Carro')) 
    if imovel ==1:
        casa=casa+1
        ValorCasa=float(input("digite o valor da casa:"))
        somaCasa= somaCasa+ValorCasa
        
    elif imovel == 2 :
        fazenda = fazenda +1
        valorFazanda=float(input("digite o valor da casa:"))
        somaFazenda = somaFazenda+ valorFazanda
        
        fazenda = fazenda +1
    elif imovel ==3:
        somaAp=0
        apartamento =apartamento+1
        valorAp=float(input("digite o valor da casa:"))
        somaAp=somaAp+valorAp

    

print("Valor total :{:.2f}".format(somaCasa)) 
print("Quantidade de casa vendidas:{}".format(casa)) 
print("imovel",imovel)

       


   