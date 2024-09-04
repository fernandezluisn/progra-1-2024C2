# las definiciones de la función son indicativas
def dividir(numero_a : int, numero_b : int = 2) -> int:

    #Si quiero restringir que numero_a sea entero, debo forzarlo en el código. 
    if type(numero_a) != int:
        if type(numero_a) == float:
            numero_a = int(numero_a)
    
    resultado = numero_a / numero_b
    
    return resultado


resultado_division = dividir(13.6)
print(resultado_division)
print(type(resultado_division))