# Mostrar por pantalla solo los números múltiplos de 3
for numero in range(1, 20):
    
    if not (numero % 3) == 0: #identifico al número que no es divisible por 3
        continue # Salteo esos casos
    else:
        print(f"El número es {numero}")