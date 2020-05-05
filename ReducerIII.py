#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la ocurrencia de un candidato,
# el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

cant = 0
distritoAnt = None
candidatoAnt = None

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteCandidato, esteDistrito  = DataIn
    
    if distritoAnt and distritoAnt != esteDistrito and candidatoAnt == esteCandidato:
        print (esteCandidato, "\t", distritoAnt,"\t",cant)
        cant = 0

    if candidatoAnt and candidatoAnt != esteCandidato:
        print (candidatoAnt, "\t", distritoAnt,"\t",cant)
        candidatoAnt = esteCandidato
        cant = 0

    candidatoAnt = esteCandidato
    distritoAnt = esteDistrito
    cant += 1

if candidatoAnt != None:
    print (candidatoAnt, "\t", distritoAnt,"\t",cant)

