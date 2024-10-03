from burbujeo import *
from seleccion import *
from quick_sort import *
from insercion import *

lista_desordenada = ["as", "xc", "j", "l", "m", "ab", "xa"]

# aux = 3 [3, 44]
# aux = 45 [3, 44, 45]
# aux = 12 [3, 12, 44, 45]
# aux = 16 [3, 12, 16, 44, 45]
# aux = 17 [3, 12, 16, 17, 44, 45]
# aux = 99 [3, 12, 16, 17, 44, 45, 99]
# aux = 76 [3, 12, 16, 17, 44, 45, 76, 99]


lista_ordenada = ordenar_x_insercion(lista_desordenada)

print(lista_ordenada)