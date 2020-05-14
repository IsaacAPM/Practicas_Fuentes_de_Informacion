#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la ocurrencia de un candidato,
# el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

distritoAnt = None
resp = {}
distCand = {}

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteDistrito, esteCand  = DataIn

    if (not (distCand.get(esteDistrito) == None)) and esteDistrito == distritoAnt:
        distCand[esteCand] += 1
    elif esteDistrito == distritoAnt:
        distCand[esteCand] = 1

    if distritoAnt and distritoAnt != esteCand:
        resp[distritoAnt] = distCand
        distCand = {}

    distritoAnt = esteDistrito

if distritoAnt != None:
    resp[distritoAnt] = distCand
    distCand = {}

