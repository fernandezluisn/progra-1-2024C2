def calcular_factorial_r(n: int) -> int :
    
    '''Recibe un entero y devuelve su factorial'''

    
    
    if n > 0:        
        resultado = n * calcular_factorial_r(n-1)
        return resultado
    else:
        return 1
    
    

    


