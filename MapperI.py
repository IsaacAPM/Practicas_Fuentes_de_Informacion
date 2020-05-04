# Selecciona campos de archivo CSV votacion
# Formato de cada linea es:
# Hora, Genero, Distrito, Candidato
#
# Este filtro toma dos elementos de stdin y entrega en stdout
# esos elementos como <key,value> separados por tab
# 
      
import sys 

distri = {}

for Line in sys.stdin:
    Data = Line.strip().split(",")

    if len(Data) == 4:
        hora, genero, distrito, candidato = Data
        
        if distri.get(distrito) == None:
            print("{0}\t{1}".format(distrito,1))
            distri[distrito] = 1
        else:
            print("{0}\{1}".format(distrito,0))
            

    