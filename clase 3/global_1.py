# Variables globales
numero_a = 44

def restar(numero_b: int) -> int:
    #variable global
    global numero_a
    numero_a = 16  
    #Variable local: numero_b
    return numero_a - numero_b

# La variable global cambia de valor cuando llamo a la función

print(numero_a) #Acá es 44
print(restar(2)) #Acá es 16-2

print(numero_a) #Acá es 16




