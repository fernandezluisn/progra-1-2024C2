base = 2
potencia = 10

print(base ** potencia)

# res = 3 x 1
# res = res x 3
# res = res x 3
# res = res x 3
# res = res x 3

# Calcular potencia con un for
resultado = 1
for num in range(0, potencia):
    
    print(f"Resultado parcial = {resultado}")
    resultado *= base

print(f"Resultado final = {resultado}")
    