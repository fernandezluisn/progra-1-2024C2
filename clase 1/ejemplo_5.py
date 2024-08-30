edad = int(input("¿Cuál es tu edad?"))

# Forma correcta de validar. No usar if.
while edad < 0 or edad > 120:
    print("La edad no puede ser menor a 0, ni mayor a 120")
    edad = int(input("¿Cuál es tu edad?"))

print(edad)
