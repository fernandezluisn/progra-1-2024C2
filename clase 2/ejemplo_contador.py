# ejemplo de contador con un for

lista_numeros = [1, 33, 77, 33, 2, 3, 88, -3, 5, -22]
numero_a_identificar = 33
conteo = 0

for numero in lista_numeros:
    if numero == numero_a_identificar:
        conteo += 1

print(conteo)