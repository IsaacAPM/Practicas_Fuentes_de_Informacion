#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la ocurrencia de un candidato,
# el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

candidatoAnt = None
resp = {}
candiDist = {}

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteCandidato, esteDist  = DataIn

    if not (candiDist.get(esteDist) == None):
        candiDist[esteDist] += 1
    else:
        candiDist[esteDist] = 1

    if candidatoAnt and candidatoAnt != esteCandidato:
        resp[candidatoAnt] = candiDist
        candiDist = {}

    candidatoAnt = esteCandidato

if candidatoAnt != None:
    resp[candidatoAnt] = candiDist
    candiDist = {}

for candidato,distritos in resp:
    for distritos,cant in distritos:
        print(candidato,"\t",distritos,"\t",cant)
