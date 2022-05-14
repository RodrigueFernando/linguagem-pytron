from datetime import datetime
now = datetime.now()
def menu():
    print("Gerencia Veiculos")
    print("   Inserir veiculo......1")
    print("   Listar  Veiculos......2")
    print("   Pesquisar veiculos....3")
    print("   Atualizar lista.......4")
    print("   Remover veiculos........5")
    print("Sair do Programa...........0")

    opcao = input("->")
    return opcao

def busca(lista,elem):
    i=0
    while i< len(lista):
     if lista[i] == elem:
         return i
     i= i+1
    return -1
#-----------------------------------------------------------------------
def inserir_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos):
    v_codigo= input("informe o codigo:")
    if busca(veiculos_codigo,v_codigo)==-1:from datetime import datetime
    now = datetime.now()
#-----------------------------------------------
def busca_verificar(lista, elem):
    i = 0
    while i < len(lista):
        if lista[i] == elem:
            return i
        i = i + 1
    return -1
#-----------------------------------------------

def cadastar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):
    v_codigo = input("Informe o codigo: ")
    
    if busca_verificar(veiculos_codigo, v_codigo) == -1:
        v_modelo = input("Informe o modelo: ")
        v_ano = int(input("Informe o ano de fabricacao: "))
    
        veiculos_codigo.append(v_codigo)
        veiculos_modelo.append(v_modelo)
        veiculos_ano.append(v_ano)
        print("\nVeiculo codigo: " + v_codigo + ", modelo: " + v_modelo + ", ano: " + str(v_ano) + " inserido com sucesso")
    else:
        print("Codigo " + v_codigo + " ja esta cadastrado!")
#------------------------------------------------
def cadastar_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento):
    cli_codigo = input("Informe o codigo: ")
    
    if busca_verificar(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento) == -1:
        cli_cpf = int(input("Informe o CPF: "))
        cli_nome = input("Informe o nome:")
        cli_nascimento = int(input("Informe o ano de nascimento: "))
        
    
        cliente_codigo.append(cli_codigo)
        cliente_cpf.append(cli_cpf)
        cliente_nome.append(cli_nome)
        cliente_nascimento.append(cli_nascimento)
        print("\nCliente codigo: " + cli_codigo + ", CPF: " + cli_cpf + ", Nome: " +cli_nome + "ano de nascimento:"+ str(cli_nascimento)+" inserido com sucesso")
    else:
        print("Codigo " + cli_codigo + " ja esta cadastrado!")
#------------------------------------------------
def gerenciador_submenu_cli_relatorio():
  opcao_submenu_cliente = 'x'
  while opcao_submenu_cliente != '0':
    opcao_submenu_cliente = submenu_cli_relatorio()
    if opcao_submenu_cliente == '1':
      print('desenvolvendo')
      #lista_idade
    elif opcao_submenu_cliente == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")
    
#-------------------------------------------------
def gerenciador_submenu_veic_relatorio():
  opcao_submenu_veiculo = 'x'
  while opcao_submenu_veiculo != '0':
    opcao_submenu_veiculo = submenu_veic_relatorio()
    if opcao_submenu_veiculo == '1':
      print('desenvolvendo')
      #lista_modelo
    elif opcao_submenu_veiculo == '2':
      print('desenvolvendo')
      #lista_modelo_quantidade
    elif opcao_submenu_veiculo == '3':
      print('desenvolvendo')
      #lista_tempo    
    elif opcao_submenu_veiculo == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!") 

#-----------------------------------------------
def submenu_veic_relatorio():
  print("\n**********************************")
  print("Gerenciar Relatorios Veiculo")
  print("   Listar por Modelo................1")
  print("   Listar por Modelo e Quantidade...2")
  print("   Listar por Tempo.................3")
  print("Sair do Programa....................0")
  op = input("-> ")
  return op

#-----------------------------------------------
def submenu_cli_relatorio():
  print("\n**********************************")
  print("Gerenciar Relatorios Clientes")
  print("   Listar por Idade...........1")
  print("Sair do Programa...............0")
  op = input("-> ")
  return op
#-----------------------------------------------
def gerenciador_relatorio():
  opcao_relatorio = 'x'
  while opcao_relatorio != '0':
    opcao_relatorio = menu_relatorios()
    if opcao_relatorio == '1':
      gerenciador_submenu_veic_relatorio()
    elif opcao_relatorio == '2':
      gerenciador_submenu_cli_relatorio() 
    elif opcao_relatorio == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!") 

#-----------------------------------------------
def gerenciador_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano):

  opcao_veiculo ='x'
  while opcao_veiculo != '0':
    opcao_veiculo = menu_veiculo()
    if opcao_veiculo == '1':
      cadastar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '2':
      print('desenvolvendo')
      #listar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '3':
      print('desenvolvendo')
      #remover_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '4':
      print('desenvolvendo')
      #pesquisar_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano)
    elif opcao_veiculo == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")  
       
#-----------------------------------------------
def gerenciador_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento):
  opcao_cliente ='x'
  while opcao_cliente != '0':
    opcao_cliente = menu_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    if opcao_cliente =='1':
      cadastar_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '2':
      print("desenvolvendo")
      #listar_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '3':
      print('desenvolvendo') 
      #remover_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '4':
      print('desenvolvendo')
     # pesquisar_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao_cliente == '0':
      print( )
    else:
      print("Opcao invalida!!! Escolha novamente!") 

#-----------------------------------------------
def menu_relatorios():
  print("\n**********************************")
  print("Gerenciar Relatorios")
  print("   Relatorios Carros...........1")
  print("   Relatorios Cliente..........2")
  print("Sair do Programa...............0")
  op = input("-> ")
  return op

