



 
 

casa=0  

apartamento=0  

fazenda=0  

imovel=0 

tipo_imovel=0  

 
 
 

valor_casa=0  

valor_apatamento=0  

valor_fazenda=0  

valor_imovel=0  

 
 

soma_casa=0  

soma_apartamento=0  

soma_fazenda=0  

 
 

#*****RESPOSTAS****  

soma_total=0  

valor_comissao=0  

menor_fazenda=0  

imovel_caro=0  

valor_maior=0  

faixa_valor=0  

media_valor_total=0  

media_valor_casa=0  

media_casa=0  

cont = 0 

 
qtd_imoveis= int(input('Informe quantidade de vendas:'))  

print()  

print('Para cada vendas digite:')  

print('1 - Casa')  

print('2 - Fazenda')  

print('3 - Apartamento')  

print()  

 
 

for i in range(qtd_imoveis):  

    imovel=int(input('Tipo de imovel:'))  

    if imovel == 1:  

        casa=casa+1  

        tipo_imovel=("Casa")  
        valor_imovel=float(input('Digite valor do imovel:'))  
 
    
    

    elif imovel == 2:  

        fazenda=fazenda+1  

        tipo_imovel=('Fazenda')  
        valor_imovel=float(input('Digite valor do imovel:'))  

        cont = cont + 1 
    elif imovel == 3:  

        apartamento=apartamento+1  

        tipo_imovel=('Apartamento')  
        valor_imovel=float(input('Digite valor do imovel:'))  

    print()  
    soma_total=soma_total+valor_imovel  
    if valor_imovel<=250:  

     valor_comissao=valor_comissao+(valor_imovel*0.05)  
    else:  
        valor_comissao=valor_comissao+(valor_imovel*0.08)  
    if valor_imovel>valor_maior:  

        valor_maior=valor_imovel  

        imovel_caro=tipo_imovel  

#maior que 200 menor que 350 

    if valor_imovel > 200 and valor_imovel < 350: 

        faixa_valor = faixa_valor + 1 
        media_valor_total = soma_total / qtd_imoveis 

 
  

    if cont == 1: #cont fazenda  

        menor_fazenda = valor_imovel 

    if imovel == 2:  
        if valor_imovel < menor_fazenda:
            print()
    print('A fazenda mais barata é: ', menor_fazenda)   
 
    
    print('-'*50) 
    print('O valor total das vendas:R${:.2f}'.format(soma_total))  
    print('O valor da comissão:R${:.2f}'.format(valor_comissao))  
    print('O imovel mais caro é {} seu valor é {}'.format(imovel_caro, valor_maior ))  
    print(faixa_valor,'imoveis variam entre R$200,000.00 e R$350,000.00') 
    print('O preço médio dos imoveis é:', media_valor_total) 
    #print("Qantidade de casas vendinda:",casa)  
    #print("Valor total das casa:""{:.3f}".format(soma_casa)) 

 