# Ejemplo en el cual suponemos que administramos la materia progra 1
# Vamos a importar de otra manera que en el ejemplo 1

# El modulo se "trae" al main mediante la palabra reservada import
# mediante la palabra from se puede acceder a un modulo y luego seleccionar
# qué se importa utilizando import
from paquete.modulo_1 import presentar_materia

presentar_materia()

# Calcular promedio no funciona porque no esta importada
calcular_promedio()