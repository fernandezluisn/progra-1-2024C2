# Resolución del ejercicio 6a de la primera guía

lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ['Juan', 'Matias', 'Carla', 'Susana', 
                'Olivia', 'Carlos', 'Daniel', 'Jimena', 
                'Mariela', 'Ignacio']

# utilizo bandera para inicializar mínimo y máximo
bandera = True

for index in range(len(lista_edad)):
    
    if bandera == True:
        
        nom_maximo = lista_nombres[index]
        edad_maximo = lista_edad[index]
        nom_minimo = lista_nombres[index]
        edad_minimo = lista_edad[index]
        bandera = False

    else:

        if lista_edad[index] > edad_maximo:
            nom_maximo = lista_nombres[index]
            edad_maximo = lista_edad[index]

        elif lista_edad[index] < edad_minimo:
            nom_minimo = lista_nombres[index]
            edad_minimo = lista_edad[index]

print(f"La edad mínima es {edad_minimo} y corresponde a {nom_minimo}")
print(f"La edad máxima es {edad_maximo} y corresponde a {nom_maximo}")


