# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:23:31 2020

@author: ipimentem
"""

# Selecciona campos de archivo CSV votacion
# Formato de cada linea es:
# Hora, Genero, Distrito, Candidato
#
# Este filtro toma dos elementos de stdin y entrega en stdout
# esos elementos como <key,value> separados por tab
# 

import sys

for Line in sys.stdin:
	Data = Line.strip().split(",")
    distri = {};
	if len(Data) == 4:
		hora, genero, distrito, candidato = Data
        if distri.get(distrito) == None:
            print("{0}\t{1}".format(distrito,1))
            distri[distrito] = 1
        else:
            print("{0}\t{1}".format(distrito,0))

    