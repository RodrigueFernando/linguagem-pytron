
def menu():

    print(" Escolha seu  invertimento")
    print(" Poupança: juros de 0.59% ao mês")
    print(" LCI: juros de 0.86% ao mês")
    print(" CDB: juros de 1.032% ao mês")
    print("________________________________")
    op =input("->")
#_________________________________________________________

capital = []
capital = input(" informe").split(" ")
valor = (capital[0])
tempo = (capital[1])


#_____________________________________________________
def investimento_poupanca(valor,tempo):

    valor = float(valor)
    tempo = int(tempo)
    juros = valor* pow((1+( 0.59/100) ),tempo)

    rentabilidade  = valor + juros
    rentabilidade  = rentabilidade -valor
    #taxa = pow(juros,tempo)


    return  rentabilidade
    #print("{:.2f}".format(rentabilidade))
#---------------------------------------------------
def investimento_lci(valor,tempo):
    tempo = int(tempo)
    valor = float(valor)
    if tempo >= 6:
         juros = valor * pow((1 + (0.86/100) ),tempo)
         rentabilidade =  valor + juros
         rentabilidade =  rentabilidade - valor
         #print( rentabilidade)
         return rentabilidade
    else:
        return valor
        #print("{:.2f}".format(valor))

#___________________________________________________________
def investimento_cdb(valor,tempo):
    valor = float(valor)
    tempo = int(tempo)
    juros = valor * pow((1 + (1.032 / 100)), tempo)
    rentabilidade =     valor + juros
    rentabilidade =  rentabilidade - valor


    if tempo > 1 and tempo <= 6:
          imposto = 22.5/100
          cont =  valor + rentabilidade
          cont2 =  imposto * rentabilidade
          valor_real =  cont - cont2
         #print("{:.2f}".format(valor_real))
          return  valor_real

    elif tempo >= 7 and tempo < 12:
        imposto = 22 / 100

        valor_real = rentabilidade - imposto
        return  valor_real
    elif tempo > 13 and tempo < 24:

        imposto = 17,5/100
        valor_real = rentabilidade - imposto
        return valor_real

    elif tempo > 24:
           imposto = 15/100
           valor_real = rentabilidade - imposto
        #print("{:. 2f}".format(valor_real))
           return valor_real



#___________________________________________________
def compara(valor,tempo):
    resultado_poupanca =    investimento_poupanca(valor,tempo)
    resultado_lci      =    investimento_lci(valor,tempo)
    resultado_cdb      =    investimento_cdb(valor,tempo)

    if resultado_poupanca > resultado_lci  and resultado_poupanca > resultado_cdb:
        print("{:.2f}".format(resultado_poupanca))
        print("{:.2f}".format(resultado_lci))
        print("{:.2f}".format(resultado_cdb))
        print("P")
    elif  resultado_lci > resultado_poupanca and resultado_lci > resultado_cdb:
        print("{:.2f}".format(resultado_poupanca))
        print("{:.2f}".format( resultado_lci))
        print("{:.2f}".format(resultado_cdb))
        print("L")
    else:
        print("{:.2f}".format(resultado_poupanca))
        print("{:.2f}".format(resultado_lci))
        print("{:.2f}".format(resultado_cdb))
        print("C")

def imprimir():
    compara(valor,tempo)
    #investimento_poupanca(valor, tempo)
    #investimento_lci(valor, tempo)
    #investimento_cdb(valor,tempo)


imprimir()