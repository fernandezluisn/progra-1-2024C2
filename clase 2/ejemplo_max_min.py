lista_numeros = [1, 33, 77, 33, 2, 3, 88]

# busco máximo y mínimo al mismo tiempo usando una bandera

bandera = True

for numero in lista_numeros:    
    if bandera == False:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero        
    else:
        maximo = numero
        minimo = numero
        bandera = False
        
            
print(maximo)
print(minimo)
    
