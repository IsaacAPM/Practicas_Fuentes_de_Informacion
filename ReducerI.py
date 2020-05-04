# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:43:04 2020

@author: ipimentem
"""

#!/usr/bin/python3
#
# Toma datos de la entrada <key\tval> y los procesa
# Como val solo es "1" para la primera ocurrencia de un distrito y
# 0 para todas las demas el procesamiento simplemente es un acumulador
# 
# Recuerde que los datos ya llegan ordenados, por lo que
# al detectar cambio de candidato, se despliega el resultado

import sys

Acumulados = 0

for line in sys.stdin:
    DataIn = line.strip().split("\t")
    if len(DataIn) != 2:
        # Hay algo raro, ignora esta linea
        continue

    esteDistrito, esteValor  = DataIn

    Acumulados += esteValor

print ("Total de distritos", "\t", Acumulados)