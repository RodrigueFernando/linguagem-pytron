pinos = []
pino_derrubados = []
pontos = []
somas = 0
entrada = 0
jogadas = []
lance = 100
cont = 1
lista = []
lista2 = []
i = 0
j = 20
soma = 0
tamanho = 0

while i < j:
    frame = input("jogada {}:".format(i + 1))
    jogadas.append(frame)
    lista.append(frame)
    y = int(jogadas[i])
    if (y == 10 and j > 11):
        j = j - 1
    if (y == 10 and i == 10 and j == 11):
        j = j + 1
    if (y == 10 and i == 18):
        j = j + 2
    if (i == 19 and j == 21) or (i == 19 and j == 20 and y == 10):
        j = i
    i = i + 1
    # COLOCAR O IF PARA O CASO DE TIRAR 10 NO ULTIMO
# lista.append(frame)
print(len(jogadas))
i = 0
if len(jogadas) == 12:
    while cont < 19:
        lista.append(cont)
        cont = cont + 1
    while i < 30:
        if i <= 25:
            lista[i] = ('x')
            lista[i + 1] = ("_")
            lista[i + 2] = ("|")
            i = i + 3
        else:
            lista[i] = ('x')
            i = i + 1
    print(lista)
    print(300)

z = 0
while z < (30):
    entrada = int(jogadas[z])
    cont = int(jogadas[z - 1])
    soma = soma + entrada
    # if i>3 and

    if z >= 1 and cont != 10 and entrada + cont == 10:
        print("SOBRESSALENTE");
        lista[z] = "/"
        lista[z + 1] = ("|")
        z = z + 2
    else:
        z = z + 1
print(lista)