#-----------------------------------------------
def menu_veiculo():
    print("\n**********************************")
    print("Gerenciar Veiculos")
    print("   Cadastrar Veiculo...........1")
    print("   Listar Veiculos.............2")
    print("   Pesquisar Veiculo...........3")
    print("   Remover Veiculo.............4")
    print("Sair do Programa...............0")
    op = input("-> ")
    return op

#-----------------------------------------------
def menu_cliente():
    print("\n**********************************")
    print("Gerenciar Cliente")
    print("   Cadastrar Cliente............1")
    print("   Listar Cliente...............2")
    print("   Pesquisar Cliente............3")
    print("   Remover Cliente..............4")
    print("Sair do Programa................0")
    op = input("-> ")
    return op

#-----------------------------------------------
def menu_principal():
    
    print("\nBem vindos a AF Locadora!")
    print(now.day,'/',now.month,'/',now.year,'  ',now.hour,':',now.minute,)
    print("\n**********************************")
    print("Escolha uma opcao:")
    print("   Gerenciar Veiculos..........1")
    print("   Gerenciar Clientes..........2")
    print("   Gerenciar Relatorios........3")
    print("   Sair do Programa............0")
    op = input("-> ")
    return op

#-----------------------------------------------
def main():
  veiculos_codigo    = []
  veiculos_modelo    = []
  veiculos_ano       = []
  cliente_codigo     = []
  cliente_cpf        = []
  cliente_nome       = []
  cliente_nascimento = []
  
  opcao = 'x'
  while opcao != '0':
    opcao = menu_principal()
    if opcao == '1':
      gerenciador_veiculo(veiculos_codigo, veiculos_modelo, veiculos_ano) 
    elif opcao == '2':
      gerenciador_cliente(cliente_codigo, cliente_cpf, cliente_nome,cliente_nascimento)
    elif opcao == '3':
      gerenciador_relatorio()  
    elif opcao == '0':
      print("Obrigado por usar nosso programa!!!")
    else:
      print("Opcao invalida!!! Escolha novamente!")

#-----------------------------------------------

# Programa principal
main()

        v_modelo=input("informe o modelo:")
        v_ano=int(input("informe o ano de fabricação:"))
        print("\nVeiculos codigos: " + v_codigo  + " modelo: "+ v_modelo  + 
        "ano: " + str(v_ano) + "\ninseri com sucesso  ")

        veiculos_codigo.append(v_codigo)
        veiculos_modelos.append(v_modelo)
        veiculos_anos.append(v_ano)
    else:
        print("Codigo:"+v_codigo +" ja  esta cadastrado!")
#-------------------------------------------------------------

def lista_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos):
   for i in range(len(veiculos_modelos)):
       v_codigo =veiculos_codigo[i]
       v_modelo =veiculos_modelos[i]
       v_ano    =veiculos_anos[i]
       print("\nVeiculos codigos: " + v_codigo  + "\n modelo: "+ v_modelo  + 
       "\n ano: " + str(v_ano)) 

#---------------------------------------------------------------------
def pesquisar_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos):

   codigo_pesquisa=input("informe o codigo  da pesquisa:")
   indice= busca(veiculos_codigo,codigo_pesquisa)
   

   if indice != -1:
       v_codigo= veiculos_codigo[indice]
       v_modelo= veiculos_modelos[indice]
       v_ano   = veiculos_anos[indice]
       print("\nVeiculos codigos: " + v_codigo  + "\n, modelo: "+ v_modelo + 
        "\nano: " + str(v_ano))

def atualizar_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos):
    codigo_atualizar = input("informe o codigo do veiculo a ser atualizado")
    indice= busca(veiculos_codigo,codigo_atualizar)
    if indice != -1:
        v_modelo = input("informe o novo modelo:")
        v_ano    = input("informe o novo ano de fabricação:")
        veiculos_modelos[indice] =v_modelo
        veiculos_anos[indice]= v_ano
        print("\nVeiculo atualizado com sucesso")
    else:
        print("\nVeiculo codigo"+codigo_atualizar + "nao encontrado")


        
def remover1(lista,indice):

    #remove deslocando o elemento
    i=indice
    while i< len(lista)-1:
        lista[i] = lista[i +1]
        i=i+1
    lista.pop()

def remover2(lista,indice):
    #remove colocando o ultimo elemento mo posição que eu quero remover
    ultimo_indice = len(lista)-1
    lista[indice]=lista[ultimo_indice]
    lista.pop()
def remover_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos):  
    codigo_remover=input("informe o codigo do veiculo a ser removido")
    indice= busca(veiculos_codigo,codigo_remover)    
    if indice !=-1: 
        remover1(veiculos_codigo,indice) 
        remover1(veiculos_modelos,indice)
        remover1(veiculos_anos,indice)
        print("\nVeiculo removido com sucesso")
    else:
        print("\nVeiculo codigo" + codigo_remover + "não encotrado") 
    
#----------------------------------------------------------------------
def main():
    veiculos_codigo=[]
    veiculos_modelos=[]
    veiculos_anos=[]
    opcao = -1
    while opcao !="0":
        opcao=menu()
        if opcao== '1':
            print('Inserir veiculos')
            inserir_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos)
        elif opcao== '2':
            lista_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos)
        elif opcao == '3':
             pesquisar_veiculos(veiculos_codigo,veiculos_modelos, veiculos_anos)
        elif opcao =='4':
             atualizar_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos)
        elif opcao=='5':
            remover_veiculos(veiculos_codigo ,veiculos_modelos,veiculos_anos)
            
        elif opcao == '0':
            print("Obrigado por usar nosso programa")

        else:
            print("Opcao invalida!!!")
main()
