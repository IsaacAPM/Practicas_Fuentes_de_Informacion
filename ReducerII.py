#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Problema II

import sys

Acumulados = 0
DistritoAnt = None
maxi = ["",-1]
mini = ["",-1]
i = 0

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteDistrito, esteValor  = DataIn

    if DistritoAnt and DistritoAnt != esteDistrito:
        print (DistritoAnt, "\t", Acumulados)
        if i == 0:
            mini[0] = DistritoAnt
            mini[1] = Acumulados
            maxi[0] = DistritoAnt
            maxi[1] = Acumulados
            i += 1
        elif Acumulados < mini[1]:
            mini[0] = DistritoAnt
            mini[1] = Acumulados
        elif Acumulados > maxi[1]:
            maxi[0] = DistritoAnt
            maxi[1] = Acumulados
        DistritoAnt = esteDistrito
        Acumulados = 0

    DistritoAnt = esteDistrito
    Acumulados += 1

if DistritoAnt != None:
    print (DistritoAnt, "\t", Acumulados)
    if Acumulados < mini[1]:
        mini[0] = DistritoAnt
        mini[1] = Acumulados
    elif Acumulados > maxi[1]:
        maxi[0] = DistritoAnt
        maxi[1] = Acumulados

print("Distrito con más encuestas","\t",maxi[0])
print("Distrito con menos encuestas","\t",mini[0])

