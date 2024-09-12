def calcular_factorial(n : int) -> int:
    
    # inicializamos multiplicación en 1 para poder arrancar del n original
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1    
    
    return resultado

