
casa=0   
apartamento=0 
fazenda=0 
imovel=0

tipo_imovel=0 
imovel_caro=0
faixa_valor=0

valor_imovel=0 
valor_comissao=0
valor_maior=0 

soma_casa=0 
soma_total=0
media_valor_total=0 
menor_fazenda=0
media_casa=0 
cont=0

qtd_imoveis= int(input('Informe quantidade de vendas:'))  
print('-'*50) 
print('Para cada tipo de venda digite um desses valores:') 
print('1 - Casa') 
print('2 - Fazenda') 
print('3 - Apartamento') 
print('-'*50)  

for i in range(qtd_imoveis): 
  imovel=int(input('Tipo de imovel:')) 

  valor_imovel=float(input('Digite valor do imovel:'))  
  print() 

 
  if imovel == 1:  
    casa = casa + 1  
    tipo_imovel = ("Casa")
    soma_casa = soma_casa + valor_imovel

  elif imovel == 2:  
    fazenda = fazenda+1 
    if cont == 0:  
        cont=cont+1
        menor_fazenda = valor_imovel

    tipo_imovel = ('Fazenda')
    if valor_imovel < menor_fazenda: 
      menor_fazenda = valor_imovel

  elif imovel == 3: 
    apartamento = apartamento + 1  
    tipo_imovel = ('Apartamento') 
 
  if valor_imovel <= 250000:  
    valor_comissao = valor_comissao+(valor_imovel*0.05)  
  else: 
    valor_comissao = valor_comissao+(valor_imovel*0.08) 

  if valor_imovel > valor_maior: 
    valor_maior = valor_imovel 
    imovel_caro = tipo_imovel 

  if valor_imovel > 200000 and valor_imovel < 350000:
    faixa_valor = faixa_valor + 1

  soma_total = soma_total + valor_imovel 
  

media_valor_total = soma_total / qtd_imoveis  
    
if casa > 0:  
  media_casa = soma_casa // casa 
  
print('-'*50)      

print('O valor total das vendas: R${:.2f}'.format(soma_total)) 

print('O valor da comissao: R${:.2f}'.format(valor_comissao)) 

print('O imovel mais caro  {} seu valor : R${' ':.2f}'.format(imovel_caro, valor_maior )) 

print('A fazenda mais barata : R${:.2f} '.format(menor_fazenda))

print(faixa_valor,' imoveis variam entre R$200,000.00 e R$350,000.00')

print('O preço medio dos imoveis : R${:.2f}'.format(media_valor_total))

print('A media do valor das casas : R${:.2f}'.format(media_casa))
