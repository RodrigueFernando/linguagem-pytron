# ENTRADA:
a = float(input()) 
b = float(input())
# PROCESSAMENTO:
res=(a+b)/2
 # SAIDA:
print("{:.2f}".format(res))


def mes(d):
    mes = int(d.mes)
    dia = int(d.dia)
    res=False
    if(mes == 1  or mes==3 or mes==5 or mes==7 or mes== 8 or mes == 10  or mes==12):
        if (dia > 0 and  dia <=31):
            res=True
    return  res

def bissexto(d):
    ano =int(d.ano)
    dia = int(d.ano)
    if ano % 4 == 0 or ano % 400 == 0:
        if d.dia <= 29 and d.dia > 0:
            res = True
    else:
        if dia <= 28 and dia > 0:

         res = True
        else:
          res =False
    return res
#n=int(input("informe n"))

d.dia = input("informe o dia:")

def bissexto(d):

    for i in lista_data:

        ano =int(d.ano)
        dia = int(d.ano)
    if comparar(d) == True:
        if ano % 4 == 0 or ano % 400 == 0:
            Ano =True
            print("entrou1")
            if d.dia <= 29 and d.dia > 0:
                Dias_29 = True
                print("entrou2")
            elif dia <= 28 and dia > 0:
                 dias_28 =True
            print("entrou3")
            if( Ano == Dias_29 == dia_28 == True):
                print(i.dia, 'de', i.mes, 'de', i.ano)
                print("entrou4")
            else:
                print("DATA INVALIDA")
comparar(d)
bissexto(d)


def gerencia_poupanca():
    opcao ='x'
    while opcao != '0':
        opcao =menu()
        if opcao == '1':
            invertimento(lista_cliente)
        elif opcao == '2':
            renta_poupanca(lista_cliente)
        elif opcao == '0':
            print("voltar")



def invertimento(lista_cliente):

#---------------------------------
def rendi_poupanca(lista_cliente):
    p=Cliente()
    valor = int(p.valor)
    tempo = float(p.tempo)
    juros = ((0.59 / 30) * 100)
    redimento = (((valor * juros)/100) *tempo)
    print("poupança", redimento)



def main():
    lista_cliente=[]
    opcao= 'x'
    while opcao!='0':
       opcao = menu()
       if opcao == '1':
        invertimento(lista_cliente)
       elif opcao == '2':
           lci(lista_cliente)
           print("desenvolvendo")
       elif (opcao == '3'):
           print("desenvolvendo")
       elif opcao == '0':
           print(" volte  sempre")
       else:
           print("opcao errada!!! tente novamnente")

main()
def poupanca():
    print(" informe o valor rendimento---1 ")
    print(" calcular-------------------2")
    print("voltar--------------------0")
    op =input(".")
    return op
def gerencia_poupanca(lista_cliente):
    opcao ='z'
    if opcao !='0':
       opcao= poupanca()
    elif opcao == '1':
        investimento_poupanca(lista_cliente)
    elif opcao =='2':
       calcula_poupanca(lista_cliente)
    elif opcao == '0':
        print("en")
    else:
        print("volte sempre")


def investimento_poupanca(lista_cliente):
    c = Cliente()
    capital = []
    capital = input("qual é valor do invertimento: ").split(" ")
    c.valor = (capital[0])
    c.tempo = (capital[1])
    lista_cliente.append(c)

def calcula_poupanca(lista_cliente):
    p = Cliente()
    valor = int(p.valor)
    tempo = float(p.tempo)
    juros = ((0.59 / 30) * 100)
    redimento = (((valor * juros) / 100) * tempo)
    print("poupança", redimento)


def main():
    lista_cliente=[]

    opcao ='x'
    while opcao != 0:
        opcao= menu()
        if opcao =='1':
            gerencia_poupanca(lista_cliente)
        elif opcao =='2':
            print()





main()
