# Variables globales
a = "Palabra"
b = 33
numero_a = 44

def restar(numero_b: int) -> int:
    #variable global
    global numero_a
    numero_a = 16  
    #Variables local: numero_b
    return numero_a - numero_b

print(numero_a)
print(restar(2))
print(a)
print(numero_a)




