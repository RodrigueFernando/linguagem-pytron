qtd_imoveis= int(input('Informe quantidade de vendas:'))  

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
  

print() 
print('Para cada tipo de venda digite um desses valores:') 
print('1 - Casa') 
print('2 - Fazenda') 
print('3 - Apartamento') 
print()  


for i in range(qtd_imoveis): 
  imovel=int(input('Tipo de imovel:')) 
  if imovel == 1:  
    casa=casa+1  
    tipo_imovel=("Casa")
    
    

  elif imovel == 2:  
    fazenda=fazenda+1 
    tipo_imovel=('Fazenda')
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

  if valor_imovel > 200000 and valor_imovel < 350000:
    faixa_valor = faixa_valor + 1

  media_valor_total = soma_total / qtd_imoveis
  

  if cont == 1:  
    menor_fazenda = valor_imovel
  if imovel == 2: 
    if valor_imovel < menor_fazenda: 
      menor_fazenda = valor_imovel

  if imovel == 1:
    soma_casa = soma_casa + valor_imovel
    
if casa > 0:  
  media_casa = soma_casa // casa 
 
  
print('-'*50)      

print('O valor total das vendas:R${:.2f}'.format(soma_total)) 

print('O valor da comissão:R${:.2f}'.format(valor_comissao)) 

print('O imovel mais caro é {} seu valor é R${}'.format(imovel_caro, valor_maior )) 

print('A fazenda mais barata é:R${:.2f} '.format(menor_fazenda))

print(faixa_valor,'imoveis variam entre R$200,000.00 e R$350,000.00')

print('O preço médio dos imoveis é:R${:.2f}'.format(media_valor_total))

print('A média das casas é:R${:.2f}'.format(media_casa))
