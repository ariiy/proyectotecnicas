def calculoMontecarloLista(v, f, n):
    valor = []
    frecuencia = []
    numeros_aleatoreos = []
    for item1 in v:
        valor.append(float(item1))

    for item2 in f:
        frecuencia.append(float(item2))

    for item3 in n:
        numeros_aleatoreos.append(float(item3))

    l_acumulada = []
    l_desde = [0]
    l_valor_simulado = []
    acumulada = 0.0
    suma = 0.0
    promedio = 0.0
    contador = 0
    for fre in frecuencia:
        acumulada = round(acumulada + frecuencia[contador], 3)
        l_acumulada.append(acumulada)
        contador = contador + 1

    contador_d = 0
    for des in l_acumulada:
        l_desde.append(round(l_acumulada[contador_d] + 0.001, 3))
        contador_d = contador_d + 1

    conrador3 = 0
    rango = len(numeros_aleatoreos)
    for nu in range(0, rango):
        valor_simulado = calculo(numeros_aleatoreos[conrador3], l_desde, l_acumulada, valor)
        l_valor_simulado.append(valor_simulado)
        suma = suma + valor_simulado
        conrador3 = conrador3 + 1
    print(valor, frecuencia, l_acumulada, l_desde, l_acumulada,)

    promedio = round(suma / len(numeros_aleatoreos), 3)
    return valor, frecuencia, l_acumulada, l_desde, l_acumulada


def calculoMontecarlo(v, f):
    valor = []
    frecuencia = []
    # numeros_aleatoreos=[]
    for item1 in v:
        valor.append(float(item1))

    for item2 in f:
        frecuencia.append(float(item2))

    # for item3 in n:
    #    numeros_aleatoreos.append(float(item3))


    l_acumulada = []
    l_desde = [0]
    l_valor_simulado = []
    acumulada = 0.0
    suma = 0.0
    promedio = 0.0
    contador = 0
    for fre in frecuencia:
        acumulada = round(acumulada + frecuencia[contador], 3)
        l_acumulada.append(acumulada)
        contador = contador + 1

    contador_d = 0
    for des in l_acumulada:
        l_desde.append(round(l_acumulada[contador_d] + 0.001, 3))
        contador_d = contador_d + 1

    # conrador3=0
    # rango=len(numeros_aleatoreos)
    # for nu in range(0, rango):
    #    valor_simulado=calculo(numeros_aleatoreos[conrador3],l_desde,l_acumulada,valor)
    #    l_valor_simulado.append(valor_simulado)
    #    suma=suma+valor_simulado
    #    conrador3=conrador3+1
    # print(valor,frecuencia,l_acumulada,l_desde,l_acumulada,)

    # promedio=round(suma/len(numeros_aleatoreos),3)
    return valor, frecuencia, l_acumulada, l_desde, l_acumulada


def calculo(numero_aleatoreo, lista_desde, lista_hasta, lista_valor):
    valor_simulado = 0

    for i in range(0, len(lista_valor)):
        if numero_aleatoreo >= lista_desde[i] and numero_aleatoreo < lista_hasta[i]:
            valor_simulado = lista_valor[i]
    # print(valor_simulado)
    return valor_simulado


def inventarioMonte(R, Q, Inv, Co, Ch, Cf, Valor1Monte, Probabilidad1, valor2Monte, Probabilidad2, aleatorio_demanda,
                    aleatorio_retraso):
    r = R
    q = Q
    inv = Inv
    co = Co
    ch = Ch
    cf = Cf

    valor = Valor1Monte
    px = Probabilidad1

    valor1 = valor2Monte
    px1 = Probabilidad2

    deman = aleatorio_demanda
    retra = aleatorio_retraso

    demanda = calculoMontecarlo(valor, px)
    retraso = calculoMontecarlo(valor1, px1)

    # print(demanda,retraso)
    lista_valor = demanda[0]
    lista_desde = demanda[3]
    lista_hasta = demanda[4]

    lista_valor1 = retraso[0]
    lista_desde1 = retraso[3]
    lista_hasta1 = retraso[4]

    bandera = 0
    entrega = 0
    banfalta = 0
    fin = inv
    isTheDay = 0
    lista_total = []
    print("Semana", "ri", "demanda", "inicial", "ingresos", "final", "faltante", "mantener", "ordenar", "ri",
          "tiempo de entrega", "dia entrega")
    for i in range(0, len(deman)):
        n = i + 1
        # metodo montecarlo al primer valor aleatorio
        vardeman = calculo(deman[i], lista_desde, lista_hasta, lista_valor)
        # inicial es igual al anterior
        inicial = fin
        # resa en uno
        # si valor inicial es menor a la demanda
        if inicial < vardeman:
            # final es igual a 0
            fin = 0
        else:
            # fina es igual al inv inicial - la demanda
            fin = inicial - vardeman

        # Si es el dia de entrega
        if n == isTheDay:
            print("es el dia xD")
            # realizo la entrega
            bandera = 0
            entrega = 1
            # si hay faltante y si es el dia de entrega
            if banfalta == 1:
                print('Hay faltante')
                # realizo la entrega
                # ingreso es igual a q
                ingreso = q
                # costo de ordenar un pedido
                ordenar = co
                # final es igual al ingreso menos la demanda
                fin = ingreso - vardeman
                # ya no hay faltantes
        else:
            ingreso = 0
            ordenar = 0

        if ingreso == inicial:
            print("bingo")
            if inicial < vardeman or ingreso < vardeman:
                faltante = cf
                banfalta = 1

        else:
            if inicial < vardeman:
                faltante = cf
                banfalta = 1
            else:
                faltante = 0
                banfalta = 0

        if ingreso > inicial:
            faltante = 0

        mantener = ch * fin

        if bandera == 0:
            varretra = calculo(retra[i], lista_desde1, lista_hasta1, lista_valor1)
            diaentrega = (n + varretra) + 1
            isTheDay = diaentrega
            print("Ahora el dia de entrega es el", isTheDay)
            bandera = 1
        else:
            varretra = 0
            diaentrega = 0
            # print(n,deman[i],vardeman,inicial,ingreso,fin,faltante,mantener,ordenar,retra[i],varretra,diaentrega)
        lista_total.append(
            {"n": n, "riDemanda": deman[i], "DemanMonte": vardeman, "inv": inicial, "ingresos": ingreso, "final": fin,
             "faltante": faltante, "mantener": mantener, "ordenar": ordenar, "RetraAlea": retra[i],
             "TiempoEntrega": varretra, "diaEntrega": diaentrega})
        # print("")

    return lista_total
    # print(lista_total)