#!/usr/bin/python3

import sys

Acumulados = 0
candidatoAnt = None
valorAnt = None

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteCandidato, esteValor  = DataIn
    
    if valorAnt and valorAnt != esteValor and candidatoAnt == candidatoAnt:
        text = esteCandidato + "\t" + valorAnt + "\t" + str(Acumulados)
        print(text)
        Acumulados = 0

    if candidatoAnt and candidatoAnt != esteCandidato:
        text = candidatoAnt + "\t" + valorAnt + "\t" + str(Acumulados)
        print (text)
        candidatoAnt = esteCandidato;
        Acumulados = 0

    candidatoAnt = esteCandidato
    valorAnt = esteValor
    Acumulados += 1

if candidatoAnt != None:
    text = candidatoAnt + "\t" + valorAnt + "\t" + str(Acumulados)
    print (text)

