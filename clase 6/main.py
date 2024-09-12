from recursividad import calcular_factorial_r
from norecursivo.factorial_while import calcular_factorial

# Voy a usar la libería time de python para comparar tiempos de ejecución
# Después del primer parcial vamos a empezar a usar librerías de terceros con
# mayor libertad. Por ahora solo en este caso de ejemplo
import time

# Calculo demora de factorial recursivo
inicio = time.time()
calcular_factorial_r(900)
fin = time.time()

duracion_r = fin - inicio

# calculo demora de factorial con while
inicio = time.time()
calcular_factorial(900)
fin = time.time()

duracion_w = fin - inicio

# comparo duración de la recursividad con el while.
# La recursividad suele ser más costosa.
print(duracion_r > duracion_w)
