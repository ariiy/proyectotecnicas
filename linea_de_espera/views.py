# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from numeros_aleatorios.views import metodo_multiplicativo,op_metodo_lineal


# Matrices linea esperaa
numLlegadas = []
numServicio = []
msumLlegadas = []
msumServicio = []
mfrecaLlegadas = []
mfrecaServicio = []

datosLlegadas = []
datosServicio = []
mdesdeServicio = []
mdesdeLlegadas = []
mdhLlegadas = []
mdhServicio = []

matrizLlegadas = []
matrizServicio = []
xLlegadas = []
xServicio = []

mresultadoLlegadas = []
mresultadoServicio = []



invdatos = []
mLlegadas = []

mLlegadaExacta = []
mServicio = []


#absoluta
num = []
datos = []
mx = []
mprob = []
mfreca = []
mfrecd = []
mfrecda = []
mdesde = []
mfrecd2 = []
matrizNueva =[]
mfreha2 = []
mresultado = []
mnume = []
datosLlegadasA = []
datosLlegadasDemA = []
datosLlegadasProbA = []
datosServicioProbA = []
datosServicioDemA = []
smx = []
smprob = []
def linea_espera(request):
    del numLlegadas[:]
    del numServicio[:]
    del datosServicio[:]
    del datosLlegadas[:]
    del mfrecaLlegadas[:]
    del mfrecaServicio[:]
    del mdesdeServicio[:]
    del mdesdeLlegadas[:]
    del mdhLlegadas[:]
    del mdhServicio[:]

    del matrizLlegadas[:]
    del matrizServicio[:]

    del xLlegadas[:]
    del xServicio[:]

    del mresultadoLlegadas[:]
    del mresultadoServicio[:]

    del invdatos[:]
    del mLlegadas[:]

    del mLlegadaExacta[:]
    del mServicio[:]

    if request.method == 'POST':

            metodo = request.POST['metodo']

            if metodo == 'numeros':

                nLlegadas = int(request.POST['nLlegadas'])
                nServicio = int(request.POST['nServicio'])

                numeLlegadas = nLlegadas + 1
                numeServicio = nServicio + 1

                numLlegadas.append(nLlegadas)
                numServicio.append(nServicio)

                if nLlegadas <= 0 or nServicio <= 0:
                    messages.error(request, "Ingrese valores mayores a 0")

                return render(request, 'lineadeespera/index.html',
                              {'numeLlegadas': range(1, numeLlegadas), 'numeServicio': range(1, numeServicio)})

            elif metodo == 'celltunning':

                # variable para seleccion de metodo
                metodofrecuencia = request.POST['metodofrecuencia']
                metodoa = request.POST['metodoa']

                if metodofrecuencia == 'FrecuenciaAbsoluta':
                    del mprob[:]
                    del mfreca[:]
                    del datos[:]
                    del mfrecd[:]
                    del mfrecd2[:]
                    del mfreha2[:]
                    del mresultado[:]
                    del mx[:]
                    del datosLlegadasDemA[:]
                    del datosLlegadasProbA[:]
                    del datosServicioProbA[:]
                    del datosServicioDemA[:]
                    del smx [:]
                    del smprob [:]
                    valorLlegadasA = request.POST.getlist('valorLlegadasA')
                    valorServicioA = request.POST.getlist('valorServicioA')
                    demandaLlegadasA = request.POST.getlist('demandaLlegadasA')
                    demandaServicioA = request.POST.getlist('demandaServicioA')
                    sumLlegadasA = 0
                    sumServicioA = 0
                    # matriz de suma para valores de frecuencia
                    msumLlegada = []
                    # se realiza recorrido y se suman los valores de frecuencia
                    # suma de frecuencia
                    for i in range(len(valorLlegadasA)):
                        sumLlegadasA = sumLlegadasA + float(valorLlegadasA[i])
                        msumLlegada.append(sumLlegadasA)
                    for i in range(len(valorServicioA)):
                        sumServicioA = sumServicioA + float(valorServicioA[i])
                        msumLlegada.append(sumServicioA)
                    for i in range(len(valorLlegadasA)):
                        # valores de frecuencia y valores de x
                        # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                        x = int(demandaLlegadasA[i])

                        # Metodo de probabilidad
                        # se divide el valor de frecuencia sobre la suma
                        prob = float(valorLlegadasA[i]) / sumLlegadasA
                        # se guarda en matriz mprob la probabilidad
                        mprob.append(prob)
                        # se guarda en matriz mx los valores de x
                        mx.append(x)
                        # Le damos formato al float solo con 3 decimales
                        # para frecuencia HASTA
                        freh = float(mprob[i])
                        prob = round(float(freh), 3)


                        # Hacemos matriz datos y guardamos todos los datos generados
                        datosLlegadasProbA.append(prob)
                        datosLlegadasDemA.append(x)
                    for i in range(len(valorServicioA)):
                        # valores de frecuencia y valores de x
                        # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                        sx = int(demandaServicioA[i])
                        # Metodo de probabilidad
                        # se divide el valor de frecuencia sobre la suma
                        sprob = float(valorServicioA[i]) / sumServicioA
                        # se guarda en matriz mprob la probabilidad
                        smprob.append(sprob)
                        # se guarda en matriz mx los valores de x
                        smx.append(sx)
                        # Le damos formato al float solo con 3 decimales
                        # para frecuencia HASTA
                        sfreh = float(smprob[i])
                        sprob = round(float(sfreh), 3)

                        # Hacemos matriz datos y guardamos todos los datos generados
                        datosServicioProbA.append(sprob)
                        datosServicioDemA.append(sx)
                    valorLlegadas = datosLlegadasProbA
                    valorServicio = datosServicioProbA
                    demandaLlegadas = datosLlegadasDemA
                    demandaServicio = datosServicioDemA
                elif metodofrecuencia == 'FrecuenciaRelativa':
                    valorLlegadas = request.POST.getlist('valorLlegadas')
                    valorServicio = request.POST.getlist('valorServicio')
                    demandaLlegadas = request.POST.getlist('demandaLlegadas')
                    demandaServicio = request.POST.getlist('demandaServicio')

                if metodoa == 'Lineal':
                    riLlegadas = []
                    riServicio = []
                    # variables de numeros Demanda
                    a = int(request.POST['a'])
                    n = int(request.POST['n'])
                    xo = int(request.POST['xo'])
                    m = int(request.POST['m'])
                    xoinicial = xo
                    riLlegadas = metodo_multiplicativo(a, xo, xoinicial, m, n)

                    # variables de numeros Servicio
                    ab = int(request.POST['ab'])
                    nb = int(request.POST['nb'])
                    xob = int(request.POST['xob'])
                    mb = int(request.POST['mb'])
                    xoinicialb = xob
                    riServicio = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

                    print (riLlegadas,riServicio,len(riLlegadas),len(riServicio))

                elif metodoa == 'Multiplicativo':

                    # variables de numeros Llegadas
                    a = int(request.POST['a'])
                    n = int(request.POST['n'])
                    xo = int(request.POST['xo'])
                    m = int(request.POST['m'])
                    xoinicial = xo
                    riLlegadas = metodo_multiplicativo(a, xo, xoinicial, m, n)

                    # variables de numeros Servicio
                    ab = int(request.POST['ab'])
                    nb = int(request.POST['nb'])
                    xob = int(request.POST['xob'])
                    mb = int(request.POST['mb'])
                    xoinicialb = xob
                    riServicio = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

                elif metodoa == 'Manual':
                    riLlegadas = request.POST.getlist('riLlegadas')
                    riServicio = request.POST.getlist('riServicio')
                frecaLlegadas =0
                frecaServicio = 0


                # for in para tabla Llegadas, Mayor Menor y frecuencia
                for i in range(len(valorLlegadas)):
                    a = int(demandaLlegadas[i])
                    xLlegadas.append(a)

                    frecaLlegadas = frecaLlegadas + float(valorLlegadas[i])
                    Llegadas = float(valorLlegadas[i])
                    msumLlegadas.append(frecaLlegadas)

                    mfrecaLlegadas.append(frecaLlegadas)
                    hastaLlegadas = float(mfrecaLlegadas[i])
                    desdeLlegadas = float(hastaLlegadas) + 0.001

                    if mfrecaLlegadas[i] == mfrecaLlegadas[0]:
                        mdesdeServicio.insert(int(desdeLlegadas), 0)
                        mdesdeLlegadas.insert(int(desdeLlegadas), 0)
                    mdesdeLlegadas.append(desdeLlegadas)

                    datosLlegadas.append([a, Llegadas, frecaLlegadas, mdesdeLlegadas, hastaLlegadas])
                print("datosllegadas",datosLlegadas)
                # for i"n para tabla Servicio, Mayor Menor y frecuencia
                for i in range(len(valorServicio)):
                    a = int(demandaServicio[i])
                    xServicio.append(a)

                    frecaServicio = frecaServicio + float(valorServicio[i])
                    Servicio = float(valorServicio[i])
                    msumServicio.append(sum)

                    mfrecaServicio.append(frecaServicio)
                    hastaServicio = float(mfrecaServicio[i])
                    desdeServicio = float(hastaServicio) + 0.001

                    mdesdeServicio.append(desdeServicio)
                    datosServicio.append([a, Servicio, frecaServicio, mdesdeServicio, hastaServicio])
                print("datpsservicio",datosServicio)
                # montecarlo Llegadas
                for i in range(len(riLlegadas)):
                    a = i + 1
                    Llegadas = float(riLlegadas[i])
                    matrizLlegadas.append(round(Llegadas,3))
                    # recorrido para seleccionar valores de x
                    for j in range(len(mfrecaLlegadas)):
                        # hacemos un if que compare los datos con la matriz y las frecuencias DESDE y HASTA
                        # si se cumple la funcion se guardan los datos en la matriz mresultado

                        if matrizLlegadas[i] >= mdesdeLlegadas[j] and matrizLlegadas[i] <= mfrecaLlegadas[j]:
                            # se guardan los datos en la matriz , de numeros aleatorios matrizNueva[i]
                            #  y de la matriz de frecuencia mfreca[j] y matriz de valores de x mx[j]
                            mLlegadas.append(xLlegadas[j])
                            mresultadoLlegadas.append([a, matrizLlegadas[i],xLlegadas[j]])
                print("mresultadoLlegadsa",mresultadoLlegadas)
                # montecarlo Servicio
                for i in range(len(riServicio)):
                    Servicio = float(riServicio[i])
                    matrizServicio.append(round(Servicio,3))
                    # recorrido para seleccionar valores de x
                    for j in range(len(mfrecaServicio)):
                        # hacemos un if que compare los datos con la matriz y las frecuencias DESDE y HASTA
                        # si se cumple la funcion se guardan los datos en la matriz mresultado
                        if matrizServicio[i] >= mdesdeServicio[j] and matrizServicio[i] <= mfrecaServicio[j]:
                            # se guardan los datos en la matriz , de numeros aleatorios matrizNueva[i]
                            #  y de la matriz de frecuencia mfreca[j] y matriz de valores de x mx[j]
                            mServicio.append(xServicio[j])
                            mresultadoServicio.append([matrizServicio[i], xServicio[j]])
                print("Mresultado Servocop",mresultadoServicio)
                #Hora
                llegadaExacta = 0
                terServicio=0
                #Tiempos

                sumtEspera=0
                sumtSistema=0


                for i in range(len(riLlegadas)):

                 llegadaExacta = int(mLlegadas[i]) + llegadaExacta
                 if llegadaExacta <= terServicio:
                     inServicio = terServicio
                 else:
                     inServicio = llegadaExacta

                 terServicio =  int(mServicio[i]) + inServicio
                 tEspera = inServicio - llegadaExacta
                 tSistema = tEspera + int(mServicio[i])

                 mLlegadaExacta.append([llegadaExacta,inServicio,terServicio,tEspera,tSistema])
                 sumtEspera = sumtEspera + tEspera
                 sumtSistema = sumtSistema + tSistema
                promtSistema = round(float(sumtSistema) / float(len(riLlegadas)),3)
                promtEspera = round(float(sumtEspera) / float(len(riLlegadas)),3)


                mdhLlegadas.append([mdesdeLlegadas, [mfrecaLlegadas]])
                mdhServicio.append([mdesdeServicio, mfrecaServicio])
                print(mdesdeLlegadas,mdhServicio)


                return render(request, 'lineadeespera/index.html',
                              {'promtEspera':promtEspera,'promtSistema':promtSistema,
                               'sumtEspera':sumtEspera,'sumtSistema':sumtSistema,'mLlegadaExacta':mLlegadaExacta,
                               'invdatos':invdatos, 'mresultadoLlegadas': mresultadoLlegadas,'mresultadoServicio': mresultadoServicio,
                               'matrizLlegadas': matrizLlegadas, 'matrizServicio': matrizServicio,
                               'frecaServicio': mfrecaServicio, 'frecaLlegadas': mfrecaLlegadas,
                               'mdhLlegadas': mdhLlegadas,'xServicio':xServicio, 'mdhServicio': mdhServicio,
                               'datosLlegadas': datosLlegadas, 'datosServicio': datosServicio,
                               'desdeLlegadas': mdesdeLlegadas, 'desdeServicio': mdesdeServicio})

            # si ocurre un error mostrara mensaje error
            else:
                messages.error(request, "error")
            # renderizamos pagina html
            return render(request, 'lineadeespera/index.html')

    # renderizamos pagina index.html
    return render(request, 'lineadeespera/index.html', {'datosLlegadas': datosLlegadas, 'datosServicio': datosServicio})

