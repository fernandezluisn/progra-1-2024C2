# Si recibe 0, por defecto funciona 996 veces. A partir de 997 falla. 
# Esto se debe a que la recursividad tiene un límite
def imprimir_n(n: int):
    if n > int(-996):
        imprimir_n(n-1)
        print(n)

imprimir_n(0)