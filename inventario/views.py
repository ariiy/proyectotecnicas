# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from inventarioMontecarlo import *
from aleatorios.views import op_metodo_lineal,metodo_multiplicativo
# Create your views here.

num = []
datos = []
mx = []
mprob = []
mfreca = []
mfrecd = []
mfrecda = []
mdesde = []
mfrecd2 = []
matrizNueva = []
mfreha2 = []
mresultado = []
mnume = []

mpromedio = []
numDemanda = []
numTiempo = []
minventarioDemanda = []
minventarioValor = []
mtiempoDemanda = []
mtiempoValor = []
matrizDemanda = []
matrizTiempo = []

datosInventarioA = []
datosInventarioDemA = []
datosInventarioProbA = []
datosTiempoProbA = []
datosTiempoDemA = []
smx = []
smprob = []
def modelo_inventario(request):
    if request.method == 'POST':
        del mpromedio[:]
        del  numDemanda[:]
        del  numTiempo[:]
        del minventarioDemanda[:]
        del minventarioValor[:]
        del mtiempoDemanda[:]
        del mtiempoValor[:]
        del matrizDemanda[:]
        del matrizTiempo[:]
        #del lista_total[:]
        #del montecarloDemanda[:]
        #del montecarloRetraso[:]

        metodo = request.POST['metodo']
        if metodo == 'numeros':
            nDemanda = int(request.POST['nDemanda'])
            nTiempo = int(request.POST['nTiempo'])

            numeDemanda = nDemanda + 1
            numeTiempo = nTiempo + 1

            numDemanda.append(nDemanda)
            numTiempo.append(nTiempo)

            return render(request, 'inventario/index.html',
                          {'numeDemanda': range(1, numeDemanda), 'numeTiempo': range(1, numeTiempo)})


        elif metodo == 'inventario':
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
                del datosInventarioDemA[:]
                del datosInventarioProbA[:]
                del datosTiempoProbA[:]
                del datosTiempoDemA[:]
                del smx[:]
                del smprob[:]


                demandaInventarioA = request.POST.getlist('demandaInventarioA')
                valorInventarioA = request.POST.getlist('valorInventarioA')

                demandaTiempoA = request.POST.getlist('demandaTiempoA')
                valorTiempoA = request.POST.getlist('valorTiempoA')

                print(valorInventarioA, valorTiempoA, demandaInventarioA, demandaTiempoA)

                sumLlegadasA = 0
                sumServicioA = 0
                # matriz de suma para valores de frecuencia
                msumLlegada = []
                # se realiza recorrido y se suman los valores de frecuencia
                # suma de frecuencia
                for i in range(len(valorInventarioA)):
                    sumLlegadasA = sumLlegadasA + float(valorInventarioA[i])
                    msumLlegada.append(sumLlegadasA)
                for i in range(len(valorTiempoA)):
                    sumServicioA = sumServicioA + float(valorTiempoA[i])
                    msumLlegada.append(sumServicioA)
                for i in range(len(valorInventarioA)):
                    # valores de frecuencia y valores de x
                    # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                    x = int(demandaInventarioA[i])

                    # Metodo de probabilidad
                    # se divide el valor de frecuencia sobre la suma
                    prob = float(valorInventarioA[i]) / sumLlegadasA
                    # se guarda en matriz mprob la probabilidad
                    mprob.append(prob)
                    # se guarda en matriz mx los valores de x
                    mx.append(x)
                    # Le damos formato al float solo con 3 decimales
                    # para frecuencia HASTA
                    freh = float(mprob[i])
                    prob = round(float(freh), 3)

                    # Hacemos matriz datos y guardamos todos los datos generados
                    datosInventarioProbA.append(prob)
                    datosInventarioDemA.append(x)
                for i in range(len(valorTiempoA)):
                    # valores de frecuencia y valores de x
                    # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                    sx = int(demandaTiempoA[i])
                    # Metodo de probabilidad
                    # se divide el valor de frecuencia sobre la suma
                    sprob = float(valorTiempoA[i]) / sumServicioA
                    # se guarda en matriz mprob la probabilidad
                    smprob.append(sprob)
                    # se guarda en matriz mx los valores de x
                    smx.append(sx)
                    # Le damos formato al float solo con 3 decimales
                    # para frecuencia HASTA
                    sfreh = float(smprob[i])
                    sprob = round(float(sfreh), 3)

                    # Hacemos matriz datos y guardamos todos los datos generados
                    datosTiempoProbA.append(sprob)
                    datosTiempoDemA.append(sx)

                inventarioValor = datosInventarioProbA
                tiempoValor = datosTiempoProbA
                demandaInventario = datosInventarioDemA
                demandaTiempo = datosTiempoDemA
            elif metodofrecuencia == 'FrecuenciaRelativa':
                demandaInventario = request.POST.getlist('demandaInventario')
                inventarioValor = request.POST.getlist('valorInventario')

                demandaTiempo = request.POST.getlist('demandaTiempo')
                tiempoValor = request.POST.getlist('valorTiempo')
            if metodoa == 'Lineal':
                riLlegadas = []
                riServicio = []
                # variables de numeros Demanda
                a = int(request.POST['a'])
                n = int(request.POST['n'])
                xo = int(request.POST['xo'])
                m = int(request.POST['m'])
                xoinicial = xo
                riDemanda = metodo_multiplicativo(a, xo, xoinicial, m, n)

                # variables de numeros Servicio
                ab = int(request.POST['ab'])
                nb = int(request.POST['nb'])
                xob = int(request.POST['xob'])
                mb = int(request.POST['mb'])
                xoinicialb = xob
                riTiempo = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

                print (riLlegadas, riServicio, len(riLlegadas), len(riServicio))

            elif metodoa == 'Multiplicativo':

                # variables de numeros Llegadas
                a = int(request.POST['a'])
                n = int(request.POST['n'])
                xo = int(request.POST['xo'])
                m = int(request.POST['m'])
                xoinicial = xo
                riDemanda = metodo_multiplicativo(a, xo, xoinicial, m, n)

                # variables de numeros Servicio
                ab = int(request.POST['ab'])
                nb = int(request.POST['nb'])
                xob = int(request.POST['xob'])
                mb = int(request.POST['mb'])
                xoinicialb = xob
                riTiempo = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

            elif metodoa == 'Manual':
                riDemanda = request.POST.getlist('riDemanda')
                riTiempo = request.POST.getlist('riTiempo')
            # r = 5
            # q = 10
            # inv = 15
            # co = 20
            # ch = 5
            # cf = 10
            r = int(request.POST['r'])
            q = int(request.POST['q'])
            inv = int(request.POST['inventario'])
            co = int(request.POST['co'])
            ch = int(request.POST['ch'])
            cf = int(request.POST['cf'])





            for i in range(len(demandaInventario)):
                inventarioDemanda = demandaInventario[i]
                valorInventario= inventarioValor[i]

                minventarioDemanda.append(inventarioDemanda)
                minventarioValor.append(valorInventario)
            for i in range(len(demandaTiempo)):
                tiempoDemanda = demandaTiempo[i]
                valorTiempo = tiempoValor[i]
                mtiempoDemanda.append(tiempoDemanda)
                mtiempoValor.append(valorTiempo)
            for i in range(len(riDemanda)):
                demanda = float(riDemanda[i])
                matrizDemanda.append(demanda)

            for i in range(len(riTiempo)):
                Tiempo = float(riTiempo[i])
                matrizTiempo.append(Tiempo)
                #
            # valor = [1, 2, 3, 4, 5]
            valor = minventarioDemanda
            # px = [0.05, 0.25, 0.35, 0.20, 0.15]
            px = minventarioValor
            # valor1 = [2, 3, 4, 5]
            # px1 = [0.20, 0.50, 0.20, 0.10]
            valor1 = mtiempoDemanda
            px1 = mtiempoValor

            # deman = [0.339, 0.431, 0.241, 0.304, 0.132, 0.071, 0.913, 0.941, 0.698, 0.657]
            # retra = [0.104, 0.318, 0.183, 0.773, 0.250, 0.561, 0.286, 0.599, 0.149, 0.058]
            deman = matrizDemanda
            retra = matrizTiempo

            lista_total = inventarioMonte(r, q, inv, co, ch, cf, valor, px, valor1, px1, deman, retra)
            


            print('el resutado',lista_total)
            


            datos.append([r,q,inv,co,ch,cf])

            
            demanda= calculoMontecarloLista(valor,px,deman)
            lvalor=demanda[0]
            lpx=demanda[1]
            lfrecuen=demanda[2]
            ldesde=demanda[3]
            lhasta=demanda[4]
            
            l_deman=[]
            for i in range(0,len(demanda[0])):
                l_deman.append({'valor':lvalor[i],'px':lpx[i],"frecuencia":lfrecuen[i],"desde":ldesde[i],"hasta":lhasta[i]})
                    

            retraso= calculoMontecarloLista(valor,px,retra)
            lvalo1r=retraso[0]
            lpx1=retraso[1]
            lfrecuen1=retraso[2]
            ldesde1=retraso[3]
            lhasta1=retraso[4]
            
            l_retra=[]
            for i in range(0,len(retraso[0])):
                l_retra.append({'valor':lvalor[i],'px':lpx[i],"frecuencia":lfrecuen[i],"desde":ldesde[i],"hasta":lhasta[i]})
            
            #print(l_deman)

            context = {
                'inventario': lista_total,
                'datos':datos,
                'montecarloDemanda':l_deman,
                'montecarloRetraso':l_retra,
            }

            return render(request, 'inventario/index.html',context)

    return render(request, 'inventario/index.html')


