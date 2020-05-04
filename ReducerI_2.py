#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la ocurrencia de un candidato,
# el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

Acumulados = 0
distritoAnt = None

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteDistrito, esteValor  = DataIn

    if distritoAnt and distritoAnt != esteDistrito:
        distritoAnt = esteDistrito;
        Acumulados += 1

    distritoAnt = esteDistrito

if distritoAnt != None:
    Acumulados += 1

print ("Total de distritos", "\t", Acumulados)

